
from django.urls import path
from .views import user_login, index, register, edit
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('', index, name='index'),

    path('login/', user_login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done_form.html'), name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset' ),
    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
    path('user_register/', register, name='user_registration'),

    path('edit/', edit, name='edit'),

] 
