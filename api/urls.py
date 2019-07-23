from rest_framework.routers import DefaultRouter 
from .views import ExecutorViewSet, CustomerViewSet, TaskViewSet, RegisterUsersView
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register('executors', ExecutorViewSet, 'executors' )
router.register('customers', CustomerViewSet, 'customers' )
router.register('tasks', TaskViewSet, 'tasks' )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/login', obtain_jwt_token),
    path('auth/register', RegisterUsersView.as_view(), name='registration'),
]
