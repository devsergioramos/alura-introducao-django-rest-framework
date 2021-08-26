from rest_framework import serializers
from escola.models import Student, Course

# transforma o model alunos em modelos serializados
# convert os dados para dados serializados para que o ORM do python possa entender
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' # traz todos os fields