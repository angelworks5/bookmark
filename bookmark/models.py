from django.db import models
from django.urls import reverse


# Create your models here.
# 모델 =  테이블 //엑셀 시트
# 모델의 필드 = 테이블의 컬럼 //엑셀 열
# 인스턴스 = 테이블 레코드 //엑셀 행
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # python manage.py makemigrations bookmark
    # python manage.py migrate bookmark 0001

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소: " + self.url

    #수정 후 링크 수정
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
