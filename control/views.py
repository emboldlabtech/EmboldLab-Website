from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Bootcamp,Registration,Blogpost,Student_project, Contact, DropShipping, Subscriber
from .forms import RegistrationForm,Cohort3RegistrationForm
from django.core.mail import EmailMessage
from email.utils import formataddr
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
import random
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
import requests


def home(request):
    # Query to get only the featured bootcamps
    featured_bootcamps = Bootcamp.objects.filter(is_featured=True)
    masterclass_bootcamps = Bootcamp.objects.filter(is_masterclass=True)
    accelerator_bootcamps = Bootcamp.objects.filter(is_accelerator=True)
    categories = Category.objects.all()
    projects = Student_project.objects.all()

    # List of tuples (Category, Bootcamps in that category)
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'index.html', {
        'featured_bootcamps': featured_bootcamps,
        'masterclass_bootcamps': masterclass_bootcamps,
        'accelerator_bootcamps': accelerator_bootcamps,
        'categorized_bootcamps': categorized_bootcamps,
        'projects': projects
    })
# View to list all bootcamps
def bootcamp_list(request):
    bootcamps = Bootcamp.objects.filter(is_featured=True)
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'all_bootcamps.html', {'bootcamps': bootcamps, 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})




def masterclass_list(request):
    bootcamps = Bootcamp.objects.filter(is_masterclass=True)
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'masterclass.html', {'bootcamps': bootcamps, 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})



def accelerator_list(request):
    bootcamps = Bootcamp.objects.filter(is_accelerator=True)
    categories = Category.objects.all()
    categorized_bootcamps = [
        (category, Bootcamp.objects.filter(category=category)) for category in categories
    ]

    return render(request, 'accelerator.html', {'bootcamps': bootcamps, 'categorized_bootcamps': categorized_bootcamps, 'categories': categories})



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
            # Check if a user with the provided email already exists
            User = get_user_model()
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                # Raise an error if a user with this email already exists
                form.add_error('email', 'An account with this email already exists. Please log in.')
            else:
                # Create User account with the provided password
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    email=email,
                    password=form.cleaned_data['password1']
                )
                # Save registration and associate with user
                registration = form.save(commit=False)
                registration.user = user
                registration.save()

                # Log the user in after successful registration
                login(request, user)

                # Send a welcome email
                user_email_subject = "Welcome to the Cohort - Special Access!"
                user_email_body = render_to_string('welcome.html', {'username': user.username, 'user_email': user.email})
                email_message = EmailMessage(
                    user_email_subject,
                    user_email_body,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                email_message.content_subtype = "html"

                try:
                    email_message.send()  # Send welcome email to the user
                    print(f"Welcome email successfully sent to {user.email}")
                except Exception as e:
                    print(f"Failed to send welcome email. Error: {e}")

                # Redirect to the profile update page or dashboard
                return redirect('profile_update')  # Replace with actual URL name for profile update page
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = Cohort3RegistrationForm()

    return render(request, 'application.html', {'form': form,  'myKey': myKey})



from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import Cohort3RegistrationForm
from .forms import ProfileUpdateForm  # A form for updating user profi


from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import Cohort3RegistrationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model



def access_register(request):
    myKey = settings.PAY_KEY
    if request.method == 'POST':
        form = Cohort3RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if a user with the provided email already exists
            User = get_user_model()
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                # Raise an error if a user with this email already exists
                form.add_error('email', 'An account with this email already exists. Please log in.')
            else:
                # Create User account with the provided password
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    email=email,
                    password=form.cleaned_data['password1']
                )
                # Save registration and associate with user
                registration = form.save(commit=False)
                registration.user = user
                registration.save()

                # Log the user in after successful registration
                                # Specify the custom backend
                backend = 'control.backends.EmailBackend'
                user.backend = backend
                login(request, user, backend=backend)

                # Send a welcome email
                user_email_subject = "Welcome to the Cohort - Special Access!"
                user_email_body = render_to_string('welcome.html', {'username': user.username, 'user_email': user.email})
                email_message = EmailMessage(
                    user_email_subject,
                    user_email_body,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                email_message.content_subtype = "html"

                try:
                    email_message.send()  # Send welcome email to the user
                    print(f"Welcome email successfully sent to {user.email}")
                except Exception as e:
                    print(f"Failed to send welcome email. Error: {e}")

                # Redirect to the profile update page or dashboard
                return redirect('profile_update')  # Replace with actual URL name for profile update page
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = Cohort3RegistrationForm()

    return render(request, 'access.html', {'form': form, 'myKey' :myKey})






















def special_access_register(request):
    if request.method == 'POST':
        form = Cohort3RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if a user with the provided email already exists
            User = get_user_model()
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                # Raise an error if a user with this email already exists
                form.add_error('email', 'An account with this email already exists. Please log in.')
            else:
                # Create User account with the provided password
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    email=email,
                    password=form.cleaned_data['password1']
                )
                # Save registration and associate with user
                registration = form.save(commit=False)
                registration.user = user
                registration.save()

                # Log the user in after successful registration
                                # Specify the custom backend
                backend = 'control.backends.EmailBackend'
                user.backend = backend
                login(request, user, backend=backend)

                # Send a welcome email
                user_email_subject = "Welcome to the Cohort - Special Access!"
                user_email_body = render_to_string('welcome.html', {'username': user.username, 'user_email': user.email})
                email_message = EmailMessage(
                    user_email_subject,
                    user_email_body,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                email_message.content_subtype = "html"

                try:
                    email_message.send()  # Send welcome email to the user
                    print(f"Welcome email successfully sent to {user.email}")
                except Exception as e:
                    print(f"Failed to send welcome email. Error: {e}")

                # Redirect to the profile update page or dashboard
                return redirect('profile_update')  # Replace with actual URL name for profile update page
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = Cohort3RegistrationForm()

    return render(request, 'special_access.html', {'form': form})






from .forms import ProfileUpdateForm, CohortUpdateForm


from django.shortcuts import render

from .forms import ProfileUpdateForm


@login_required
def profile_update(request):
    try:
        user = request.user
        profile_form = ProfileUpdateForm(request.POST or None, instance=user)
        cohort_form = CohortUpdateForm(request.POST or None, request.FILES or None, instance=user.cohort_registration)

        if profile_form.is_valid() and cohort_form.is_valid():
            profile_form.save()
            cohort_form.save()
            print(f"Saved profile picture URL: {user.cohort_registration.profile_picture.url}")
            return redirect('dashboard')  # Redirect after saving the form
        else:
        # Print errors to debug why the form isn't saving
            print("Profile form errors:", profile_form.errors)
            print("Cohort form errors:", cohort_form.errors)

        return render(request, 'profile_update.html', {
            'profile_form': profile_form,
            'cohort_form': cohort_form,
        })
    except Cohort3Registration.DoesNotExist:
        messages.error(request, "You do not have a cohort registration associated with your account.")
        return redirect('login')




from .models import Cohort3Registration















@login_required  # Ensure that the user is logged in
def dashboard(request):
    try:
        cohort_registration = Cohort3Registration.objects.get(user=request.user)
        progress = cohort_registration.progress_percentage

        certificate = cohort_registration.certificate
        return render(request, 'dashboard.html', {
            'progress': progress,

            'certificate': certificate,
        })

    except Cohort3Registration.DoesNotExist:
        messages.error(request, "You do not have a cohort registration associated with your account.")
        return redirect('login')

from .models import Message
from .forms import MessageForm

@login_required
def message_page(request):
    received_messages = Message.objects.filter(recipient=request.user)
    sent_messages = Message.objects.filter(sender=request.user)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.instance.sender = request.user
            form.save()
            return redirect('message_page')
    else:
        form = MessageForm()

    context = {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
        'form': form,
    }
    return render(request, 'messages/message_page.html', context)

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Assign the sender to the current user (Instructor or Support)
            form.instance.sender = 'instructor'  # Or 'support', depending on the sender
            form.instance.recipient = form.cleaned_data['recipient']  # User selected
            form.save()
            return redirect('message_page')  # Redirect to the message page after sending

    else:
        form = MessageForm()

    return render(request, 'messages/send_message.html', {'form': form})



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the email and password from the form
            email = form.cleaned_data.get('username')  # We'll treat 'username' field as 'email' here
            password = form.cleaned_data.get('password')

            # Authenticate the user by email
            user = authenticate(request, username=email, password=password)  # 'username' now holds email

            if user is not None:
                # Log the user in
                login(request, user)
                # Redirect to the original page or the dashboard
                next_url = request.GET.get('next', 'dashboard')  # If 'next' exists in GET, use it; otherwise, use 'dashboard'
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid email or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def success_page(request):
    return render(request, 'success.html')

def contact_page(request):
    if request.method == "POST":
        try:
            new_contact = Contact(
                name = request.POST.get("fName"),
                email = request.POST.get("fEmail"),
                reason = request.POST.get("reason"),
                message = request.POST.get("fMessage")
            )
            new_contact.save()
            messages.success(request, "Thank you for contacting us, we'll reach out to you shortly.")
        except Exception as e:
            print(f"An error occured: {e}")
    return render(request, 'contact.html')

def service_page(request):
    return render(request, 'service.html')

def work_page(request):
    projects = Student_project.objects.all()
    return render(request, 'work.html', {'projects': projects})
def ship_page(request):
    if request.method == "POST":
        new_ship = DropShipping(
            email=request.POST.get("email")
        )
        new_ship.save()
        messages.success(request, "Thanks for subscribing to our dropshiping launch mail, we will notify you when we launch")
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

    if request.method == "POST":
        new_sub = Subscriber(
            email=request.POST.get("fEmail")
        )
        new_sub.save()
        messages.success(request, "Thanks for subscribing to our newsletter!")
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
    if request.method == "POST":
        new_sub = Subscriber(
            email=request.POST.get("fEmail")
        )
        new_sub.save()
        messages.success(request, "Thanks for subscribing to our newsletter!")
    context = {
        'all_posts': page,
        'timezone': timezone,
        'categorized_bootcamps': categorized_bootcamps,
        'popular_posts': popular_posts,
    }

    return render(request, 'blog_list.html', context)