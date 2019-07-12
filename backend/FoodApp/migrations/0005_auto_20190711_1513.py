# Generated by Django 2.2 on 2019-07-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0004_remove_organisation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='user_details',
        ),
        migrations.AddField(
            model_name='organisation',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]