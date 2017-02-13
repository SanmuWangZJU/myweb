from django.db import models

# Create your models here.(Use ORM to operate SQL)
class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.title # 在admin中数据库显示内容标题，若不重写__str__函数，就会显示‘Article’
