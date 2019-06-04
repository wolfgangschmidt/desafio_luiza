from django.conf.urls import url
from .views import FuncionarioCrudApiView, FuncionarioApiView

urlpatterns = [
	url(r'^$', FuncionarioApiView.as_view(), name='post_create'),
	url(r'(?P<pk>\d+)$', FuncionarioCrudApiView.as_view(), name='post_crud'),
]