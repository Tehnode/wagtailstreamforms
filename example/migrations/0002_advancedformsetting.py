# Generated by Django 2.0.5 on 2018-06-15 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailstreamforms', '0001_initial'),
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedFormSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_address', models.EmailField(max_length=254)),
                ('form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advanced_settings', to='wagtailstreamforms.Form')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
