from rest_framework import serializers
from appname.models import Person
from appname.models import Users


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'time')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password', 'time')
