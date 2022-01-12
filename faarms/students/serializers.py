from rest_framework import routers, serializers, viewsets
from .models import Studentsinfo
from .models import StudentAcademics

# Serializers define the API representation.
class StudentsinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentsinfo
        fields = '__all__'

class StudentAcademicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAcademics
        fields = '__all__'
       