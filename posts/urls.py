from django.conf.urls import url

# from contact import views as contact_view
# from posts import views as post_view

from . import views

urlpatterns = [
    url(r'create/^$', "posts.views.post_create"),
    url(r'detail/^$', "posts.views.post_detail"),
    # Home page for posts
    url(r'^$', "posts.views.post_list"),
    url(r'update/^$', "posts.views.post_update"),
    url(r'delete/^$', "posts.views.post_delete"),
    # url(r'^admin/', "<appname>.<module>.<function>"),
    # url(r'^posts/', post_view.post_home),
]