
from django.db import models

class Photo(models.Model):
    
    # 文件字段    
    zip_file = models.FileField(help_text=('Zip-file'))
    
    title = models.CharField(
        ('title'),
        max_length=250,
        help_text=('All uploaded photos will be given a title made up of this title + a '
                                        'sequential number.<br>This field is required if creating a new '
                                        'gallery, but is optional when adding to an existing gallery - if '
                                        'not supplied, the photo titles will be creating from the existing '
                                        'gallery name.'))

    # 说白了，就是用标题作为url的一部分访问网页。 参考：Django 为slug字段添加中文化支持 https://www.jianshu.com/p/7fe8037ed6be
    slug = models.SlugField(
        ('slug'),
        unique=True,
        max_length=250,
        help_text=('A "slug" is a unique URL-friendly title for an object.')) # “slug”也是对象唯一的URL友好标题。 
    

