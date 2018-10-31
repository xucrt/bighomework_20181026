from django.contrib import admin
from .models import Plate, Post, User, Reply
#from .models import Plate, Post, Reply

# Register your models here.
admin.site.register(Plate)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Reply)