# Generated by Django 2.0.7 on 2019-10-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nanotask', '0007_ticket_instance_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mturk_worker_id', models.CharField(blank=True, max_length=255, null=True)),
                ('is_qualified', models.IntegerField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='nanotask',
            name='ground_truth',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]