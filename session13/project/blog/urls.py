from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns =[
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>/', views.detail,	name="detail"),
    path('edit/<int:post_pk>/', views.edit,	name="edit"),
    path('delete/<int:post_pk>/', views.delete,	name="delete"),
    path('delete-comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path("registration/signup/", views.signup, name="signup"),
    path("registration/login/", views.login, name="login"),
    path("registration/logout/", views.logout, name="logout"),
]
