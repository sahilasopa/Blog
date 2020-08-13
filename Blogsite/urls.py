from django.urls import path
from . import views
from django.contrib.auth import views as passreset
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('new/post', views.new_post),
    path('blog/edit/<str:pk>/', views.edit, name='edit'),
    path('my/blogs/', views.my_blogs, name='my_blog'),
    path('post/<str:pk>/', views.post),
    path('login/', views.login),
    path('logout/', views.logout),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('register/', views.signup),
    path('reset_password/',
         passreset.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         passreset.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         passreset.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         passreset.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
