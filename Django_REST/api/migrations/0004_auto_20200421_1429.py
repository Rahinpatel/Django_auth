# Generated by Django 2.2.12 on 2020-04-21 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200414_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='to_who',
        ),
        migrations.RemoveField(
            model_name='borrowed',
            name='what',
        ),
        migrations.DeleteModel(
            name='Belonging',
        ),
        migrations.DeleteModel(
            name='Borrowed',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
