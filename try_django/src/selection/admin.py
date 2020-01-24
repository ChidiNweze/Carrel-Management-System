from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Carrel
from .models import Floor
from .models import Program

admin.site.register(Student)
admin.site.register(Carrel)
admin.site.register(Floor)
admin.site.register(Program)