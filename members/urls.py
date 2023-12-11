from django.urls import path
from . import views
from .views import UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path(r'^login/$', views.login_page, name='login'),
    path('mycomments/', views.CommentListView, name='comments'),
    path('myprofile/', views.UserEditView, name='edit_profile'),
    path('myprofile/change_password/', views.UserChangePasswordView, name='edit_security'),
    path('myprofile/security/', views.UserChangePageView, name='edit_security_page'),
    path('myprofile/change_email/', views.UserChangeEmailView, name='edit_email'),
    path('myprofile/notifications/', views.user_notification_view, name='notifications'),
    path('myprofile/author/', views.UserAuthorView, name='edit_author'),

    path('myprofile/posts/', views.my_posts, name='my_posts'),
    path('myprofile/posts/create/', views.my_posts_create, name='my_posts_create'),
    path('myprofile/posts/detail/<int:pk>', views.my_posts_detail, name='my_posts_detail'),
    path('myprofile/posts/edit/<int:pk>', views.my_posts_edit, name='my_posts_edit'),
    path('myprofile/posts/delete/<int:pk>', views.my_posts_delete, name='my_posts_delete'),

    path('myprofile/author_application/', views.article_author_form, name='article_author_form'),
    path('myprofile/author_application/history/', views.article_author_history, name='article_author_history'),
    path('myprofile/author_application/detail/<int:pk>', views.article_author_detail, name='article_author_detail'),
    path('myprofile/author/create/', views.create_author, name='create_author'),

    path('confirmation/', views.confirmation_page, name='confirmation'),
    path('confirm/<str:uidb64>/<str:token>/', views.confirm_email, name='confirm_email'),
    path('confirmed/', views.registration_confirmed, name='registration_confirmed'),
    path('confirmation-error/', views.confirmation_error, name='confirmation_error'),

    path('reset_password/', views.CustomPasswordResetView.as_view(
        template_name='Registration/ResetPassword/PasswordResetForm.html',
        html_email_template_name='registration/ResetPassword/PasswordResetEmail.html',
        subject_template_name='registration/ResetPassword/PasswordResetSubject.txt',
    ), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='Registration/ResetPassword/PasswordResetDone.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='Registration/PasswordResetConfirm.html'
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='Registration/ResetPassword/PasswordResetComplete.html'
    ), name='password_reset_complete'),

]
