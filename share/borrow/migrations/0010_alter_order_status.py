# Generated by Django 4.2.11 on 2024-05-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("borrow", "0009_order_airdropamount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("wait_to_pay", "Wait To Pay"),
                    ("pending", "Pending"),
                    ("unpaid", "Unpaid"),
                    ("accept", "Accept"),
                    ("deny", "Deny"),
                    ("cancel_order", "Cancel Order"),
                    ("approve_expired", "Approve Expired"),
                    ("not_picked_up", "Not Picked Up"),
                    ("get_item", "Get Item"),
                    ("return_item", "Return Item"),
                    ("borrower_comment", "Borrower Comment"),
                    ("finish", "Finish"),
                ],
                max_length=32,
            ),
        ),
    ]
