# Generated by Django 2.2.5 on 2019-09-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together={('workbook', 'name')},
        ),
    ]
