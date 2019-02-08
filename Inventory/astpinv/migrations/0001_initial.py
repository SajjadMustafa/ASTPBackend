# Generated by Django 2.1.5 on 2019-01-18 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Department')),
            ],
        ),
        migrations.CreateModel(
            name='IssuanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=100)),
                ('iquantity', models.CharField(max_length=100)),
                ('idept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Department')),
            ],
        ),
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_po_or_pettycash', models.CharField(max_length=100)),
                ('po_number', models.CharField(max_length=100)),
                ('scanner_id', models.CharField(max_length=100)),
                ('po_company', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Date')),
                ('invoice_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Employee')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Department')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='ise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.StockEntry'),
        ),
        migrations.AddField(
            model_name='item',
            name='iunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Unit'),
        ),
        migrations.AddField(
            model_name='issuancerecord',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.Item'),
        ),
        migrations.AddField(
            model_name='issuancerecord',
            name='req_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='astpinv.User'),
        ),
    ]
