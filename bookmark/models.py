from django.db import models

# Create your models here.

class Bookmark(models.Model):
    # 하나의 필드를 만든다.
    # 칼럼 이름 = 칼럼 종류(제약조건)
    site_name = models.CharField(max_length = 100)
    url = models.URLField('url')

    # 모델의 옵션
    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        from django.urls import reverse
        # http://localhost:8000/bookmark/detail/4
        return reverse('bookmark:detail', args=[str(self.id)])