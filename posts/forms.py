from django import forms
from posts.models import Post,Comment
# 모델폼을 작성하려면 이전에 작성한 모델에서 불러와야 함
# 사용하는 모델에 form을 붙여 클래스명 정함

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 해당 클래스를 기반으로 모델을 만들겠다는 뜻
        fields =['author', 'title', 'contents']
        # 필드에 어떤식으로 넣을지에 따라 입력칸이 정해짐



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
