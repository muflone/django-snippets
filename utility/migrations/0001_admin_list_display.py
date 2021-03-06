# Generated by Django 2.2.5 on 2019-09-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminListDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminListDisplayLinkAdmin', 'AdminListDisplayLinkAdmin'), ('AdminListFilterAdmin', 'AdminListFilterAdmin'), ('FolderAdmin', 'FolderAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('SnippetAdmin', 'SnippetAdmin'), ('WorkbookAdmin', 'WorkbookAdmin')], max_length=255, verbose_name='model')),
                ('field', models.CharField(max_length=255, verbose_name='field')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'Admin List Display',
                'verbose_name_plural': 'Admin List Display',
                'db_table': 'utility_admin_list_display',
                'ordering': ['model', 'order', 'field'],
                'unique_together': {('model', 'order'), ('model', 'field')},
            },
        ),
    ]
