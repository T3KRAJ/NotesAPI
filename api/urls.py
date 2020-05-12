from django.urls import path
from .views import GenericAPIView, apioverview

urlpatterns = [
    path('', apioverview, name='main-view'),
    path('api-view/<int:id>/', GenericAPIView.as_view())

    #for function based views
#     path('task-list/', views.taskList, name='task-list'),
#     path('task-create/', views.taskCreate, name='task-create'),
#     path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
#     path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
#     path('task-delete/<str:pk>/', views.taskDelete, name='task-delete')
]
