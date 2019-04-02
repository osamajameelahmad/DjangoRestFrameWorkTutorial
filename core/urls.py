from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from core import views as core_views
#
# urlpatterns = [
#     url(r'^$', core_views.home, name='home'),
#
#     url(r'^manage_groups/$', core_views.manage_groups, name='manage_groups'),
#     url(r'^manage_users/$', core_views.manage_users, name='manage_users'),
#     url(r'^delete_user/$', core_views.delete_user, name='delete_user'),
#     url(r'^password/$', core_views.change_password, name='change_password'),
#     url(r'^forgot_password/$', core_views.forgot_password, name='forgot_password'),
#     url(r'^edit_user_access_to_group/$', core_views.edit_user_access_to_group, name='edit_user_access_to_group'),
#     url(r'^add_group/$', core_views.add_group, name='add_group'),
#     url(r'remove_group/(?P<group_id>.+)/$', core_views.remove_group, name="remove_group"),
#     url(r'download_certificate_file/(?P<user_id>.+)/', core_views.download_certificate_file,
#         name="download_certificate_file"),
#
#     url(r'^login/$', core_views.login, name='login'),
#     url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
#     url(r'^signup/$', core_views.signup, name='signup'),
# ]

from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'customusers', views.CustomUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^home/$', core_views.home, name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
