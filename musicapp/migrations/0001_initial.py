# Generated by Django 2.2 on 2021-05-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicdata',
            fields=[
                ('singer', models.CharField(max_length=255, verbose_name='歌手名')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='排名')),
                ('name', models.CharField(max_length=255, verbose_name='歌曲名')),
                ('s_time', models.CharField(max_length=255, verbose_name='时长')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment', models.CharField(max_length=255, verbose_name='评论内容')),
                ('username', models.CharField(max_length=255, verbose_name='用户名')),
                ('c_time', models.CharField(max_length=255, verbose_name='评论时间')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='musicapp.Musicdata')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
    ]