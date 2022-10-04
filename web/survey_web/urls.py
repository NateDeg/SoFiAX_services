from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.views.generic.base import RedirectView
from django.conf import settings

from survey.views import detection_products, instance_products, \
    run_products, run_catalog, \
    logout_view, test

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.INDEX_TITLE

admin.autodiscover()

urlpatterns = [
    path('test', test, name='test'),
    path('detection_products', detection_products, name='detection_products'),
    path('instance_products', instance_products, name='instance_products'),
    path('run_products', run_products, name='run_products'),
    path('catalog', run_catalog, name='run_catalog'),
    # path('admin/login/', RedirectView.as_view(url=settings.LOGIN_URL, permanent=True, query_string=True)),
    # path('admin/logout/', logout_view, name="logout_view"),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace="social")),
]

admin.site.enable_nav_sidebar = False
