from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Guardian)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Event)
admin.site.register(Assignment)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(Wish)
admin.site.register(WishResponse)
admin.site.register(Message)

