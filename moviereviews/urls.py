from django.contrib import admin
from django.urls import path, include
from movie import views as movieViews  # Importando las vistas de movie

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', movieViews.home, name='home'),  # Página de inicio desde movie
    path('admin/', admin.site.urls),
    path('about/', movieViews.about),  # Nueva ruta para la página about
    path('news/', include('news.urls')),  # Ruta para la app news
    path('statistics/', movieViews.statistics_view, name='statistics'),  # Nueva ruta para la página statistics
    path('signup/', movieViews.signup, name='signup'),  # Nueva ruta para la página singup
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)