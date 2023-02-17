from django.db import models

# Create your models here.

from django.db import models

class Musicdata(models.Model):
    singer = models.CharField("歌手名", max_length=255)
    id = models.IntegerField("排名", primary_key=True)
    name= models.CharField("歌曲名", max_length=255)
    s_time = models.CharField("时长", max_length=255)

    class Meta:
        verbose_name = "歌曲信息"
        verbose_name_plural = "歌曲信息"



class Comment(models.Model):
    comment = models.CharField("评论内容", max_length=255)
    username = models.CharField("用户名", max_length=255)
    c_time = models.CharField("评论时间", max_length=255)
    id = models.ForeignKey(to=Musicdata,unique=True,
                           on_delete=models.CASCADE, primary_key=True)
    class Meta:
        verbose_name = "评论信息"
        verbose_name_plural = "评论信息"
