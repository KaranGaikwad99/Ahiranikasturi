"""marathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""



from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from posts import views




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name='marathi/index.html')),
    url(r'^$', views.HomePageView, name='home'),
    url(r'^blog/$', views.post_home, name='post_home'),
    url(r'^blog_detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^gallery/$', views.gallery_home, name='gallery_home'),
    url(r'^gallery_detail/(?P<id>\d+)/$', views.gallery_detail, name='gallery_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^program/$', views.program, name='program'),
    url(r'^program_detail/(?P<id>\d+)/$', views.program_detail, name='program_detail'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^registration/$', views.registration, name='registration'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













