from django.urls import path
from .views import (
    CourseView,
    # my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    # path('', my_fbv, name='courses-list'),
    

    # path('create/', <create_view>, name='courses-create'),
    # path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update/', <update_view>, name='courses-update'),
    # path('<int:id>/delete/', <delete_view>, name='courses-delete'),
]