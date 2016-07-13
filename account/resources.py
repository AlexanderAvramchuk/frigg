# -*- coding: utf-8
from import_export import resources
from account.models import CustomUser as User


class UserResource(resources.ModelResource):
    """For excel import/export"""
    class Meta:
        model = User
        #fields = ('id', 'username', 'last_name', 'first_name', 'middle_name',
        #          'email', 'phone_number', 'skype', 'country', 'city', 'address',
        #          'born_date', 'facebook', 'vkontakte', 'description',
        #          'department', 'hierarchy', 'master')
        exclude = ('user_ptr', 'first_name', 'last_name', 'middle_name',)
        #export_order = ('id', 'username', 'last_name', 'first_name', 'middle_name',
        #                'email', 'phone_number', 'skype', 'country', 'city', 'address',
        #                'born_date', 'facebook', 'vkontakte', 'description',
        #                'department', 'hierarchy', 'master')


def clean_password(data):
    password1 = data['password1']
    password2 = data['password2']
    if password1 and password2:
        if password1 == password2:
            return password2
        else:
            return False
    else:
        return False


def clean_old_password(user, data):
        if data["old_password"]:
            old_password = data["old_password"]
            if user.check_password(old_password):
                return old_password
            else:
                return False
        else:
            return False