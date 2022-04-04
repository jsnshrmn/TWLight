# Generated by Django 3.2.12 on 2022-03-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0082_partner_searchable"),
    ]

    operations = [
        migrations.AddField(
            model_name="suggestion",
            name="ticket_number",
            field=models.CharField(
                blank=True,
                default="",
                help_text="phabricator ticket id where we track progress of request",
                max_length=10,
            ),
        ),
    ]