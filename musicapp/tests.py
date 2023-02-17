from django.test import TestCase

# Create your tests here.
import os
import django
from django.db import connection
from django.db.models import Q, F, Sum, Min

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music.settings')
django.setup()
from musicapp.models import *

queryset = Musicdata.objects.order_by("id")
for i in queryset:
    print(i.name)