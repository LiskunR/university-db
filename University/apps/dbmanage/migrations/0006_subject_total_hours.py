# Generated by Django 3.2.3 on 2021-05-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmanage', '0005_teacher_teacher_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='total_hours',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Всего часов'),
        ),
    ]
