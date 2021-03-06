# Generated by Django 3.2.5 on 2021-08-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBNコード')),
                ('title', models.CharField(max_length=100, verbose_name='著名')),
                ('price', models.IntegerField(default=0, verbose_name='出版社')),
                ('publisher', models.CharField(choices=[('照英社', '照英社'), ('技術評論社', '技術評論社'), ('照英社', '照英社'), ('技術評論社', '技術評論社'), ('技術評論社', '技術評論社')], max_length=50, verbose_name='出版社')),
                ('published', models.DateField(verbose_name='刊行日')),
            ],
        ),
    ]
