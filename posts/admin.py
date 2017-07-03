from django.contrib import admin

# Register your models here.
from .models import Post,Genre

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp", "favs",'draft']
	list_display_links = ["title"]
	list_editable = ["favs"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = Post


admin.site.register(Genre)
admin.site.register(Post, PostModelAdmin)