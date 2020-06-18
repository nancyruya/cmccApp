from django.conf.urls import url
from django.contrib import admin
import cmccDemos.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cmccDemos.views.homepage, name ='home'),
    path('blog/', cmccDemos.views.blog, name='blog'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
