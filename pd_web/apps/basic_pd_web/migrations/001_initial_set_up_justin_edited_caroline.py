# Generated by Django 3.0.3 on 2020-02-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_start', models.PositiveIntegerField(default=0)),
                ('year_end', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connected', models.BooleanField()),
                ('pending', models.BooleanField()),
                ('contacted', models.BooleanField()),
                ('future', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tb_event', models.CharField(max_length=45)),
                ('rsvp', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('umbrella', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.PositiveIntegerField(default=0)),
                ('tuesday', models.PositiveIntegerField(default=0)),
                ('wednesday', models.PositiveIntegerField(default=0)),
                ('thursday', models.PositiveIntegerField(default=0)),
                ('friday', models.PositiveIntegerField(default=0)),
                ('saturday', models.PositiveIntegerField(default=0)),
                ('sunday', models.PositiveIntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('year', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('phone_number', models.PositiveIntegerField(default=0)),
                ('in_rcsa', models.BooleanField(default=False)),
                ('authentication_level', models.PositiveIntegerField(default=0)),
                ('committee', models.ManyToManyField(related_name='users_committees', to='basic_pd_web.Committee')),
            ],
        ),
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField(default=0)),
                ('month', models.PositiveIntegerField(default=0)),
                ('month_word', models.CharField(max_length=45)),
                ('year', models.PositiveIntegerField(default=0)),
                ('hour', models.PositiveIntegerField(default=0)),
                ('minute', models.PositiveIntegerField(default=0)),
                ('second', models.PositiveIntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('repeats', models.ManyToManyField(related_name='datetime_repeats', to='basic_pd_web.Repeat')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=45)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('company_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_status', to='basic_pd_web.CompanyStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('archive', models.SmallIntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_user', to='basic_pd_web.User')),
            ],
        ),
    ]
