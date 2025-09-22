from rest_framework import serializers
from escola.models import Estudante,Curso, Matricula
from escola.validators import nome_invalido, cpf_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

    def validate(self, dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'Seu nome só pode conter letras'}) 
        if cpf_invalido(dados['cpf']):
           raise serializers.ValidationError({'cpf':'O cpf deve ser um valor válido!'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'Seu celular deve seguir esse modelo XX 9XXXX-XXXX respeite os espaços e os traços'})
        return dados
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
        
class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']
    def validate(self, dados):
            if celular_invalido(dados['celular']):
                raise serializers.ValidationError({'celular':'Seu celular deve seguir esse modelo XX 9XXXX-XXXX respeite os espaços e os traços'})
            return dados