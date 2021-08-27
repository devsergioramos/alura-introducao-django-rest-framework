from rest_framework import viewsets
from escola.models import Student, Course, Registry
from escola.serializer import StudentSerializer, CourseSerializer, RegistrySerializer

# Com essas linhas ja conseguimos manipular o CRUD com base no nosso model serializado
# ViewSet é uma forma de declarar os CRUD usando as convenções de uma REST API, sem a necessidade de criar suas lógicas
class StudentsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistryViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer