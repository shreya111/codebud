# Generated by Django 4.0.4 on 2022-05-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_testcases_problem_test_input_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='verdict',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('COMPILATION_ERROR', 'Compilation Error'), ('Wrong Output', 'Wrong Output'), ('TIME LIMIT EXCEEDED', 'Time Limit Exceeded'), ('RUNTIME ERROR', 'Runtime Error')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
