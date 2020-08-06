from django.db import models
from django.utils import timezone
now = timezone.localtime()

class Post(models.Model):
    title = models.CharField("제목", max_length=30)
    author = models.CharField("작성자", max_length=20)
    contents = models.TextField('글 내용', max_length=1000)
    posted_date = models.DateTimeField('게시일', auto_now=True)

    def __str__(self):
        return self.contents

    # author는 입력 란이 한 줄 필요. max_length는 필수
    # contents는 여러 줄을 입력할 수 있는 란이 필요함
    # models를 기반으로 입력란을 자동으로 생성함


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text