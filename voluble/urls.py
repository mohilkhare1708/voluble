from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import mainapp.views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'), name='login-page'),
    path('register/', main_views.register_page, name='register-page'),
    path('choice/', main_views.choice_page, name='choice-page'),
    path('choice/add_word', main_views.add_word_page, name='add-word-page'),
    path('choice/revise', main_views.revise_page, name='revise-page'),
]
