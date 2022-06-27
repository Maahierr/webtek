# Generated by Django 4.0.4 on 2022-06-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_product_prod_img_product_prod_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_img',
            new_name='prod_img_main',
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img_back',
            field=models.ImageField(default='', upload_to='prod_img'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img_side',
            field=models.ImageField(default='', upload_to='prod_img'),
        ),
    ]
