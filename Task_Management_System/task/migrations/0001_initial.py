# Generated by Django 5.0.4 on 2024-06-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=30)),
                ('task_discription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('task_Assign_Date', models.DateField()),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
