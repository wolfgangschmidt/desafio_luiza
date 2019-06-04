from rest_framework import serializers
from cadastro.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Funcionario
		fields = ['pk', 'name', 'email', 'dept']