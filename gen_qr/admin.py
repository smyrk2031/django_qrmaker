from django.contrib import admin
from .models import regist_table, temp_image

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
#class YourModelAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'created_at')
    #list_display_links = ('id', 'name')
    #search_fields = ('name',)
    #list_filter = ('created_at',)
admin.site.register(regist_table, PostAdmin)
admin.site.register(temp_image, PostAdmin)
