from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone

class Post(models.Model):   # PostはDjango Modelであることを示す
    # プロパティを定義
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 他のモデルへのリンク
    title = models.CharField(max_length=200)    # 文字数制限ありのテキストを定義するフィールド
    text = models.TextField()                   # 文字数制限なし　　　　　〃
    create_date = models.DateTimeField(default=timezone.now)    # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title