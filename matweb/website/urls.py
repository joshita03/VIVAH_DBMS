from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/dash', views.dash, name='dash'),
    path('login/partnerpref', views.partner_pref, name='partner_pref'),
    #path('profile_pic/', views.profile_pic, name='profile_pic'),
    path('login/pic', views.pic, name='pic'),
    path('login/profile', views.profile, name='profile'),
    path('login/feedback', views.feedback_form, name='feedback'),
    path('save_profile/', views.save_customer_profile, name='save_customer_profile'),
    path('save_feedback/', views.save_feedback, name='save_feedback'),
    #path('save_pic/', views.save_user_pic, name='save_user_pic'),
    path('save_preferences/', views.save_partner_pref, name='save_partner_pref'),
    path('personal_profile/', views.user_profile, name='user_profile'),
    #path('profile_pic/', views.profile_pic, name='profile_pic'),
    path('saved_pp/', views.pp_profile, name='pp_profile'),
    path('match/', views.get_matching_customers, name='match'),
    path('user_activities/', views.get_user_activities, name='user_activities'),
    path('delete_customer/', views.delete_customer, name='delete_customer'),
    path('login/pics/', views.index, name='index'),
    path('login/upload_image/', views.uploadView, name= 'upload_image'),
    path('login/display_pic/', views.display_pic, name= 'display_pic')

]