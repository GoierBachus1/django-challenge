from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .api import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("tasks/",views.task_list, name = "task_list"),
    path("tasks/new/", views.task_create, name = "task_create"),
    path("tasks/<int:pk>/",views.task_detail, name = "task_detail"),
    path("tasks/<int:pk>/edit/",views.task_update, name= "task_update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name = "task_delete"),

    path("api/", include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]