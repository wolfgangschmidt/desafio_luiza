from django.conf.urls import url
from .views import FuncionarioCrudApiView

urlpatterns = [
	url(r'(?P<pk>\d+)$', FuncionarioCrudApiView.as_view(), name='post_crud')
]