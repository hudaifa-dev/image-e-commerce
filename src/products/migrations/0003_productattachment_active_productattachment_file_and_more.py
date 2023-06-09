# Generated by Django 4.1.7 on 2023-03-27 23:12

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_productattachment_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="productattachment",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="productattachment",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    location="/Users/hudaifa/Documents/Backend/image-e-commerce/local-cdn/protected"
                ),
                upload_to=products.models.handle_product_attachment_upload,
            ),
        ),
        migrations.AddField(
            model_name="productattachment",
            name="is_free",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productattachment",
            name="name",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="productattachment",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="productattachment",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productattachment",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
