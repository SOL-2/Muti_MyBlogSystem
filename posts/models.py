from django.db import models

class Post(models.Model):
    author = models.CharField("작성자",max_length=20)
    contents = models.TextField('글 내용', max_length=1000)

    def __str__(self):
        return self.contents

    # author는 입력 란이 한 줄 필요. max_length는 필수
    # contents는 여러 줄을 입력할 수 있는 란이 필요함
    # models를 기반으로 입력란을 자동으로 생성함


