# Generated by Django 2.2.5 on 2019-09-14 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_workbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('workbook', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snippets.Workbook', verbose_name='workbook')),
            ],
            options={
                'verbose_name': 'Folder',
                'verbose_name_plural': 'Folders',
                'db_table': 'snippets_folders',
                'ordering': ['name'],
            },
        ),
    ]
