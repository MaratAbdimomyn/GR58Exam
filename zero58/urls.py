from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('about_category/<int:pk>/', AboutCategoryView.as_view(), name='about_category'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('', ToDoView.as_view(), name='home'),
    path('about_todo/<int:pk>/', ToDoDetailView.as_view(), name='about_todo'),
    path('create_todo/', ToDoCreateView.as_view(), name='create_todo'),
    path('delete_todo/<int:pk>/', ToDoDeleteView.as_view(), name='delete_todo'),
    path('update/<int:pk>/', update, name='update'),
]