# Generated by Django 5.1.2 on 2024-10-31 02:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_answer_modify_date_question_modify_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='voter',
            field=models.ManyToManyField(related_name='voter_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_answer', to='article.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
