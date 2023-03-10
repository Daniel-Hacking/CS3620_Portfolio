# Generated by Django 2.2 on 2023-02-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_auto_20230222_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=32)),
                ('contact_email', models.CharField(max_length=64)),
                ('contact_message', models.CharField(max_length=256)),
            ],
        ),
    ]
