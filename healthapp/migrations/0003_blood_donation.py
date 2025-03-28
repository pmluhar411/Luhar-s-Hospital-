from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_auto_20220222_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('purpose', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='healthapp.patient')),
            ],
        ),
    ]
