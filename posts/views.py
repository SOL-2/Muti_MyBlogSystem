from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,reverse
from posts.models import Post,Comment
from posts.forms import PostForm, CommentForm



def p_list(request):
    my_list = Post.objects.all().order_by('-posted_date')
    context = {'posts': my_list}
    return render(request, 'list.html', context)






def p_create(request):
    # POST 방식으로 호출될 때
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        # 사용자가 입력한 데이터가 다 들어있음
        if post_form.is_valid(): # 입력한 데이터에 문제가 없다면
            post_form.save() # 포스트 폼에 저장한다
            return redirect('posts:list')
            # 네임스페이스가 posts이고 urlpattern에서 name이 list인
            # url로 리다이렉션



    # GET 방식으로 호출될 때(폼으로 요청하는게 아니면 다 GET 방식으로 요청하는 것)
    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})


def p_delete(request, post_id):
    post = Post.objects.get(id=post_id) # id가 인자로 넘어온 id와 일치한 객체만 post에 넘겨줌
    post.delete()

    return redirect('posts:list')


def p_update(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        # 사용자가 입력한 데이터가 다 들어있음.
        # instance = post 에 pk(id)도 들어있음.
        # 때문에 아래 save()에서 새로 저장하는 것이 아니라 수정이 되는 것

        if post_form.is_valid(): # 입력한 데이터에 문제가 없다면
            post_form.save() # 포스트 폼에 저장한다
            return redirect('posts:list')
            # 네임스페이스가 posts이고 urlpattern에서 name이 list인
            # url로 리다이렉션



    # GET 방식으로 호출될 때(폼으로 요청하는게 아니면 다 GET 방식으로 요청하는 것)
    else:
        post_form = PostForm(instance=post)
        # 수정 시 빈 칸이 아니라 instance에 post 데이터를 가져오는 칸을 만들어줌

    return render(request, 'create.html', {'post_form': post_form})




def p_detail(request, post_id):
    print("디테일함수 들어옴 ")
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        print("디테일 포스트로 들어옴 ")
        # 사용자가 입력한 데이터가 다 들어있음.
        # instance = post 에 pk(id)도 들어있음.
        # 때문에 아래 save()에서 새로 저장하는 것이 아니라 수정이 되는 것

        # if post_form.is_valid(): # 입력한 데이터에 문제가 없다면
        #     post_form.save() # 포스트 폼에 저장한다
        #     return redirect('posts:list')
            # 네임스페이스가 posts이고 urlpattern에서 name이 list인
            # url로 리다이렉션

    else:
        post_form = PostForm(instance=post)
        for i in post_form.fields: # 수정이 되지 않도록 처리
            post_form.fields[i].disabled = True
        comment_form = CommentForm()
        print("디테일 엘스 들어옴 ")


    return render(request, 'detail.html', {'post_form': post_form, 'post': post, 'comment_form':comment_form})


def p_comment(request, post_id):
    print("pComment 들어왔다")
    post = get_object_or_404(Post, pk=post_id)
    # comment = get_object_or_404(Post, pk=comment_post)

    if request.method == "POST":
        print("post 들어왔다 ")
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print("valid 들어왔다 ")
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            print("comment pk: {}".format(comment.pk))
            return redirect('posts:detail', post_id=post_id)
    else:
        form = CommentForm(request.GET)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:detail', post_id=post_id)

    print("pComment 그린다 ")
    return redirect('posts:detail', post_id=post_id)#render(request, 'detail.html', {'post_form': post_form, 'post': post, 'comment_form':comment_form})



def c_delete(request, post_id,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id) # id가 인자로 넘어온 id와 일치한 객체만 post에 넘겨줌
    comment.delete()

    return redirect('posts:detail',post_id=post_id)



# def p_send_comment(request, comment_post):
#     print("댓글아 쌓여")
#     comment = get_object_or_404(Post, comment_post)
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST, instance=Post)
#         if comment_form.is_valid():
#             print('댓글아 쌓여2')
#             comment = comment_form.save(commit=False)
#             comment.post = comment
#             comment.save()
#             return HttpResponseRedirect(reverse('posts:detail', args=(comment.post,)))
#
#
