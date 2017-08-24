from django.conf.urls import url

# from contact import views as contact_view
# from posts import views as post_view

# from . import views
from .views import(
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete

	)

# urlpatterns = [
#     url(r'create/^$', "posts.views.post_create"),
#     url(r'detail/^$', "posts.views.post_detail"),
#     # Home page for posts
#     url(r'^$', "posts.views.post_list"),
#     url(r'update/^$', "posts.views.post_update"),
#     url(r'delete/^$', "posts.views.post_delete"),
#     # url(r'^admin/', "<appname>.<module>.<function>"),
#     # url(r'^posts/', post_view.post_home),
# ]

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^delete/$', post_delete),
]
