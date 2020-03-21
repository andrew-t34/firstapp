import random
from django.contrib.auth.mixins import PermissionGroupMixin
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer



class ParentTestList():
    permission_required = ['listener', 'admin']
