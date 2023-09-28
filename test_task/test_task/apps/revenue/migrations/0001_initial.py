# Generated by Django 4.2.5 on 2023-09-28 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevenueStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('revenue', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('spend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spend.spendstatistic')),
            ],
        ),
    ]
