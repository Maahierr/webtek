# Generated by Django 4.0.4 on 2022-06-26 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_alter_product_prod_img_fold_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_img_fold',
            new_name='prod_img_other',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prod_img_side',
        ),
    ]