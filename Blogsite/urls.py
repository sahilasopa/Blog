from django.urls import path
from . import views
from django.contrib.auth import views as passreset
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('profile/<str:pk>/', views.profile, name='profile'),
                  path('about/', views.about, name='about'),
                  path('contact/', views.contact, name='contact'),
                  path('new/post', views.new_post, name="new-post"),
                  path('blog/edit/<str:pk>/', views.edit, name='edit'),
                  path('my/blogs/', views.my_blogs, name='my_blog'),
                  path('post/<str:pk>/', views.post, name="post"),
                  path('login/', views.login, name='login'),
                  path('logout/', views.logout, name='logout'),
                  path('delete/<str:pk>', views.delete, name='delete'),
                  path('register/', views.signup, name='register'),
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
