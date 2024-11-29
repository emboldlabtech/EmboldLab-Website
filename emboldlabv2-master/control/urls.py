from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('blog/<slug:slug>/', views.posts, name='posts'),
    path('terms-and-conditions/',  views.terms, name='terms'),
    path('privacy-policy/',  views.policy, name='policy'),
    path('about-us/',  views.about_us, name='about_us'),
    path('faq/',  views.faq, name='faq'),
    path('register/<slug:bootcamp_slug>/', views.register_for_course, name='register_for_course'),
    path('bootcamp/', views.bootcamp_list, name='bootcamp_list'),
    path('masterclass/', views.masterclass_list, name='masterclass'),
    path('accelerator-programs/', views.accelerator_list, name='accelerator'),
    #path('categories/', views.category_list, name='category_list'),
    #path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:bootcamp_slug>/', views.bootcamp_detail, name='bootcamp_detail'),
    path('success/', views.success_page, name='success_page'),
    path('register-for-cohort/', views.register, name='application'),

    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_page, name='contact'),
    path('services/', views.service_page, name='services'),
    path('work/', views.work_page, name='work'),
    path('dropship-services/', views.ship_page, name='ship'),


    path('special-accessx12y90qu_v_cash/', views.special_access_register, name='special_access_register'),
    path('access-signup', views.access_register, name='access'),





    path('messages/', views.message_page, name='message_page'),
    path('messages/send/', views.send_message, name='send_message'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

]