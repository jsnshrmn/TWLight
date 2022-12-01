# Generated by Django 3.2.15 on 2022-10-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0083_suggestion_ticket_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhabricatorTask",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "task_type",
                    models.IntegerField(
                        choices=[
                            (0, "Service information"),
                            (1, "Service issue"),
                            (2, "Temporarily unavailable"),
                        ],
                        default=0,
                        help_text="Will linking this task inform them of ongoing changes, warn them of issues impacting some users, or indicate an outage?",
                    ),
                ),
                (
                    "phabricator_task",
                    models.CharField(
                        help_text="Phabricator Task ID, eg. T314780", max_length=255
                    ),
                ),
                (
                    "partners",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The partner(s) affected by this task.",
                        to="resources.Partner",
                    ),
                ),
            ],
            options={
                "verbose_name": "Phabricator Task",
                "verbose_name_plural": "Phabricator Tasks",
            },
        ),
    ]