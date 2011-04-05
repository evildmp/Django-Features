from django.contrib import admin
from features.models import Request, Comment
from cms.admin.placeholderadmin import PlaceholderAdmin

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    
class RequestAdmin(PlaceholderAdmin):
    inlines = [CommentInline]
    
admin.site.register(Request,RequestAdmin)