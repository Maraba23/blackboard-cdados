import code
from imp import reload
import profile
import random
import string
import subprocess
import re
from tokenize import Token
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import *
from django.contrib.auth import login
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import sweetify

# Create your views here.
def home(request):
    return render(request, 'home.html')