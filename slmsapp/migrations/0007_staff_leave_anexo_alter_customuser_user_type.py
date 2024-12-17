# Generated by Django 5.1.2 on 2024-11-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0006_staff_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_leave',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='leave_attachments/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'staff')], default=1, max_length=50),
        ),
    ]
