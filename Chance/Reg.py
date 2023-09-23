import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chance.settings')
django.setup()


from Regression.models import Params

params = Params.objects.get(pk=1)  # replace 1 with the primary key of the Params object you want to use
a = params.Age
b = params.Asset
c = params.Financial

def Regression(a, b, c):
    C = 0.01 * c + 0.23 * b + 0.012 * a 
    print(C)

Regression(a , b , c)