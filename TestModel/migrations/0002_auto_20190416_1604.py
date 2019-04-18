# Generated by Django 2.1.7 on 2019-04-16 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章标题')),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog_img', verbose_name='博客配图')),
                ('body', models.TextField(verbose_name='正文')),
                ('abstract', models.TextField(blank=True, max_length=256, null=True, verbose_name='摘要')),
                ('visiting', models.PositiveIntegerField(default=0, verbose_name='访问量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modifyed_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '博客正文',
                'verbose_name_plural': '博客正文',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('comment', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='标签')),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': '博客分类', 'verbose_name_plural': '博客分类'},
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=128, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ManyToManyField(to='TestModel.Test', verbose_name='博客分类'),
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='TestModel.Tag', verbose_name='标签'),
        ),
    ]
