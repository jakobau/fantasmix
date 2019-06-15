# django_project URLs.

from django.contrib import admin
# from django.urls import path
from votings import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/about/$', views.about, name='about'),
    url(r'^home/generate/$', views.generate, name='generate'),
    url(r'^home/generateMagenta/$', views.generateMagenta, name='generatemMgenta'),
    url(r'^signin/$', views.signIn, name='signIn'),
    url(r'^login/$', views.login, name='login'),
    url(r'^postsign/$', views.postsign, name='postsign'),
    url(r'admin/', admin.site.urls),
    url(r'^home/generateMusic/$', views.generateMusic, name='generateMusic'),
    url(r'^home/generateMusicMagenta/$', views.generateMusicMagenta, name='generateMusicMagenta'),
    url(r'^home/generateMusicTest/$', views.getSettings, name='getSettings'),
]
