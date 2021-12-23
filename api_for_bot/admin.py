from django.contrib import admin



# Register your models here.
from api_for_bot.models import APIData, URL

admin.site.register(APIData)
admin.site.register(URL)