import pytz
from datetime import datetime
import pandas as pd
from django.core.management.base import BaseCommand
from interest.models import (
    BookingPaymentSchedule,
    PaymentReceiptMaster,
    PaymentReceiptReferences,
    CreditsNotesMaster,
    CreditsNotesReferences,
)


class Command(BaseCommand):
    help = 'Imports data from Excel into Django models'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Excel file path')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        xl = pd.ExcelFile(file_path)

        try:
            self.import_booking_payment_schedule(xl)
            self.import_payment_receipt_references(xl)
            self.import_credits_notes_master(xl)
            self.import_credits_notes_references(xl)
            self.import_payment_receipt_master(xl)

        except KeyError as e:
            if e.args[0] == 'tbl_booking_payment_schedule':
                table_name = 'tbl_booking_payment_schedule'
            elif e.args[0] == 'tbl_payment_receipt_references':
                table_name = 'tbl_payment_receipt_references'
            elif e.args[0] == 'tbl_credits_notes_master':
                table_name = 'tbl_credits_notes_master'
            elif e.args[0] == 'tbl_credits_notes_references':
                table_name = 'tbl_credits_notes_references'
            elif e.args[0] == 'tbl_payment_receipt_master':
                table_name = 'tbl_payment_receipt_master'
            else:
                table_name = 'Unknown Worksheet'

            raise ValueError(f"Column '{e.args[0]}' not found in the worksheet '{table_name}'.")

    def import_booking_payment_schedule(self, xl):
        sheet_name = 'tbl_booking_payment_schedule'
        try:
            if sheet_name.strip() not in xl.sheet_names:
                raise KeyError(sheet_name)

            df = xl.parse(sheet_name.strip())
            df.columns = df.columns.str.strip()

            for index, row in df.iterrows():
                try:
                    stage_no = row.get('stage_no')
                    stage_name = row.get('stage_name')

                    BookingPaymentSchedule.objects.create(
                        booking_payment_schedule_id = row['id'],
                        percentage=row['percentage'],
                        gst_percentage=row['gst_percentage'],
                        invoice_no=row['invoice_no'],
                        invoice_on=row['invoice_on'],
                        due_date=row['due_date'],
                        is_special_schedule=row['is_special_schedule'],
                        amount=row['amount'],
                        gst=row['gst'],
                        total_amount=row['total_amount'],
                        total_paid_amount=row['total_paid_amount'],
                        total_balance_amount=row['total_balance_amount'],
                        stage_no=stage_no,
                        stage_name=stage_name,
                        booking_id=row['booking_id'],
                        payment_schedule_id=row['payment_schedule_id'],
                    )

                except KeyError as e:
                    print(f"KeyError: Column '{e.args[0]}' not found in '{sheet_name}'")
                    raise

        except KeyError:
            raise ValueError(f"Worksheet named '{sheet_name}' not found")

        except Exception as e:
            raise ValueError(f"Error processing '{sheet_name}' worksheet: {str(e)}")

    def import_credits_notes_references(self, xl):
        try:
            df = xl.parse('tbl_credits_notes_references')

            for index, row in df.iterrows():
                CreditsNotesReferences.objects.create(
                    credits_notes_references_id=row['id'],
                    against=row['against'],
                    amount=row['amount'],
                    object_id=row['object_id'],
                    content_type_id=row['content_type_id'],
                    notes_id=row['notes_id'],
                )

        except KeyError:
            raise ValueError("Worksheet named 'tbl_credits_notes_references' not found")

        except Exception as e:
            raise ValueError(f"Error processing 'tbl_credits_notes_references' worksheet: {str(e)}")

    def import_credits_notes_master(self, xl):
        sheet_name = 'tbl_credits_notes_master'
        try:
            if sheet_name not in xl.sheet_names:
                raise ValueError(f"Worksheet named '{sheet_name}' not found")

            df = xl.parse(sheet_name)
            timezone = pytz.UTC

            for index, row in df.iterrows():
                is_approved = None
                if pd.notna(row['is_approved']):
                    if isinstance(row['is_approved'], bool):
                        is_approved = row['is_approved']
                    elif isinstance(row['is_approved'], str):
                        is_approved = row['is_approved'].lower() == 'true'
                    elif isinstance(row['is_approved'], (int, float)):
                        is_approved = bool(row['is_approved'])
                    else:
                        print(f"Warning: Unexpected type for is_approved value at row {index + 2}")
                if is_approved is None:
                    is_approved = False

                id = int(row['id'])
                notes_no = str(row['notes_no']) if pd.notna(row['notes_no']) else None
                transaction_date = pd.to_datetime(row['transaction_date'], format='%d/%m/%Y').date() if pd.notna(
                    row['transaction_date']) else None
                amount = float(row['amount']) if pd.notna(row['amount']) else None
                advance_amount = float(row['advance_amount']) if pd.notna(row['advance_amount']) else None
                milestone_amount = float(row['milestone_amount']) if pd.notna(row['milestone_amount']) else None
                description = str(row['description']) if pd.notna(row['description']) else None
                reject_reason = str(row['reject_reason']) if pd.notna(
                    row['reject_reason']) else 'N/A'
                approved_on = pd.to_datetime(row['approved_on'], format='%d/%m/%Y %H:%M:%S') if pd.notna(
                    row['approved_on']) else timezone.localize(datetime.now())
                created_on = pd.to_datetime(row['created_on'], format='%d/%m/%Y %H:%M:%S') if pd.notna(
                    row['created_on']) else None
                updated_on = pd.to_datetime(row['updated_on'], format='%d/%m/%Y %H:%M:%S') if pd.notna(
                    row['updated_on']) else None
                approved_by_id = int(row['approved_by_id']) if pd.notna(row['approved_by_id']) else None
                booking_id = int(row['booking_id']) if pd.notna(row['booking_id']) else None
                category_id = int(row['category_id']) if pd.notna(row['category_id']) else None
                created_by_id = int(row['created_by_id']) if pd.notna(row['created_by_id']) else None

                def localize_if_naive(dt):
                    if dt and dt.tzinfo is None:
                        return timezone.localize(dt)
                    return dt

                created_on = localize_if_naive(created_on)
                updated_on = localize_if_naive(updated_on)
                approved_on = localize_if_naive(approved_on)

                if approved_by_id is None:
                    approved_by_id = 1

                try:
                    CreditsNotesMaster.objects.create(
                        credits_notes_master_id=id,
                        notes_no=notes_no,
                        transaction_date=transaction_date,
                        amount=amount,
                        advance_amount=advance_amount,
                        milestone_amount=milestone_amount,
                        description=description,
                        is_approved=is_approved,
                        reject_reason=reject_reason,
                        approved_on=approved_on,
                        created_on=created_on,
                        updated_on=updated_on,
                        approved_by_id=approved_by_id,
                        booking_id=booking_id,
                        category_id=category_id,
                        created_by_id=created_by_id,
                    )
                except Exception as ex:
                    print(f"Error creating CreditsNotesMaster object at row {index + 2}: {str(ex)}")

        except KeyError as ke:
            raise ValueError(f"Column '{ke.args[0]}' not found in the worksheet '{sheet_name}'.")

        except Exception as e:
            raise ValueError(f"Error processing '{sheet_name}' worksheet: {str(e)}")

    def import_payment_receipt_master(self, excel_file):
        try:
            df = pd.read_excel(excel_file, sheet_name='tbl_payment_receipt_master')
            print(f"Loaded worksheet 'tbl_payment_receipt_master' with {len(df)} rows.")

            for index, row in df.iterrows():
                try:
                    print(f"Processing row {index + 2}")
                    transaction_date = row['transaction_date'].date()
                    created_on = row['created_on'].date()
                    updated_on = row['updated_on']
                    reference_doc = str(row['reference_doc']) if not pd.isna(row['reference_doc']) else ''
                    comments = str(row['comments']) if not pd.isna(row['comments']) else ''
                    bank_name = str(row['bank_name']) if not pd.isna(row['bank_name']) else ''
                    branch_name = str(row['branch_name']) if not pd.isna(row['branch_name']) else ''
                    is_booking_receipt = bool(row['is_booking_receipt'])
                    id = int(row['id'])
                    receipt_no = int(row['receipt_no'])
                    pay_pattern = str(row['pay_pattern'])
                    mode_of_pay = str(row['mode_of_pay'])
                    transaction_details = str(row['transaction_details'])
                    status = str(row['status'])
                    customer_receipt = str(row['customer_receipt'])

                    print(f"Creating PaymentReceiptMaster object for row {index + 2}")

                    receipt = PaymentReceiptMaster.objects.create(
                        payment_receipt_master_id = id,
                        receipt_no=receipt_no,
                        pay_pattern=pay_pattern,
                        mode_of_pay=mode_of_pay,
                        transaction_details=transaction_details,
                        bank_name=bank_name,
                        branch_name=branch_name,
                        amount=row['amount'],
                        transaction_date=transaction_date,
                        reference_doc=reference_doc,
                        is_booking_receipt=is_booking_receipt,
                        comments=comments,
                        advance_amount=row['advance_amount'],
                        milestone_amount=row['milestone_amount'],
                        status=status,
                        created_on=created_on,
                        created_on_new=row['created_on_new'],
                        bank_details_id=row['bank_details_id'],
                        booking_id=row['booking_id'],
                        created_by_id=row['created_by_id'],
                        customer_receipt=customer_receipt,
                        updated_on=updated_on,
                    )

                    print(f"Successfully inserted row {index + 2} into the database.")

                except Exception as e:
                    print(f"Error processing row {index + 2}: {str(e)}")

        except KeyError:
            raise ValueError("Worksheet named 'tbl_payment_receipt_master' not found")

        except Exception as e:
            raise ValueError(f"Error processing 'tbl_payment_receipt_master' worksheet: {str(e)}")

    def import_payment_receipt_references(self, xl):
        try:
            df = xl.parse('tbl_payment_receipt_references')

            for index, row in df.iterrows():
                PaymentReceiptReferences.objects.create(
                    payment_receipt_references_id=row['id'],
                    against=row['against'],
                    amount=row['amount'],
                    object_id=row['object_id'],
                    content_type_id=row['content_type_id'],
                    receipt_id=row['receipt_id'],
                )

        except KeyError:
            raise ValueError("Worksheet named 'tbl_payment_receipt_references' not found")

        except Exception as e:
            raise ValueError(f"Error processing 'tbl_payment_receipt_references' worksheet: {str(e)}")


