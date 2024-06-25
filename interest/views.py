from django.shortcuts import render
from .models import BookingPaymentSchedule, PaymentReceiptReferences, PaymentReceiptMaster
from decimal import Decimal
import pandas as pd
from django.http import HttpResponse
from io import StringIO
import xlsxwriter


def calculate_interest_report(request):
    report_data = []

    try:
        schedules = BookingPaymentSchedule.objects.all()

        for schedule in schedules:
            due_amount = schedule.total_amount

            payments = PaymentReceiptReferences.objects.filter(object_id=schedule.booking_payment_schedule_id)

            for payment in payments:
                try:
                    payment_master = PaymentReceiptMaster.objects.get(payment_receipt_master_id=payment.receipt_id)
                    received_date = payment_master.transaction_date
                except PaymentReceiptMaster.DoesNotExist:
                    received_date = None

                no_of_delays = (schedule.due_date - received_date).days if received_date else 0

                interest = (payment.amount * Decimal(str(no_of_delays)) * Decimal('10.25')) / Decimal('365')
                gst = interest * Decimal('0.18')
                total_interest = interest + gst

                report_data.append({
                    'flat_no': '1-B26',
                    'customer_code': 'CROS137600',
                    'customer_name': 'Mr. V.Sundaram',
                    'description': f'{schedule.stage_name} & {schedule.percentage}',
                    'due_date': schedule.due_date,
                    'due_amount': due_amount,
                    'received_date': received_date,
                    'receipt_type': 'Receipt',
                    'amount_received': payment.amount,
                    'no_of_delays': no_of_delays,
                    'percentage': Decimal('10.25'),
                    'interest': interest,
                    'gst': gst,
                    'total_interest': total_interest,
                })
                due_amount -= payment.amount

        print(f"Final report_data: {report_data}")

    except Exception as e:
        print(f"Error in calculate_interest_report: {str(e)}")
        report_data = []

    return render(request, 'interest_report.html', {'report_data': report_data})


def export_to_excel(request):
    try:
        response = calculate_interest_report(request)
        if isinstance(response, HttpResponse):
            html_content = response.content.decode('utf-8')
            html_io = StringIO(html_content)
            tables = pd.read_html(html_io)

            if not tables or len(tables) == 0:
                return HttpResponse("No data found in the interest report.")

            df = tables[0]
            response_excel = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response_excel['Content-Disposition'] = 'attachment; filename="interest_report.xlsx"'

            with pd.ExcelWriter(response_excel, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Interest Report', index=False)

            return response_excel

        else:
            return HttpResponse("Failed to export to Excel. Please try again later.")

    except Exception as e:
        print(f"Error in export_to_excel: {str(e)}")
        return HttpResponse("Failed to export to Excel. Please try again later.")
