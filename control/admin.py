import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.text import slugify
from .forms import BootcampForm, CategoryForm, RegistrationForm, BlogForm
from .models import Blogpost, Student_project, Author, Cohort3Registration, Bootcamp, Category, Registration, Message, Contact, DropShipping

def export_registrations_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registrations.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Middle Name', 'Surname', 'Email', 'Bootcamp', 'Date Registered'])

    for registration in queryset:
        writer.writerow([
            registration.first_name,
            registration.middle_name,
            registration.surname,
            registration.email,
            registration.bootcamp.title,
            registration.date_registered
        ])
    return response

export_registrations_to_csv.short_description = 'Export selected registrations to CSV'


# Admin header
admin.site.site_header = 'Embold Lab Dashboard'


class BootcampAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price']
    list_filter = ['category', 'is_featured', 'start_date', 'end_date']
    search_fields = ('title', 'category__title')
    form = BootcampForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()

    def has_module_permission(self, request):
        return request.user.groups.filter(name='Developer').exists() or request.user.is_superuser


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'bootcamp', 'date_registered', 'referral_code')
    list_filter = ('bootcamp', 'date_registered')
    search_fields = ('first_name', 'surname', 'email', 'bootcamp__title')
    ordering = ('-date_registered',)
    actions = [export_registrations_to_csv]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.surname}"
    full_name.short_description = 'Name'


class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added')  # Ensure 'created_at' exists in Blogpost model
    search_fields = ('title', 'author__name')
    form = BlogForm

    def has_module_permission(self, request):
        return request.user.groups.filter(name='Editor').exists() or request.user.is_superuser


class Cohort3RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'program', 'course' ,'progress_percentage')
    search_fields = ['name', 'email','course']
    list_filter = ['course']

    def has_module_permission(self, request):
        return request.user.groups.filter(name='Developer').exists() or request.user.is_superuser
    # Allow admin to select a user and edit all at once
    def save_model(self, request, obj, form, change):
        obj.save()


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'sent_at', 'is_read')
    search_fields = ['sender__username', 'recipient__username']

admin.site.register(Message, MessageAdmin)
# Registering models with role-based ModelAdmin classes
admin.site.register(Bootcamp, BootcampAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Student_project)  # Unrestricted access to Student_project
admin.site.register(Author)  # Unrestricted access to Author
admin.site.register(Cohort3Registration, Cohort3RegistrationAdmin)
admin.site.register(Contact)
admin.site.register(DropShipping)
