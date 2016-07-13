from rest_framework import viewsets
from serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def add_user(data):
    message = dict()
    try:
        user = User.objects.get(email=data['email'])
        message['message'] = u"FAIL"
        message['id'] = user.id
        message['redirect'] = True
    except User.DoesNotExist:
        user = User.objects.create(username=data['email'],
                                   is_active=False)
        for key, value in data.iteritems():
            setattr(user, key, value)
        user.save()
        message['message'] = u"OK"
        message['id'] = user.id
        message['redirect'] = True
    return message


@api_view(['POST'])
def registration(request):
    data = request.data
    response_dict = add_user(data)
    return Response(response_dict)
