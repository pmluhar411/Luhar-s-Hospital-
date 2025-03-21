from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralHealthProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='search_data',
            name='predict_for',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
