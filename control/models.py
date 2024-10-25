from django.db import models

# Create your models here.
# course model

from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from PIL import Image
from io import BytesIO
from django.core.files import File
from cloudinary.models import CloudinaryField


from ckeditor.fields import RichTextField



class Category(models.Model):
    title = models.CharField(max_length=555)
    slug = models.SlugField(max_length=555)

    def __str__(self):
        return self.title

class Bootcamp(models.Model):
    category = models.ForeignKey(Category, related_name='bootcamps', on_delete=models.CASCADE)
    title = models.CharField(max_length=555)
    slug = models.SlugField(max_length=555)
    image = CloudinaryField('image', blank=True, null=True)
    intro = RichTextField(blank=True)
    subdetail = RichTextField(blank=True)
    course_content_title_1 = RichTextField(blank=True)
    course_content_desc_1 = RichTextField(blank=True)
    course_content_title_2 = RichTextField(blank=True)
    course_content_desc_2 = RichTextField(blank=True)
    course_content_title_3 = RichTextField(blank=True)
    course_content_desc_3 = RichTextField(blank=True)
    course_content_title_4 = RichTextField(blank=True)
    course_content_desc_4 = RichTextField(blank=True)
    course_content_title_5 = RichTextField(blank=True)
    course_content_desc_5 = RichTextField(blank=True)
    course_content_title_6 = RichTextField(blank=True)
    course_content_desc_6 = RichTextField(blank=True)
    course_content_title_7 = RichTextField(blank=True)
    course_content_desc_7 = RichTextField(blank=True)
    course_content_title_8 = RichTextField(blank=True)
    course_content_desc_8 = RichTextField(blank=True)
    course_content_title_9 = RichTextField(blank=True)
    course_content_desc_9 = RichTextField(blank=True)
    course_content_title_10 = RichTextField(blank=True)
    course_content_desc_10 = RichTextField(blank=True)
    price = models.FloatField()
    former_price= models.FloatField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_masterclass = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    num_visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)



    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super( Bootcamp, self).save(*args, **kwargs)



    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'WEBP', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail



class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    LEVEL_CHOICES = [
        ('F', 'Fresher'),
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    ]
    OPTIONS = [
        ('Y', 'Yes'),
        ('N', 'No'),

    ]

    SOURCE_CHOICES = [
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
        ('LinkedIn', 'LinkedIn'),
        ('Referral', 'Referral'),
        ('NAUS', 'NAUS'),
    ]

    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE)
    first_name = models.CharField(default='john', max_length=255 )
    middle_name = models.CharField( max_length=255, blank=True, null=True)
    surname = models.CharField(default='doe', max_length=255)
    phone = models.CharField( max_length=20, default='')
    email = models.EmailField()
    referral_code = models.CharField( max_length=255, blank=True, null=True)
    gender = models.CharField(default='M', max_length=1, choices=GENDER_CHOICES )
    level = models.CharField(default='B', max_length=1, choices=LEVEL_CHOICES)
    laptop_access =models.CharField(default='Y', max_length=1, choices=OPTIONS )
    full_duration_commitment = models.CharField(default='Y', max_length=1, choices=OPTIONS )
    source = models.CharField(max_length=205, choices=SOURCE_CHOICES , blank=True, null=True)
    pledge_dedication = models.BooleanField(default='True',blank=False, null=False)
    pledge_terms = models.BooleanField(default='True' , blank=False, null=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} registered for {self.bootcamp.title}"


# Define the Author model with name and color fields
class Author(models.Model):
    COLOR_CHOICES = [
        ('#FF5733', 'Red'),
        ('#33FF57', 'Green'),
        ('#3357FF', 'Blue'),
        ('#FF33A5', 'Pink'),
        ('#33FFF6', 'Cyan'),
        ('#F6FF33', 'Yellow'),
        ('#FF8C33', 'Orange'),
    ]

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, help_text="Select a color")

    def __str__(self):
        return self.name


class Blogpost(models.Model):
    title = models.CharField(max_length=3700)
    Cover_image = CloudinaryField('image')
    subtitle = models.CharField(max_length=20000)
    slug = models.SlugField(unique=True, max_length=3700)
    post_detail = RichTextField(blank=True, null=True)
        # Add author field as a ForeignKey

    # ForeignKey to Author without default value
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogposts")


    num_views = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    thumbnail = CloudinaryField('image')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super( Blogpost, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return '/%s/' % (self.slug)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class Student_project(models.Model):
    title = models.CharField(max_length=3700)
    Cover_image = CloudinaryField('image')
    subtitle = models.CharField(max_length=20000)
    link =models.URLField()

    def __str__(self):
        return self.title




class BootcampRegistration(models.Model):
    PROGRAM_CHOICES = [
        ('Bootcamp', 'Bootcamp'),
        ('Accelerator', 'Accelerator Program'),
        ('Masterclass', 'Masterclass'),
    ]

    LEVEL_CHOICES = [
        ('Fresher', 'Fresher'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    SOURCE_CHOICES = [
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
        ('LinkedIn', 'LinkedIn'),
        ('Referral', 'Referral'),
        ('NAUS', 'NAUS'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    laptop_access = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    course = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    location = models.TextField()
    proof_of_payment = models.FileField(upload_to='payments/')
    referral_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.program}'
