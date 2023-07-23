from django.urls import path, include
from . import views 

app_name = 'portfolio'
urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('', views.index_page_view, name='preloader'),
    path('activities', views.activities_page_view, name='activities'),
    path('parallax', views.parallax_page_view, name='parallax'),
    path('index', views.index, name='index'),
    path('escola', views.escola_page_view, name='escola'),
    path('academia', views.academia_page_view, name='academia'),
    path('web', views.web_page_view, name='web'),
    path('news', views.noticias, name='news'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('nova/', views.nova_page_view, name='nova'),
    path('blogueira', views.blogueira_page_view, name='blogueira'),
    path('edita/<int:tarefa_id>', views.edita_page_view, name='edita'),
    path('apaga/<int:tarefa_id>', views.apaga_page_view, name='apaga'),
    path('publication', views.publication, name='publication'),
    path('novoPost/', views.novo_post_page_view, name='novopost'),
    path('editPost/<int:post_id>', views.edit_post_page_view, name='editPost'),
    path('apagaPost/<int:post_id>', views.apaga_post_page_view, name='apagaPost'),
    path('like_post/<int:post_id>/', views.blog_like_post, name='like_post'),
    path('comentario', views.comentario, name='comentario'),
    path('search/', views.search_posts, name='search_posts'),
    path('editCourse/<int:course_id>', views.edit_course_page_view, name='editCourse'),
    path('apagaCourse/<int:course_id>', views.apaga_course_page_view, name='apagaCourse'),
]

