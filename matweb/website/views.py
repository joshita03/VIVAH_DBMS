from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from .forms import ImageUploadForm
 
from . import models

def home(request):
    return render(request, 'home.html', {})

def dash(request):
    return render(request,'dash.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('logged in')
            print(username)
            login(request, user=user)
            return render(request, 'dash.html', {})
        else:
            print('not logged in')
    return render(request, 'login.html', {})


def logout_user(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print("You already exist")
            return redirect("login")
        else:
            User.objects.create_user(username, email=email, password=password)
            with connection.cursor() as cursor:
                cursor.execute(f'''CREATE USER if not exists '{username}'@'localhost' IDENTIFIED BY '{password}';''')
                cursor.execute(f'''grant Cust to '{username}'@'localhost';''')
            return redirect("dash")
    return render(request,'signup.html',{})

def save_customer_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        height = request.POST.get('height')
        about_me = request.POST.get('about')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        mother_tongue = request.POST.get('mother_tongue')
        occupation = request.POST.get('occupation')
        income = request.POST.get('income')
        religion = request.POST.get('religion')
        drink = request.POST.get('drink')
        smoke = request.POST.get('smoke')
        diet = request.POST.get('diet')
        highest_education = request.POST.get('highest-education')
        prev_marital_status = request.POST.get('prev-marital-status')
        matched = request.POST.get('matched')

        user = request.user


        customer = models.Customer.objects.create(
        Cust_id=user,
        Name=name,
        DOB=dob,
        Sex=sex,
        Height=height,
        Mother_tongue=mother_tongue,
        Occupation=occupation,
        Income=income,
        City=city,
        Country=country,
        Religion=religion,
        Drink=drink,
        Smoke=smoke,
        Diet=diet,
        Highest_Education=highest_education,
        Prev_Marital_Status=prev_marital_status,
        About_Me=about_me,
        Matched=matched
    )
        
    # This is the trigger that checks the marital status 
        marital_status_warning = check_marital_status(request)
        if marital_status_warning:
            return marital_status_warning  

        return redirect('dash') #success page do

    
    return render(request, 'dash.html',{})

def save_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('review')
        rating = request.POST.get('rating')

        
        try:
            rating = int(rating)
        except ValueError:
            
            return render(request, 'feed.html', {'error_message': 'Invalid Rating'})

        
        if not 1 <= rating <= 5:
            return render(request, 'feed.html', {'error_message': 'Rating must be between 1 and 5'})

        
        user = request.user

        
        feedback = models.Feedback.objects.create(
            Cust_id=user,
            Feedback=feedback_text,
            Rating=rating
        )

        return render(request, 'dash.html', {'feedback': feedback})

    return render(request, 'feed.html')


'''def save_user_pic(request):
    if request.method == 'POST':
        photo=request.Post.get('photo')
        user=request.user
        customer = models.Photos.objects.create(
            Pic1=photo
        )
    return render(request, 'dash.html',{})'''



def user_profile(request):
    user = request.user
    customer = models.Customer.objects.get(Cust_id=user)
    return render(request, 'personal_profile.html', {'customer': customer})

def feedback_form(request):
    user = request.user
    if models.Feedback.objects.filter(Cust_id=user).exists():
        feedback = models.Feedback.objects.get(Cust_id=user)
        return render(request, 'saved_feedback.html', {'feedback': feedback})
    else:
        return render(request, 'feed.html')

'''def profile_pic(request):
    user=request.user
    photo = models.Photos.objects.get(Cust_id_id=user)
    return render(request, 'saved_pic.html', {'photo': photo})'''


'''def user_profile(request):
    user = request.user
    customer = models.Customer.objects.get(Cust_id=user)
    try:
        photo = models.Photos.objects.get(Cust_id=user)
    except models.Photos.DoesNotExist:
        photo = None

    return render(request, 'personal_profile.html', {'customer': customer, 'photo': photo})'''


'''def show_profile_pic(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        user = request.user
        try:
            # Try to get the user's photo from the Photos table
            photo = models.Photos.objects.get(Cust_id=user)
            return render(request, 'pic_display.html', {'photo': photo})
        except models.Photos.DoesNotExist:
            # If the user doesn't have a photo, redirect to the pic_upload.html page
            return redirect('pic_upload')
    else:
        # If the user is not logged in, you can handle it accordingly
        return redirect('login')  # Adjust this based on your authentication logic'''

'''def show_profile_pic(request):
    user = request.user
    try:
        customer = models.Customer.objects.get(Cust_id=user)
        return redirect('showprofilepic')
    except models.Customer.DoesNotExist:
        return render(request, 'pic_upload.html', {})'''

def pp_profile(request):
    user = request.user
    pref = models.PartnerPref.objects.get(Cust_id=user)
    return render(request, 'savedpp.html', {'partner_pref': pref})

def profile(request):
    user = request.user
    try:
        customer = models.Customer.objects.get(Cust_id=user)
        return redirect('user_profile')
    except models.Customer.DoesNotExist:
        return render(request, 'custdet.html', {})
    
def pic(request):
    user = request.user
    try:
        customer = models.Customer.objects.get(Cust_id=user)
        return redirect('profile_pic')
    except models.Customer.DoesNotExist:
        return render(request, 'pic_upload.html', {})

    
def partner_pref(request):
    user = request.user
    try:
        if isinstance(user, User):
            pref = models.PartnerPref.objects.get(Cust_id=user)
            return redirect('pp_profile')
    except:
        return render(request, 'pp.html', {})

def save_partner_pref(request):
    if request.method == 'POST':
        age_min = int(request.POST.get('minAge'))
        age_max = int(request.POST.get('maxAge'))
        #height = int(request.POST.get('height'))
        religion = request.POST.get('religion')
        diet = request.POST.get('diet')
        income = request.POST.get('income')

        user = request.user
        if diet == 'Veg':
            diet = 1
        else:
            diet = 2

        partner_pref = models.PartnerPref.objects.filter(Cust_id=user)
        if len(partner_pref) == 0:
            new_pref = models.PartnerPref(
                Cust_id=user,
                Age_min=age_min,
                Age_max=age_max,
                #Height=height,
                Religion=religion,
                Diet=diet,
                Income=income
            )

            new_pref.save()
        else:
            partner_pref.Age_min=age_min,
            partner_pref.Age_max=age_max,
            #partner_pref[0].Height=height,
            partner_pref.Religion=religion,
            partner_pref.Diet=diet,
            partner_pref.Income=income
            partner_pref[0].save()

    return render(request, 'pp.html', {})


'''def get_matching_customers(request):
    customer_id = request.user
    try:
        partner_preferences = models.PartnerPref.objects.get(Cust_id=customer_id)
    except models.PartnerPref.DoesNotExist:
        print("No match")
        return render(request, 'match.html')
    
    matching_customers = models.Customer.objects.filter(
        #Age_max=partner_preferences.Age_min,
        #Age_max=partner_preferences.Age_max,
        Income=partner_preferences.Income,
        Religion=partner_preferences.Religion,
    )
    print(matching_customers)

    return render(request, 'match.html', {"partner_pref": matching_customers})'''

def get_matching_customers(request):
    customer_id = request.user

    try:
        partner_preferences = models.PartnerPref.objects.get(Cust_id=customer_id)
        #partner_preferences= models.PartnerPref.objects.raw(f"SELECT * FROM WEBSITE_partnerpref WHERE Cust_id_id = {customer_id};")
    except models.PartnerPref.DoesNotExist:
        return render(request, 'match.html', {"partner_pref": []})
    #print(partner_preferences[0])
    # Using raw SQL to perform a JOIN operation
    query = """
    SELECT customer.*
    FROM website_customer AS customer
    JOIN website_partnerpref AS partner_pref ON customer.Cust_id_id = partner_pref.Cust_id_id
    WHERE customer.Income = %s AND customer.Religion = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [partner_preferences.Income, partner_preferences.Religion])
        matching_customers_data = cursor.fetchall()

    
    matching_customers = [models.Customer.objects.get(Cust_id=customer_data[0]) for customer_data in matching_customers_data]

    return render(request, 'match.html', {"partner_pref": matching_customers})

def get_user_activities(request):
    
    user_city = models.Customer.objects.get(Cust_id=request.user).City

    
    user_activities = models.Activities.objects.filter(City=user_city)
    acts = models.Activities.objects.filter(City=user_city).count()

    
    context = {
        'user_activities': user_activities,
        'user_city': user_city,
        'acts': acts
    }

    return render(request, 'ar.html', context)

'''def create_trigger():
    with connection.cursor() as cursor:
        trigger_sql = """
            CREATE TRIGGER delete_married_user_profile
            BEFORE DELETE ON Customer
            FOR EACH ROW
            BEGIN
                DELETE FROM auth_user WHERE id = OLD.Cust_id_id AND Prev_Marital_Status = 'Married';
            END;"""

        cursor.execute(trigger_sql)'''

def delete_customer(request): #procedure
    try:
        user = request.user  # Get the current user
        customer = models.Customer.objects.get(Cust_id=user)
        customer.delete()
        return HttpResponse("Customer deleted successfully.")
    except models.Customer.DoesNotExist:
        return HttpResponse("Customer not found.")
    

def check_marital_status(request):
    try:
        user = request.user
        customer = models.Customer.objects.get(Cust_id=user)

        # Check if the customer is married
        if customer.Prev_Marital_Status == 'Married':
            return HttpResponse("Warning: This user is marked as married. Consider appropriate action.")

        # If not married, you can perform any other actions or return a success message
        return HttpResponse("Marital status is 'Married'. Our website does NOT promote Polygamy.")
    
    except models.Customer.DoesNotExist:
        return HttpResponse("Customer not found.")  

def index(request):
    data = models.Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context) 

def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def display_pic(request):
    user = request.user
    try:
        if isinstance(user, User):
            image = models.PartnerPref.objects.get(id=user)
            return redirect('index')
    except:
        return render(request, 'upload.html', {})
