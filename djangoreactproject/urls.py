
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
from todo import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/todos/$', views.todo_list),
    re_path(r'^auth/me/$', views.info_user),
    
    re_path('^api/admin/todos/$', views.all_todo_list),
    re_path('^api/admin/users/$', views.all_users_list),
    
    re_path(r'^api/users/$', views.users_list),
	re_path(r'^api/todos/(?P<pk>[0-9]+)$', views.todos_list),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    
    # path('password-reset/<str:encoded_pk>/<str:token>/'name="jhkjhjk")
 
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
