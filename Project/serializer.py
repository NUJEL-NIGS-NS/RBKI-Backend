from rest_framework import serializers
from .models import Project,Update_project

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Project
        fields ='__all__'

class ProjectDisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Project
        fields =['id',"as_no","pro_name","district","length_km",'pro_cat','stage','phy_pro','fin_pro']

class UpdateProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Update_project
        fields = '__all__'

class UpdateDisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Update_project
        fields =['id',"as_no","pro_name","district","length_km",'pro_cat','stage','phy_pro','fin_pro']        