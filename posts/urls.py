
from django.urls import path
from . import views

app_name = 'posts'



urlpatterns = [
    path('list/', views.p_list, name='list'),
    path('create/', views.p_create, name='create'),
    path('<int:post_id>/delete/', views.p_delete, name='delete'),
    path('<int:post_id>/update/', views.p_update, name='update'),
    path('<int:post_id>/detail/', views.p_detail, name='detail'),
    path('<int:post_id>/comment/', views.p_comment, name='comment'),
]
