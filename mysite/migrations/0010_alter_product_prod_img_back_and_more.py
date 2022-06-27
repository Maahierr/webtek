# Generated by Django 4.0.4 on 2022-06-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_product_prod_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img_back',
            field=models.ImageField(blank=True, upload_to='prod_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img_main',
            field=models.ImageField(blank=True, upload_to='prod_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img_other',
            field=models.ImageField(blank=True, default='', upload_to='prod_img'),
            preserve_default=False,
        ),
    ]