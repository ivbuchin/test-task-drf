from rest_framework import serializers

from .models import Permission, Employee, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    
    class Meta:
        model = Permission
        fields = '__all__'

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        permission = Permission.objects.create(**validated_data)

        for section_data in sections_data:
            section, created = Section.objects.get_or_create(**section_data)
            permission.sections.add(section)

        return permission


class AdminEmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = Employee
        fields = ['username', 'password']


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'permission', 'username', 'password']
    
    def create(self, validated_data):
        employee = Employee.objects.create_user(**validated_data)
        return employee
