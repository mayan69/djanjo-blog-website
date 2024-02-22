from django.contrib import admin
from .models import BlogPost




# Register your models here.

class MainAppAdmin(admin.ModelAdmin):
    list_display=["id","title","published_date"]
    list_display_links=["id", "title"]


admin.site.register(BlogPost,MainAppAdmin)


admin.site.site_header="Django Blog Website Panel"  #to change the site panel title to any name we want
admin.site.site_title="Site portal" #for the before you open the webiste admin where you put password and username
admin.site.index_title="site administrative panel"