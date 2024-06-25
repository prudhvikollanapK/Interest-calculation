# Generated by Django 4.2.13 on 2024-06-25 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookingPaymentSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("booking_payment_schedule_id", models.IntegerField()),
                ("percentage", models.DecimalField(decimal_places=2, max_digits=5)),
                ("gst_percentage", models.DecimalField(decimal_places=2, max_digits=5)),
                ("invoice_no", models.CharField(max_length=100)),
                ("invoice_on", models.DateField()),
                ("due_date", models.DateField()),
                ("is_special_schedule", models.BooleanField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gst", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "total_paid_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "total_balance_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("stage_no", models.IntegerField()),
                ("stage_name", models.CharField(max_length=255)),
                ("booking_id", models.IntegerField()),
                ("payment_schedule_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="CreditsNotesMaster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("credits_notes_master_id", models.IntegerField()),
                ("notes_no", models.CharField(max_length=100)),
                ("transaction_date", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "advance_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "milestone_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("description", models.TextField()),
                ("is_approved", models.BooleanField()),
                ("reject_reason", models.TextField()),
                ("approved_on", models.DateField()),
                ("created_on", models.DateTimeField()),
                ("updated_on", models.DateTimeField()),
                ("approved_by_id", models.IntegerField()),
                ("booking_id", models.IntegerField()),
                ("category_id", models.IntegerField()),
                ("created_by_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="CreditsNotesReferences",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("credits_notes_references_id", models.IntegerField()),
                ("against", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("object_id", models.IntegerField()),
                ("content_type_id", models.IntegerField()),
                ("notes_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PaymentReceiptMaster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_receipt_master_id", models.IntegerField()),
                ("receipt_no", models.IntegerField()),
                ("pay_pattern", models.TextField()),
                ("mode_of_pay", models.TextField()),
                ("transaction_details", models.TextField()),
                ("bank_name", models.TextField()),
                ("branch_name", models.TextField()),
                ("amount", models.IntegerField()),
                ("transaction_date", models.DateField()),
                ("reference_doc", models.TextField(blank=True)),
                ("is_booking_receipt", models.BooleanField(default=False)),
                ("comments", models.TextField(blank=True)),
                ("advance_amount", models.IntegerField()),
                ("milestone_amount", models.IntegerField()),
                ("status", models.TextField()),
                ("created_on", models.DateField()),
                ("created_on_new", models.TextField(blank=True)),
                ("bank_details_id", models.IntegerField()),
                ("booking_id", models.IntegerField()),
                ("created_by_id", models.IntegerField()),
                ("customer_receipt", models.TextField()),
                ("updated_on", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="PaymentReceiptReferences",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_receipt_references_id", models.IntegerField()),
                ("against", models.CharField(max_length=100)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("object_id", models.IntegerField()),
                ("content_type_id", models.IntegerField()),
                ("receipt_id", models.IntegerField()),
            ],
        ),
    ]
