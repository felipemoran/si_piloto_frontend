from django.conf.urls import patterns, include, url
from django.contrib import admin

from sistema import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^curtir_post/$', views.curtir_post, name='curtir_post'),
    url(r'^ver_post/(?P<post_id>\d+)', views.ver_post, name='ver_post'),

    url(r'^comentar_post/$', views.comentar_post, name='comentar_post'),
    url(r'^apagar_comentario/(?P<comm_id>\d+)', views.apagar_comentario, name='apagar_comentario'),

    url(r'^cadastrar/$', views.cadastrar, name='cadastrar'),


    url(r'^admin/', include(admin.site.urls)),
)
