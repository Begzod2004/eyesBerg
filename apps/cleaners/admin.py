from django.contrib import admin
from .models import Category, Work, Review, Portfolio
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Optional: Custom Admin for Django's built-in User model
class UserAdmin(BaseUserAdmin):
    pass

# Admin for Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Admin for Work
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'location', 'price')
    search_fields = ('title', 'description')
    list_filter = ('location',)

# Admin for Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'work', 'stars')
    search_fields = ('description',)
    list_filter = ('stars',)

# Admin for Portfolio
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')
    search_fields = ('category__name',)

# Register the custom UserAdmin
admin.site.register(User, UserAdmin)
