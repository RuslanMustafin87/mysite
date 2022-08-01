from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^clients/$', views.ClientListView.as_view(), name='clients'),
    re_path(r'^architectors/$', views.ArchitectorListView.as_view(), name='architectors'),
    re_path(r'^client/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client-detail'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

]

# urlpatterns += [
#     re_path(r'^book/newbook/$', views.new_book, name='new-book'),
#     ]

urlpatterns += [
    re_path(r'^book/create/$', views.BookCreateView.as_view(), name='book-create'),
    re_path(r'^book/(?P<pk>\d+)/update/$', views.BookUpdateView.as_view(), name='book-update'),
    re_path(r'^book/(?P<pk>\d+)/delete/$', views.BookDeleteView.as_view(), name='book-delete'),
]