import re

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def all_users(request):
    if request.method == 'GET':
        # get all users
        users = User.objects.all()

        # return them
        return Response(
            UserSerializer(
                users,
                many=True).data
        )
    elif request.method == 'POST':
        # test entries
        username = request.data.get('username').strip()
        matchs = re.match("^[\\w.@+-]+$", username)
        if matchs is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=["username invalid"]
            )

        # creating new user
        try:
            user = User.objects.create_user(
                username=username,
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                password=request.data.get('password'),
                is_active=request.data.get('is_active'),
            )
        except Exception as exp:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=["something went wrong when saving user"]
            )

        # return created user
        return Response(
            status=status.HTTP_201_CREATED,
            data=UserSerializer(user).data
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def crud_users(request, id: str or int):
    if request.method == 'GET':
        # search user
        user = User.objects.filter(id=id)

        # return it
        return Response(
            UserSerializer(
                user[0]
            ).data if len(user) > 0 else []
        )
    elif request.method == 'PUT':
        # search for the user to be usdated
        user = User.objects.filter(id=id)
        if len(user) == 0:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=["user {} not found".format(id)]
            )
        else:
            user: User = user[0]

        # treat entries
        data = {
            'username': request.data.get('username'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'password': request.data.get('password'),
            'is_active': request.data.get('is_active'),
        }

        for key in data:
            if(not data[key]):
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=["{} must be present".format(key)]
                )

        # udate infos
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.password = data['password']
        user.is_active = data['is_active']

        # save informations
        try:
            user.save()
        except BaseException:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERRORm,
                data=["could not save user"]
            )

        # return updated user
        return Response(UserSerializer(user).data)
    elif request.method == 'PATCH':
        # search for the user to be usdated
        user = User.objects.filter(id=id)
        if len(user) == 0:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=["user {} not found".format(id)]
            )
        else:
            user: User = user[0]

        # treat entries
        data = {
            'username': request.data.get('username'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'password': request.data.get('password'),
            'is_active': request.data.get('is_active'),
        }

        # udate infos
        if data['username'] is not None:
            user.username = data['username']
        if data['first_name'] is not None:
            user.first_name = data['first_name']
        if data['last_name'] is not None:
            user.last_name = data['last_name']
        if data['password'] is not None:
            user.password = data['password']
        if data['is_active'] is not None:
            user.is_active = data['is_active']

        # save informations
        try:
            user.save()
        except BaseException:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERRORm,
                data=["could not save user"]
            )

        # return updated user
        return Response(UserSerializer(user).data)
    elif request.method == 'DELETE':
        # search for the user to be usdated
        user = User.objects.filter(id=id)
        if len(user) == 0:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=["user {} not found".format(id)]
            )
        else:
            user: User = user[0]

    try:
        user.delete()
    except BaseException:
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data=["could not delete user"]
        )

    return Response(status.HTTP_204_NO_CONTENT)
