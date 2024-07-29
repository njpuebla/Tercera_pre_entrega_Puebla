from django.contrib import admin
from app.models import Electrica
from app.models import Acustica
from app.models import Amplificadore
from app.models import Efecto

# Register your models here.
admin.site.register(Electrica)
admin.site.register(Acustica)
admin.site.register(Amplificadore)
admin.site.register(Efecto)