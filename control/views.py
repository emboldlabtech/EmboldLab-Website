from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Bootcamp,Registration,Blogpost,Student_project
from .forms import RegistrationForm,Cohort3RegistrationForm
from django.core.mail import EmailMessage
from email.utils import formataddr
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
import random
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger

def home(request):
    # Query to get only the featured bootcamps
    featured_bootcamps = Bootcamp.objects.filter(is_featured=True)
    masterclass_bootcamps = Bootcamp.objects.filter(is_masterclass=True)
    categories = Category.objects.all()
    projects = Student_project.objects.all()

    # List of tuples (Category, Bootcamps in that category)
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'index.html', {
        'featured_bootcamps': featured_bootcamps,
        'masterclass_bootcamps': masterclass_bootcamps,
        'categorized_bootcamps': categorized_bootcamps,
        'projects': projects
    })
# View to list all bootcamps
def bootcamp_list(request):
    bootcamps = Bootcamp.objects.all()
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'all_bootcamps.html', {'bootcamps': bootcamps, 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})



# View to display details of a specific bootcamp
# Assuming `Bootcamp` model has fields like `course_content_title_1`, `course_content_desc_1`, etc.

def bootcamp_detail(request, category_slug, bootcamp_slug):
    bootcamp = get_object_or_404(Bootcamp, category__slug=category_slug, slug=bootcamp_slug)

    # Prepare a list of tuples containing (title, description) pairs
    content_items = []
    for i in range(1, 11):
        title_attr = getattr(bootcamp, f'course_content_title_{i}', None)
        desc_attr = getattr(bootcamp, f'course_content_desc_{i}', None)
        if title_attr:
            content_items.append((title_attr, desc_attr))

    related_bootcamps = Bootcamp.objects.filter(category=bootcamp.category).exclude(id=bootcamp.id)
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'bootcamp_detail.html', {
        'bootcamp': bootcamp,
        'related_bootcamps': related_bootcamps,
        'categorized_bootcamps': categorized_bootcamps,
        'categories': categories,
        'content_items': content_items,  # Pass the processed content items to the template
    })

def about_us(request):
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'about.html',{ 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})

def terms(request):
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'terms.html', { 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})

def policy(request):
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'policy.html', { 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})

def faq(request):
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'faq.html', { 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})

from_name = 'EMBOLD DESIGN'
from_email = 'embolddesign@gmail.com'
from_formatted = formataddr((from_name, from_email))

def register_for_course(request, bootcamp_slug):
    bootcamp = get_object_or_404(Bootcamp, slug=bootcamp_slug)
    categories = Category.objects.all()
    myKey = settings.PAY_KEY
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    if request.method == 'POST':
        form = RegistrationForm(request.POST, bootcamp_price=bootcamp.price)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.bootcamp = bootcamp
            registration.save()


                        # Send email to the myself
            self_user_email_subject = "New Order Received!"
            self_user_email_body = render_to_string('new_order.html')
            my_email_message = EmailMessage(
                self_user_email_subject,
                self_user_email_body,
                from_formatted,
                [settings.EMAIL_HOST_NAME],
            )
            my_email_message.content_subtype = "html"




            # Get user details from form
            user_email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')

            # Send welcome email
            user_email_subject = "Welcome To embold!"
            user_email_body = render_to_string('welcome.html', {
                'username': first_name,
                'user_email': user_email
            })

            email_message = EmailMessage(
                user_email_subject,
                user_email_body,
                from_formatted,  # Replace with your from email
                [user_email]
            )
            email_message.content_subtype = "html"

            try:
                email_message.send()
                my_email_message.send()
                # Log email sending success
                print(f"Email successfully sent to {user_email}")

            except Exception as e:
                # Log email sending failure
                print(f"Failed to send email to {user_email}. Error: {e}")

            # Redirect to success page
            return redirect('success_page')  # Use the name of your URL pattern for the success page



            # Process payment or any other logic here

            return render(request, 'register.html', {
                'form': form,
                'bootcamp': bootcamp,
                'categorized_bootcamps': categorized_bootcamps,
                'categories': categories,
                'bootcamp_price': bootcamp.price,
            })
    else:
        form = RegistrationForm(initial={'bootcamp': bootcamp, 'bootcamp_price': bootcamp.price})

    return render(request, 'register.html', {
        'form': form,
        'bootcamp': bootcamp,
        'categorized_bootcamps': categorized_bootcamps,
        'categories': categories,
        'bootcamp_price': bootcamp.price,
        'myKey' : myKey,
    })


def register(request):
    myKey = settings.PAY_KEY
    if request.method == 'POST':
        form = Cohort3RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the registration form
            registration = form.save()

            # Get user details from the form
            user_email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')

            # Prepare email for the site owner
            self_user_email_subject = "New Registration Received!"
            self_user_email_body = render_to_string('new_registration.html', {
                'registration': registration
            })
            my_email_message = EmailMessage(
                self_user_email_subject,
                self_user_email_body,
                settings.EMAIL_HOST_USER,  # Replace with your from email
                [settings.EMAIL_HOST_NAME],  # Replace with your notification email
            )
            my_email_message.content_subtype = "html"

            # Prepare welcome email for the user
            user_email_subject = "Welcome to the Cohort!"
            user_email_body = render_to_string('welcome_email.html', {
                'username': first_name,
                'user_email': user_email
            })
            email_message = EmailMessage(
                user_email_subject,
                user_email_body,
                settings.EMAIL_HOST_USER,  # Replace with your from email
                [user_email]
            )
            email_message.content_subtype = "html"

            try:
                email_message.send()  # Send welcome email to the user
                my_email_message.send()  # Send registration notification to admin
                # Log email sending success
                print(f"Emails successfully sent to {user_email} and admin.")
            except Exception as e:
                # Log email sending failure
                print(f"Failed to send emails. Error: {e}")

            # Redirect to success page after successful registration
            return redirect('registration_success')  # Adjust to your success page URL name
    else:
        form = Cohort3RegistrationForm()

    return render(request, 'application.html', {'form': form,  'myKey': myKey,})


# def register_for_course(request, bootcamp_slug):
#     categories = Category.objects.all()
#     bootcamp = get_object_or_404(Bootcamp, slug=bootcamp_slug)
#     categorized_bootcamps = [
#         (category, Bootcamp.objects.filter(category=category)) for category in categories
#     ]

#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             registration = form.save(commit=False)
#             registration.bootcamp = bootcamp
#             registration.save()

#     else:
#         form = RegistrationForm(initial={'bootcamp': bootcamp})

#     return render(request, 'register.html', {'form': form, 'bootcamp': bootcamp,  'categorized_bootcamps': categorized_bootcamps, 'categories': categories})

def success_page(request):
    return render(request, 'success.html')

def contact_page(request):
    return render(request, 'contact.html')

def service_page(request):
    return render(request, 'service.html')

def work_page(request):
    return render(request, 'work.html')
def ship_page(request):
    return render(request, 'ship.html')

def posts(request, slug):
    # Get the Blogpost object for the given slug
    post = get_object_or_404(Blogpost, slug=slug)
    categories = Category.objects.all()

    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    # Increment the visit count and update the last visit time for the post
    post.num_views += 1
    post.last_visit = timezone.now()
    post.save()

    # Get related posts (you might want to refine this logic)
    related_posts = Blogpost.objects.exclude(slug=slug).order_by('?')[:4]

    # Prepare images data
    images = [
        {
            "url": post.Cover_image.url,
            "caption": post.title
        }
    ]

    # Create the context dictionary
    context = {
        "post": post,
        "related_posts": related_posts,
        "images": images,
        'categorized_bootcamps': categorized_bootcamps,

    }

    return render(request, 'blog_detail.html', context)

def blog(request):
    all_posts = Blogpost.objects.all()
    categories = Category.objects.all()
    popular_posts = Blogpost.objects.order_by('-num_views')[:5]
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    paginator = Paginator(all_posts, 6)
    page_num = request.GET.get('page', 1)

    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {
        'all_posts': page,
        'timezone': timezone,
        'categorized_bootcamps': categorized_bootcamps,
        'popular_posts': popular_posts,
    }

    return render(request, 'blog_list.html', context)