# Generated by Django 3.1.4 on 2020-12-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0012_auto_20201207_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='index_schedule',
            field=models.IntegerField(choices=[(3600, 'Every hour'), (7200, 'Every 2 hours'), (10800, 'Every 3 hours'), (14400, 'Every 4 hours'), (18000, 'Every 5 hours'), (21600, 'Every 6 hours'), (43200, 'Every 12 hours'), (86400, 'Every 24 hours')], db_index=True, default=21600, help_text='Schedule of how often to index the source for new media', verbose_name='index schedule'),
        ),
    ]
