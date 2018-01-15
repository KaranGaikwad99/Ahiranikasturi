from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# Register your models here.
from.models import Post, Program, Contact_us, Gallery

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_filter = ["updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]

    search_fields = ["title","content"]
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_filter = ["updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]

    search_fields = ["title","content"]
    class Meta:
        model = Program

admin.site.register(Program,ProgramModelAdmin)

class GalleryModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_filter = ["updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]

    search_fields = ["title","content"]
    class Meta:
        model = Gallery

admin.site.register(Gallery,GalleryModelAdmin)


class Contact_usModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "subject","message"]

    search_fields = ["first_name", "last_name" ]
    class Meta:
        model = Contact_us

admin.site.register(Contact_us, Contact_usModelAdmin)