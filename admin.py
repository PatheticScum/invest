from django.contrib import admin
from .models import Addproject, Partner,Price,Region,Category
# Register your models here.
admin.site.register(Addproject)
admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Region)
