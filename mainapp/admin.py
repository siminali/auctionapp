from django.contrib import admin

# Register your models here.

#from django.contrib.auth.admin import User
from .models import User


from .models import Item
from .models import QandA
from .models import Bids

#admin.site.register(User, UserAdmin)
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Bids)
admin.site.register(QandA)





