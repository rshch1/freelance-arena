from rest_framework.routers import DefaultRouter 
from . import views
from django.urls import path, include
from rest_framework_jwt import views as views_jwt
router = DefaultRouter()
router.register('executors', views.ExecutorViewSet, 'executors' )
router.register('customers', views.CustomerViewSet, 'customers' )
router.register('tasks', views.TaskViewSet, 'tasks' )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/login', views_jwt.obtain_jwt_token),
    path('auth/register', views.RegisterUsersView.as_view()),
]
