from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views
from .views import *

urlpatterns = [

    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^products/$', views.products, name = 'products'),
    url(r'^product/$', ProductListView.as_view(), name='product_list'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'post_url/', views.post_product, name='post_product'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
    url(r'^like_product/$', views.like_product, name='like_product' ),

    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='product-edit'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='product-delete'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^product/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
