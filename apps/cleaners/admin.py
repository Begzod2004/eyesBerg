from django.contrib import admin
from .models import Category, Work, Review, Portfolio, WorkImage
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
from django.contrib import admin

class WorkImageInline(admin.StackedInline):
    model = WorkImage
    extra = 1  # Number of extra forms to display

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    inlines = [WorkImageInline]
    list_display = ['title', 'user', 'location', 'price', 'start_date', 'payment_type']
    list_filter = ['payment_type', 'start_date']
    search_fields = ['title', 'description', 'user__username']

@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    list_display = ['work', 'image']
    search_fields = ['work__title']


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
