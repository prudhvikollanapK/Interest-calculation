from django.db import models


class BookingPaymentSchedule(models.Model):
    booking_payment_schedule_id = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    invoice_no = models.CharField(max_length=100)
    invoice_on = models.DateField()
    due_date = models.DateField()
    is_special_schedule = models.BooleanField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage_no = models.IntegerField()
    stage_name = models.CharField(max_length=255)
    booking_id = models.IntegerField()
    payment_schedule_id = models.IntegerField()


class PaymentReceiptMaster(models.Model):
    payment_receipt_master_id = models.IntegerField()
    receipt_no = models.IntegerField()
    pay_pattern = models.TextField()
    mode_of_pay = models.TextField()
    transaction_details = models.TextField()
    bank_name = models.TextField()
    branch_name = models.TextField()
    amount = models.IntegerField()
    transaction_date = models.DateField()
    reference_doc = models.TextField(blank=True)
    is_booking_receipt = models.BooleanField(default=False)
    comments = models.TextField(blank=True)
    advance_amount = models.IntegerField()
    milestone_amount = models.IntegerField()
    status = models.TextField()
    created_on = models.DateField()
    created_on_new = models.TextField(blank=True)
    bank_details_id = models.IntegerField()
    booking_id = models.IntegerField()
    created_by_id = models.IntegerField()
    customer_receipt = models.TextField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return f"Payment Receipt {self.receipt_no}"


class PaymentReceiptReferences(models.Model):
    payment_receipt_references_id = models.IntegerField()
    against = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    object_id = models.IntegerField()
    content_type_id = models.IntegerField()
    receipt_id = models.IntegerField()

    def __str__(self):
        return f"PaymentReceiptReferences {self.id}"


class CreditsNotesMaster(models.Model):
    credits_notes_master_id = models.IntegerField()
    notes_no = models.CharField(max_length=100)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    milestone_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_approved = models.BooleanField()
    reject_reason = models.TextField()
    approved_on = models.DateField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    approved_by_id = models.IntegerField()
    booking_id = models.IntegerField()
    category_id = models.IntegerField()
    created_by_id = models.IntegerField()


class CreditsNotesReferences(models.Model):
    credits_notes_references_id = models.IntegerField()
    against = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    object_id = models.IntegerField()
    content_type_id = models.IntegerField()
    notes_id = models.IntegerField()
