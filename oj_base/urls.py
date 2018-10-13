from django.urls import path
from . import views

app_name = 'oj_base'
urlpatterns = [
    path('', views.index,name='主页'),
    path('index/', views.index, name='主页'),
    path('about/', views.about, name='关于'),
    # path('edit/<每一件事_id>', views.edit, name='编辑'),
    # path('del/<每一件事_id>', views.delete, name='删除'),
    # path('cross/<每一件事_id>', views.cross, name='划掉')
]
