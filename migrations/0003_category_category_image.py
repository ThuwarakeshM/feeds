# Generated by Django 2.1.1 on 2018-09-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20180910_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.CharField(default='https://image.vikatan.com/news/2018/09/images/1088X550/136533_thumb.jpg', max_length=300),
            preserve_default=False,
        ),
    ]