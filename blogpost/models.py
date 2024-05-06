from django.db import models

CATEGORY = (('business','ビジネス'),('life','生活'),('other','その他'))

class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

# ↓↓modelsモジュールの中にあるModelクラスを継承している↓↓
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )

    #↓↓オブジェクトの文字列表現を返すという役割を持つ「特殊メソッド」↓↓
    def __str__(self):
        return self.title