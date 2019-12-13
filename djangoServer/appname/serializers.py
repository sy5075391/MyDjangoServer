from rest_framework import serializers
from appname.models import Person


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'time')
