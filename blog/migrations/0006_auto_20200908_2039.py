# Generated by Django 3.1 on 2020-09-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200908_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('Design', 'Design'), ('interface', 'interface'), ('shop', 'shop'), ('suggestion', 'suggestion')], default='', max_length=50),
        ),
    ]
