import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.text import slugify
from .forms import BootcampForm,CategoryForm,RegistrationForm,BlogForm
from .models import Blogpost,Student_project
def export_registrations_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

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

# Register your models here.
from .models import Bootcamp, Category, Registration
admin.site.site_header = 'Embold Design Dashboard'

class BootcampAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price']
    list_filter = ['category', 'is_featured']
    list_filter = ('category', 'is_featured', 'start_date', 'end_date')
    search_fields = ('title', 'category__title')
    form = BootcampForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()

class ProductAdmin(admin.ModelAdmin):
    form = CategoryForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()
        

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'bootcamp', 'date_registered','referral_code')
    list_filter = ('bootcamp', 'date_registered')
    search_fields = ('first_name', 'surname', 'email', 'bootcamp__title')
    ordering = ('-date_registered',)
    actions = [export_registrations_to_csv]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.surname}"
    full_name.short_description = 'Name'

class ProductAdmin(admin.ModelAdmin):
    # list_display=('title', 'category','price','num_available')
    # list_filter =['category','is_featured','timer_products','new_product','hot_deals','top_sale',]

    form = BlogForm

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        obj.save()


admin.site.register(Blogpost, ProductAdmin)
admin.site.register(Student_project)

admin.site.register(Bootcamp, BootcampAdmin)
admin.site.register(Category, ProductAdmin)
admin.site.register(Registration, RegistrationAdmin)
