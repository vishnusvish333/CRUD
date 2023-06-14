from django.urls import  path

from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('index',views.add,name="add"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    
   
]
