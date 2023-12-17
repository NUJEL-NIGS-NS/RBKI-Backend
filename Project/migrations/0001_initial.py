# Generated by Django 4.2.4 on 2023-10-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('lac', models.CharField(blank=True, max_length=255, verbose_name='Legistative assembly council')),
                ('local_bdy', models.CharField(blank=True, max_length=50, verbose_name='Local Body')),
                ('stage', models.CharField(blank=True, max_length=255, verbose_name='completed/under construction')),
                ('as_no', models.CharField(blank=True, max_length=255, verbose_name='administrative sanction no')),
                ('as_date', models.DateField(blank=True, verbose_name='administrative sanction date')),
                ('as_amt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='administrative sanction amount')),
                ('ts_no', models.CharField(blank=True, max_length=255, verbose_name='technical sanction no]')),
                ('ts_date', models.DateField(blank=True, verbose_name='technical sanction date')),
                ('ts_amt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='technical sanction amount')),
                ('reas_no', models.CharField(blank=True, max_length=255, verbose_name='revised administrative sanction no')),
                ('reas_date', models.DateField(blank=True, verbose_name='revised administrative sanction Date')),
                ('reas_amt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='revised administrative sanction Amount')),
                ('s_date', models.DateField(blank=True, verbose_name='Starting Date')),
                ('pro_cat', models.CharField(blank=True, max_length=255, verbose_name='Project Category')),
                ('length_km', models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='length')),
                ('lat_tude', models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='lattitude')),
                ('log_tude', models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='logitude')),
                ('status', models.CharField(blank=True, max_length=255, verbose_name='current progress')),
                ('piu', models.CharField(blank=True, max_length=255, verbose_name='PIU')),
                ('c_name', models.CharField(blank=True, max_length=255, verbose_name='contractor Name')),
                ('c_phone', models.BigIntegerField(blank=True, verbose_name='contractor phone')),
                ('c_email', models.EmailField(blank=True, max_length=254, verbose_name='contractor email')),
                ('c_pan', models.CharField(blank=True, max_length=50, verbose_name='contractor_PAN')),
                ('tender_no', models.CharField(blank=True, max_length=255, verbose_name='Tender Number')),
                ('tender_data', models.DateField(blank=True, verbose_name='Tender Date')),
                ('tender_amt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='Tender Amount')),
                ('agr_no', models.CharField(blank=True, max_length=50, verbose_name='agreement no')),
                ('agr_date', models.DateField(blank=True, verbose_name='agreement date')),
                ('arg_amt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='agreement amount')),
                ('hand_to_date', models.DateField(blank=True, verbose_name='handover date]')),
                ('period', models.CharField(blank=True, max_length=50, verbose_name='period of completion')),
                ('completion_date', models.DateField(blank=True, verbose_name='Complition Date')),
                ('utility', models.CharField(blank=True, max_length=50, verbose_name='utility shifting&its amount')),
                ('mait_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='maintenance charge')),
                ('total_exp', models.DecimalField(blank=True, decimal_places=4, max_digits=8, verbose_name='Total Expenditure')),
                ('fin_pro', models.IntegerField(blank=True, verbose_name='financial Progress')),
                ('phy_pro', models.IntegerField(blank=True, verbose_name='Physical Progress')),
                ('updated_by', models.CharField(blank=True, max_length=50, verbose_name='Updated By')),
                ('last_upd', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, upload_to='Videos/', verbose_name='video')),
                ('pro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project', verbose_name='Project Name')),
            ],
        ),
        migrations.CreateModel(
            name='Project_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='Images', verbose_name='image')),
                ('pro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project', verbose_name='Project Name')),
            ],
        ),
        migrations.CreateModel(
            name='Project_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(blank=True, upload_to='Docs/', verbose_name='Document')),
                ('pro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project', verbose_name='Project Name')),
            ],
        ),
    ]
