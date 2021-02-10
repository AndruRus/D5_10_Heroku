# Generated by Django 2.2.6 on 2021-02-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20210204_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishinghouse',
            name='city',
            field=models.TextField(null='-', verbose_name='Город'),
            preserve_default='-',
        ),
        migrations.AddField(
            model_name='publishinghouse',
            name='country',
            field=models.CharField(max_length=2, null='-', verbose_name='Страна'),
            preserve_default='-',
        ),
    ]