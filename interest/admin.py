from django.contrib import admin
from .models import (
    BookingPaymentSchedule,
    PaymentReceiptMaster,
    PaymentReceiptReferences,
    CreditsNotesMaster,
    CreditsNotesReferences,
)


@admin.register(BookingPaymentSchedule)
class BookingPaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'percentage', 'gst_percentage', 'invoice_no', 'invoice_on', 'due_date', 'is_special_schedule', 'amount', 'gst', 'total_amount', 'total_paid_amount', 'total_balance_amount', 'stage_no', 'stage_name','booking_id', 'payment_schedule_id')
    list_filter = ('percentage', 'due_date')
    search_fields = ('gst_percentage', 'due_date')
    date_hierarchy = 'due_date'


@admin.register(PaymentReceiptMaster)
class PaymentReceiptMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'receipt_no', 'transaction_date', 'amount', 'reference_doc', 'is_booking_receipt')
    list_filter = ('transaction_date', 'is_booking_receipt')
    search_fields = ('receipt_no', 'transaction_details')
    date_hierarchy = 'transaction_date'


@admin.register(PaymentReceiptReferences)
class PaymentReceiptReferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'against', 'amount')
    search_fields = ('against', 'amount')
    list_filter = ('amount',)


@admin.register(CreditsNotesMaster)
class CreditsNotesMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'notes_no', 'transaction_date', 'amount', 'description', 'is_approved', 'approved_on')
    list_filter = ('transaction_date', 'is_approved', 'approved_on')
    search_fields = ('notes_no', 'description')
    date_hierarchy = 'transaction_date'


@admin.register(CreditsNotesReferences)
class CreditsNotesReferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'against', 'amount')
    search_fields = ('against', 'amount')
    list_filter = ('amount',)
