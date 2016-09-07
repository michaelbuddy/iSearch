#encoding=utf-8
from django.db import models
from django.contrib import admin 

class Blog(models.Model):  
    Title=models.CharField(u'标题',max_length=200,blank=True)  
    Content=models.TextField(u'内容',blank=True)  
    def __unicode__(self):  
        return self.Title  
class Meta:
    verbose_name=u"Blog"
admin.site.register(Blog)