from rest_framework import  serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name', 'last_name','username','password','credit')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        customer = Customer.objects.create_user(validated_data['username'] ,password = validated_data['password'] ,
                                                first_name=validated_data['first_name'] ,last_name=validated_data['last_name'] ,
                                                credit=validated_data['credit'])
        return customer

class IncreaseCreditCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('credit',)