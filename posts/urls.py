from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.new_post, name='new_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post')
]
