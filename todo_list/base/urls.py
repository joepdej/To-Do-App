from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, TodoLogin, TodoRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', TodoRegister.as_view(), name="register"),
    path('login/', TodoLogin.as_view(), name="login"),
    path('', TodoList.as_view(), name="todo-list"),
    path('taak/<int:pk>/', TodoDetail.as_view(), name="taak"),
    path('maak-taak/', TodoCreate.as_view(), name="maak-taak"),
    path('update-taak/<int:pk>/', TodoUpdate.as_view(), name="update-taak"),
    path('delete-taak/<int:pk>/', TodoDelete.as_view(), name="delete-taak"),

]
