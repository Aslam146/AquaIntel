from django.shortcuts import render, redirect, get_object_or_404
from floodmanager.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.http import JsonResponse
def login(request):
    return render(request,"login.html")

def index(request):
    staffdt=Staff.objects.all()
    totstaff=staffdt.count()
    userdt=Staffuserregistration.objects.all()
    totuser=userdt.count()
    campdt=ReliefCamp.objects.all()
    totcamp=campdt.count()
    totrainfal=RainfallIntensity.objects.all()
    totrainfall=totrainfal.count()
    
    context={
        "totstaff":totstaff,
         "totuser":totuser,
         "totcamp":totcamp,
         "totrainfall":totrainfall
         
    }
    return render(request,"index.html",context)
##staff-management
def staffindex(request):
    staffdt=Staff.objects.all()
    totstaff=staffdt.count()
    userdt=Staffuserregistration.objects.all()
    totuser=userdt.count()
    campdt=ReliefCamp.objects.all()
    totcamp=campdt.count()
    transdt=TransportMethod.objects.all()
    tottrans=transdt.count()
    transdtt=RainfallIntensity.objects.all()
    tottranss=transdtt.count()
    context={
        "totstaff":totstaff,
         "totuser":totuser,
         "totcamp":totcamp,
         "tottrans":tottrans,
          "tottranss":tottranss
    }
    return render(request,"staff/staffindex.html",context)

def registration(request):
    return render(request,"form.html")

def reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            st = Staff.objects.get(email=email)
            uid = st.id
            # Send email without link
            reset_url = f"{settings.SITE_URL}/staff_reset_password/{uid}/"
            
            # Send the email
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, "Password reset instructions have been sent to your email.")
        except Staff.DoesNotExist:
            messages.error(request, "Email not found. Please enter a registered email.")
    return render(request,"staff/reset.html")

def staffreset(request,staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
    except Staff.DoesNotExist:
        messages.error(request, "Invalid password reset link.")
        return redirect("forgot_password")

    if request.method == "POST":
        new_password = request.POST.get("get_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            staff.password = new_password  # This should be hashed (use Django's set_password)
           
            staff.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect("stafflogin")  # Redirect after reset

    # return render(request, "j_reset_password.html", {"staff_id":staff_id}
    return render(request,"staff/staffreset.html", {"staff_id":staff_id})

def staffdashboard(request):
    return render(request,"staff/staffdashboard.html")


from django.template.loader import render_to_string
##admin userregistration -Mail
def staffusermail(request):
    if request.method == 'POST':
        # Collect user profile data from the form
        user_data = {
            'Name': request.POST.get('name'),
            'Address': request.POST.get('address'),
            'Date of Birth': request.POST.get('dob'),
            'Sex': request.POST.get('sex'),
            'Marital Status': request.POST.get('marital_status'),
            'Aadhaar Card No': request.POST.get('aadhaar_no'),
            'Landscape Level': request.POST.get('landscape_level'),
            'Phone Number': request.POST.get('phone_number'),
            'Occupation': request.POST.get('occupation'),
            'House No': request.POST.get('house_no'),
            'Location': request.POST.get('location'),
            'Username': request.POST.get('username'),
            'password': request.POST.get('password'),
            'Email': request.POST.get('mail'),
        }
        # Format the user data as plain text
        message = "\n".join([f"{key}: {value}" for key, value in user_data.items()])
        subject = 'User Profile Details'
        recipient = user_data['Email']
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'User profile sent successfully!')
        except Exception as e:
            messages.error(request, f'Failed to send email: {e}')

        return redirect('staffuserregistration')
    return render(request, 'staff/staffusermail.html')
    

def staffsendemaildetailsdispaly(request):
    userdt=Staffuserregistration.objects.all().last()
    context={
        "user":userdt
    }
    return render(request,"staff/staffusermail.html",context)

def staffuserregistration(request):    
    if request.method == 'POST':
        # Get staff user data from the form
        name = request.POST.get('name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        marital_status = request.POST.get('marital_status')
        aadhaar_no = request.POST.get('aadhaar_no')
        landscape_level = request.POST.get('landscape_level', '')  # Optional
        phone_number = request.POST.get('phone_number')
        occupation = request.POST.get('occupation', '')  # Optional
        house_no = request.POST.get('house_no')
        location = request.POST.get('location')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mail = request.POST.get('useremail')
        # Hash the password before storing it
        # hashed_password = make_password(password)

        # Create the Staffuserregistration object
        staff_user = Staffuserregistration(
            name=name,
            address=address,
            dob=dob,
            sex=sex,
            marital_status=marital_status,
            aadhaar_no=aadhaar_no,
            landscape_level=landscape_level,
            phone_number=phone_number,
            occupation=occupation,
            house_no=house_no,
            location=location,
            username=username,
            password=password,
            email=mail
        )
        staff_user.save()

        # Handle the dynamic household members
        member_names = request.POST.getlist('member_name[]')
        member_phones = request.POST.getlist('member_phone[]')

        # Loop through the submitted member data and save each household member
        for name, phone in zip(member_names, member_phones):
            if name and phone:  # Ensure both name and phone are provided
                HouseholdMember.objects.create(
                    name=name,
                    phone_number=phone,
                    familyid=staff_user  # Link household member to the created staff user
                )

        messages.success(request, "User successfully registered!")
        return redirect('staffsendemaildetailsdispaly')  # Redirect to a success page or the same page

    # If it's a GET request, render the registration page
    return render(request, 'staff/staffuserregistration.html')


def staffusertable(request):
    """View to display all registered users."""
    users = Staffuserregistration.objects.all()  # Fetch all users
    return render(request, "staff/staffusertable.html", {'users': users})


def staffuseredit(request, user_id):
    """View to edit user details."""
    user = get_object_or_404(Staffuserregistration, id=user_id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.address = request.POST.get('address')
        user.phone_number = request.POST.get('phone_number')
        user.username = request.POST.get('username')

        # Only update password if provided
        new_password = request.POST.get('password')
        if new_password:
            user.password = make_password(new_password)  # Hash new password

        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('staffusertable')

    return render(request, "staff/staffuseredit.html", {'user': user})


def staffuserdelete(request, user_id):
    """View to delete a user."""
    user = get_object_or_404(Staffuserregistration, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('staffusertable')

    return render(request, "staff/staffuserdelete.html", {'user': user})

  
def stafflogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the staff member exists with the given username and password
            staff = Staff.objects.get(username=username, password=password)

            # Store staff details in session
            request.session['staff_id'] = staff.id
            request.session['staff_name'] = staff.name

            # Check if the staff member's designation is admin
            if staff.designation.name == 'Admin':  # Assuming 'admin' is the designation name
                return redirect('index')  # Redirect to the admin index page

            # Otherwise, redirect to the staff dashboard
            return redirect('staffindex')

        except Staff.DoesNotExist:
            # If the staff is not found, display an error message
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "staff/stafflogin.html")

def staffdetails(request):
    if request.method == "POST":
        staff_name = request.POST.get('staff_name')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        contact = request.POST.get('contact')
        email = request.POST.get('email', '')  # Optional field
        joining_date = request.POST.get('joining_date')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the password already exists
        if Staff.objects.filter(email=email).exists():
            # If the password exists, return an error message
            des = Designation.objects.all()
            de = Department.objects.all()
            context = {
                'des': des,
                'dep': de,
                'error': "The password already exists. Please choose a different password."
            }
            return render(request, "staffmanagementform.html", context)

        # Save the new staff object
        obj_staff = Staff()
        obj_staff.name = staff_name
        obj_staff.designation_id = designation  # Assuming ForeignKey
        obj_staff.department_id = department  # Assuming ForeignKey
        obj_staff.contact = contact
        obj_staff.email = email
        obj_staff.date_of_joining = joining_date
        obj_staff.username = username
        obj_staff.password = password
        obj_staff.save()

        return redirect('staffdetails')

    # GET request handling
    des = Designation.objects.all()
    de = Department.objects.all()
    context = {
        'des': des,
        'dep': de
    }
    return render(request, "staffmanagementform.html", context)

def adddesignation(request):
    if request.method == "POST":
        desgn = request.POST.get('designation_name')
        if Designation.objects.filter(name=desgn).exists():
            messages.warning(request, "Designation already exists!")
        else:
            objdes = Designation(name=desgn)
            objdes.save()
            messages.success(request, "Designation added successfully!")
    return render(request, "designation.html")

def adddepartment(request):
    if request.method == "POST":
        depart = request.POST.get('department_name')
        if Department.objects.filter(deptname=depart).exists():
            messages.warning(request, "Department already exists!")
        else:
            objdep = Department(deptname=depart)
            objdep.save()
            messages.success(request, "Department added successfully!")
    return render(request, "department.html")
def staff_table(request):
    staff_list = Staff.objects.all()  # Fetch all staff records
    return render(request, "staff_table.html", {"staff_list": staff_list})

def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == "POST":
        staff.staff_id = request.POST['staff_id']
        staff.staff_name = request.POST['staff_name']
        staff.designation_id = request.POST['designation']
        staff.department_id = request.POST['department']
        staff.contact = request.POST['contact']
        staff.email = request.POST['email']
        staff.joining_date = request.POST['joining_date']
        
        staff.save()
        messages.success(request, "Staff details updated successfully.")
        return redirect('staff_table')  # Redirect to staff list

    return render(request, "edit_staff.html", {"staff": staff})
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == "POST":
        staff.delete()
        messages.success(request, "Staff deleted successfully.")
        return redirect('staff_table')

    return render(request, "delete_staff.html", {"staff": staff})

##water-level- admin

def addwaterstatus(request):
    if request.method == 'POST':
        status = request.POST.get('waterstatus')

        if status:
            # Check if status already exists
            if WaterStatus.objects.filter(status=status).exists():
                messages.error(request, "This water status already exists.")
            else:
                WaterStatus.objects.create(status=status)
                messages.success(request, "Water status added successfully.")
        else:
            messages.error(request, "Water status cannot be empty.")

        return redirect('addwaterstatus')

    return render(request,"waterstatus.html")  



import requests
from django.utils.dateparse import parse_datetime
from .models import WaterStatus, TempWaterLevel, WaterSource
from django.shortcuts import render, redirect
from django.contrib import messages

def water1(request):
    # Step 1: Fetch data from API
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]  # First item = latest due to order
            iot_id = int(latest['id'])
            water_level = latest['data']['waterlevel']
            
            # Step 2: Update or create the latest temp value
            TempWaterLevel.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={'water_level': water_level}
            )
    except Exception as e:
        print("API fetch error:", e)

    # Step 3: Get temp value
    wlevel = WaterStatus.objects.all()
    temp_level = TempWaterLevel.objects.last()
    temp_value = temp_level.water_level if temp_level else ''

    # Step 4: Handle form submission
    if request.method == 'POST':
        source_name = request.POST.get('source_name')
        location = request.POST.get('location')
        water_level = request.POST.get('water_level')
        water_status_id = request.POST.get('water_status')

        if not (source_name and water_level):
            messages.error(request, "Please fill in all required fields.")
        else:
            WaterSource.objects.create(
                source_name=source_name,
                location=location,
                water_level=water_level,
                water_status_id=water_status_id,
            )
            messages.success(request, "Water source added successfully.")
            return redirect('watertable')

    context = {
        'wlevel': wlevel,
        'temp_water_level': temp_value
    }
    return render(request, "waterlevel.html", context)


import requests
from django.http import JsonResponse
from .models import TempWaterLevel

def update_temp_water_level(request):
    url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, list) and data:
            latest_entry = data[0]
            latest_data = latest_entry['data']
            water_level = latest_data['waterlevel']
            iot_data_id = int(latest_entry['id'])  # Get the 'id' from the API

            # Check if this id already exists in the TempWaterLevel table
            if not TempWaterLevel.objects.filter(iot_data_id=iot_data_id).exists():
                TempWaterLevel.objects.all().delete()  # Optional: keep only the latest entry
                TempWaterLevel.objects.create(
                    iot_data_id=iot_data_id,
                    water_level=water_level
                )
                return JsonResponse({'status': 'success', 'water_level': water_level})
            else:
                # No update needed since this ID already exists
                existing = TempWaterLevel.objects.get(iot_data_id=iot_data_id)
                return JsonResponse({'status': 'no_change', 'water_level': existing.water_level})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid response'})



def watertable(request):
    water_sources = WaterSource.objects.all()  # Fetch all water sources
    return render(request, "watertable.html", {"water_sources": water_sources})

def wateredit(request, source_id):
    water_source = get_object_or_404(WaterSource, id=source_id)
    wlevel = WaterStatus.objects.all()

    if request.method == 'POST':
        water_source.source_name = request.POST.get('source_name')
        water_source.location = request.POST.get('location')
        water_source.water_level = request.POST.get('water_level')
        water_status_id = request.POST.get('water_status')
        water_source.last_updated = request.POST.get('last_updated')

        if water_status_id:
            water_source.water_status = WaterStatus.objects.get(id=water_status_id)

        water_source.save()
        messages.success(request, "Water source updated successfully.")
        return redirect('watertable')

    context = {"water_source": water_source, "wlevel": wlevel}
    return render(request, "wateredit.html", context)

def waterdelete(request, source_id):
    water_source = get_object_or_404(WaterSource, id=source_id)
    water_source.delete()
    messages.success(request, "Water source deleted successfully.")
    return redirect('watertable')

# staffview waterlevel
import requests
from django.utils.dateparse import parse_datetime
from .models import WaterStatus, TempWaterLevel, WaterSource
from django.shortcuts import render, redirect
from django.contrib import messages

def staffwaterlevel(request):
    # Step 1: Fetch data from API
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]  # First item = latest due to order
            iot_id = int(latest['id'])
            water_level = latest['data']['waterlevel']
            
            # Step 2: Update or create the latest temp value
            TempWaterLevel.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={'water_level': water_level}
            )
    except Exception as e:
        print("API fetch error:", e)

    # Step 3: Get temp value
    wlevel = WaterStatus.objects.all()
    temp_level = TempWaterLevel.objects.last()
    temp_value = temp_level.water_level if temp_level else ''

    # Step 4: Handle form submission
    if request.method == 'POST':
        source_name = request.POST.get('source_name')
        location = request.POST.get('location')
        water_level = request.POST.get('water_level')
        water_status_id = request.POST.get('water_status')

        if not (source_name and water_level):
            messages.error(request, "Please fill in all required fields.")
        else:
            WaterSource.objects.create(
                source_name=source_name,
                location=location,
                water_level=water_level,
                water_status_id=water_status_id,
            )
            messages.success(request, "Water source added successfully.")
            return redirect('staffwatertable')

    context = {
        'wlevel': wlevel,
        'temp_water_level': temp_value
    }
    return render(request, "staff/staffwaterlevel.html", context)



def staffwatertable(request):
     water_sources = WaterSource.objects.all()  # Fetch all water sources
     return render(request, "staff/staffwatertable.html", {"water_sources": water_sources})
    
def staffwateredit(request, source_id):
    water_source = get_object_or_404(WaterSource, id=source_id)
    wlevel = WaterStatus.objects.all()

    if request.method == 'POST':
        water_source.source_name = request.POST.get('source_name')
        water_source.location = request.POST.get('location')
        water_source.water_level = request.POST.get('water_level')
        water_status_id = request.POST.get('water_status')
        water_source.last_updated = request.POST.get('last_updated')

        if water_status_id:
            water_source.water_status = WaterStatus.objects.get(id=water_status_id)

        water_source.save()
        messages.success(request, "Water source updated successfully.")
        return redirect('staffwatertable')

    context = {"water_source": water_source, "wlevel": wlevel}
    return render(request, "staff/staffwateredit.html", context)
    
def staffwaterdelete(request, source_id):
    water_source = get_object_or_404(WaterSource, id=source_id)
    water_source.delete()
    messages.success(request, "Water source deleted successfully.")
    return redirect('staffwatertable')
def staffwaterstatus(request):
     if request.method == 'POST':
        status = request.POST.get('staffwaterstatus')

        if status:
            # Check if status already exists
            if WaterStatus.objects.filter(status=status).exists():
                messages.error(request, "This water status already exists.")
            else:
                WaterStatus.objects.create(status=status)
                messages.success(request, "Water status added successfully.")
        else:
            messages.error(request, "Water status cannot be empty.")

        return redirect('staffwaterstatus')
     return render(request,"staff/staffwaterstatus.html")


#weather - Admin

import requests
from django.utils.dateparse import parse_datetime
from .models import TempWeatherData, Weather
from django.shortcuts import render, redirect
from django.contrib import messages

def weather(request):
    # Step 1: Fetch latest API data
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]
            iot_id = int(latest['id'])
            temperature = latest['data']['temperature']
            humidity = latest['data']['humidity']
            created_at = parse_datetime(latest['created_at'])

            # Step 2: Save to temp table
            TempWeatherData.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={
                    'temperature': temperature,
                    'humidity': humidity,
                    'created_at': created_at
                }
            )
    except Exception as e:
        print("API Fetch Error:", e)

    # Step 3: Get latest values for form
    temp_data = TempWeatherData.objects.last()
    temperature_value = temp_data.temperature if temp_data else ''
    humidity_value = temp_data.humidity if temp_data else ''

    if request.method == 'POST':
        location = request.POST.get('location')
        date = request.POST.get('date')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')

        if not (location and date):
            messages.error(request, "Location and Date are required fields.")
        else:
            Weather.objects.create(
                location=location,
                date=date,
                temperature=temperature if temperature else None,
                humidity=humidity if humidity else None
            )
            messages.success(request, "Weather data added successfully.")
            return redirect('weathertable')

    return render(request, "weather.html", {
        "temperature_value": temperature_value,
        "humidity_value": humidity_value
    })


def weathertable(request):
    weather_data = Weather.objects.all()
    return render(request, "weathertable.html", {"weather_data": weather_data})

def weather_edit(request, weather_id):
    weather_entry = get_object_or_404(Weather, id=weather_id)

    if request.method == 'POST':
        weather_entry.location = request.POST.get('location')
        weather_entry.date = request.POST.get('date')
        weather_entry.temperature = request.POST.get('temperature')
        weather_entry.humidity = request.POST.get('humidity')

        weather_entry.save()
        messages.success(request, "Weather data updated successfully.")
        return redirect('weathertable')

    return render(request, "weatheredit.html", {"prediction": weather_entry})

def weather_delete(request, weather_id):
    weather_entry = get_object_or_404(Weather, id=weather_id)

    if request.method == 'POST':
        weather_entry.delete()
        messages.success(request, "Weather data deleted successfully.")
        return redirect('weathertable')

    return render(request, "weatherdelete.html", {"prediction": weather_entry})

##staff-weather

def staffweather(request):
    # Step 1: Fetch latest API data
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]
            iot_id = int(latest['id'])
            temperature = latest['data']['temperature']
            humidity = latest['data']['humidity']
            created_at = parse_datetime(latest['created_at'])

            # Step 2: Save to temp table
            TempWeatherData.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={
                    'temperature': temperature,
                    'humidity': humidity,
                    'created_at': created_at
                }
            )
    except Exception as e:
        print("API Fetch Error:", e)

    # Step 3: Get latest values for form
    temp_data = TempWeatherData.objects.last()
    temperature_value = temp_data.temperature if temp_data else ''
    humidity_value = temp_data.humidity if temp_data else ''

    if request.method == 'POST':
        location = request.POST.get('location')
        date = request.POST.get('date')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')

        if not (location and date):
            messages.error(request, "Location and Date are required fields.")
        else:
            Weather.objects.create(
                location=location,
                date=date,
                temperature=temperature if temperature else None,
                humidity=humidity if humidity else None
            )
            messages.success(request, "Weather data added successfully.")
            return redirect('staffweathertable')

    return render(request, "staff/staffweather.html", {
        "temperature_value": temperature_value,
        "humidity_value": humidity_value
    })


def staffweathertable(request):
    weather_data = Weather.objects.all()
    return render(request, "staff/staffweathertable.html", {"weather_data": weather_data})

def staffweather_edit(request, weather_id):
    weather_entry = get_object_or_404(Weather, id=weather_id)

    if request.method == 'POST':
        weather_entry.location = request.POST.get('location')
        weather_entry.date = request.POST.get('date')
        weather_entry.temperature = request.POST.get('temperature')
        weather_entry.humidity = request.POST.get('humidity')

        weather_entry.save()
        messages.success(request, "Weather data updated successfully.")
        return redirect('staffweathertable')

    return render(request, "staff/staffweatheredit.html", {"prediction": weather_entry})

def staffweather_delete(request, weather_id):
    weather_entry = get_object_or_404(Weather, id=weather_id)

    if request.method == 'POST':
        weather_entry.delete()
        messages.success(request, "Weather data deleted successfully.")
        return redirect('staffweathertable')

    return render(request, "staff/staffweatherdelete.html", {"prediction": weather_entry})
##rain intensity Admin
def rainchart(request):
    rainfall_data = RainfallIntensity.objects.order_by("date")
    # Formatting data for Chart.js
    labels = []
    data = []

    for entry in rainfall_data:
        month_year = entry.date.strftime("%Y-%m")  # Convert date to "YYYY-MM" format
        labels.append(month_year)
        data.append(entry.rainfall_intensity)
    # Pass data to template
    context = {
        "labels": labels,
        "data": data
    }
    return render(request,"rainchart.html",context)
def rainfall_chart_data(request):
    rainfall_data = RainfallIntensity.objects.order_by("date")

    labels = []
    data = []

    for entry in rainfall_data:
        month_year = entry.date.strftime("%Y-%m")  
        labels.append(month_year)
        data.append(entry.rainfall_intensity)

    return JsonResponse({"labels": labels, "data": data})
from django.db.models import Sum
def daily_rainfall_chart_data(request):
    daily_data = (
        RainfallIntensity.objects
        .values('date')
        .annotate(total_rainfall=Sum('rainfall_intensity'))
        .order_by('date')  # Ensure it's ordered
    )
    labels = [entry['date'].strftime("%Y-%m-%d") for entry in daily_data]  # Convert date to string
    data = [entry['total_rainfall'] for entry in daily_data]
    return JsonResponse({"labels": labels, "data": data})
def addrainfalllocations(request):
    if request.method == "POST":
        location_name = request.POST.get('rainfalllocation_name')
        if RainfallLocation.objects.filter(name=location_name).exists():
            messages.warning(request, "Rainfall location already exists!")
        else:
            obj_location = RainfallLocation(name=location_name)
            obj_location.save()
            messages.success(request, "Rainfall location added successfully!")
    return render(request, "rainfalllocations.html")




import requests
from .models import TempRainfallData, RainfallLocation, RainfallIntensity
from django.utils.dateparse import parse_datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def rain1(request):
    # Step 1: Fetch latest rainfall data from API
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]
            iot_id = int(latest['id'])
            rainfall = latest['data']['rainfall']
            created_at = parse_datetime(latest['created_at'])

            # Step 2: Store in TempRainfallData table
            TempRainfallData.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={
                    'rainfall_intensity': rainfall,
                    'created_at': created_at
                }
            )
    except Exception as e:
        print("API Error:", e)

    # Step 3: Get latest rainfall for form
    temp_rain = TempRainfallData.objects.last()
    rainfall_value = temp_rain.rainfall_intensity if temp_rain else ''

    if request.method == 'POST':
        location_id = request.POST.get('location')
        date = request.POST.get('date')
        time = request.POST.get('time')
        rainfall_intensity = request.POST.get('rainfall_intensity')

        if not (location_id and date and time and rainfall_intensity):
            messages.error(request, "Please fill in all required fields.")
        else:
            location = get_object_or_404(RainfallLocation, id=location_id)
            RainfallIntensity.objects.create(
                location=location,
                date=date,
                time=time,
                rainfall_intensity=rainfall_intensity
            )
            messages.success(request, "Rainfall record added successfully.")
            return redirect('raintable')

    locations = RainfallLocation.objects.all()
    return render(request, "rain.html", {
        "locations": locations,
        "rainfall_value": rainfall_value
    })


# Function to display rainfall table
def raintable(request):
    rainfall_data = RainfallIntensity.objects.all()
    return render(request, "raintable.html", {"rainfall_data": rainfall_data})

# Function to edit rainfall data
def rainedit(request, rainfall_id):
    rainfall = get_object_or_404(RainfallIntensity, id=rainfall_id)
    locations = RainfallLocation.objects.all()
    if request.method == 'POST':
        rainfall.location = get_object_or_404(RainfallLocation, id=request.POST.get('location'))
        rainfall.date = request.POST.get('date')
        rainfall.time = request.POST.get('time')
        rainfall.rainfall_intensity = request.POST.get('rainfall_intensity')
        rainfall.save()
        messages.success(request, "Rainfall record updated successfully.")
        return redirect('raintable')
    return render(request,"rainedit.html", {"rainfall": rainfall, "locations": locations})

# Function to delete rainfall data
def raindelete(request, rainfall_id):
    rainfall = get_object_or_404(RainfallIntensity, id=rainfall_id)

    if request.method == "POST":
        rainfall.delete()
        messages.success(request, "Rainfall record deleted successfully.")
        return redirect('raintable')

    return render(request, "raindelete.html", {"data": rainfall})


##staffrainfallintensity
def staffrainchart(request):
    return render(request,"staff/staffrainchart.html")
def staffaddrainfalllocations(request):
    if request.method == "POST":
        location_name = request.POST.get('rainfalllocation_name')
        if RainfallLocation.objects.filter(name=location_name).exists():
            messages.warning(request, "Rainfall location already exists!")
        else:
            obj_location = RainfallLocation(name=location_name)
            obj_location.save()
            messages.success(request, "Rainfall location added successfully!")
    
    return render(request, "staff/staffrainfalllocations.html")
def staffrain1(request):
    # Step 1: Fetch latest rainfall data from API
    api_url = "https://mybusinesshub.in/iot/get.php?project_id=9&page=1"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()

        if 'data' in json_data and json_data['data']:
            latest = json_data['data'][0]
            iot_id = int(latest['id'])
            rainfall = latest['data']['rainfall']
            created_at = parse_datetime(latest['created_at'])

            # Step 2: Store in TempRainfallData table
            TempRainfallData.objects.update_or_create(
                iot_data_id=iot_id,
                defaults={
                    'rainfall_intensity': rainfall,
                    'created_at': created_at
                }
            )
    except Exception as e:
        print("API Error:", e)

    # Step 3: Get latest rainfall for form
    temp_rain = TempRainfallData.objects.last()
    rainfall_value = temp_rain.rainfall_intensity if temp_rain else ''

    if request.method == 'POST':
        location_id = request.POST.get('location')
        date = request.POST.get('date')
        time = request.POST.get('time')
        rainfall_intensity = request.POST.get('rainfall_intensity')

        if not (location_id and date and time and rainfall_intensity):
            messages.error(request, "Please fill in all required fields.")
        else:
            location = get_object_or_404(RainfallLocation, id=location_id)
            RainfallIntensity.objects.create(
                location=location,
                date=date,
                time=time,
                rainfall_intensity=rainfall_intensity
            )
            messages.success(request, "Rainfall record added successfully.")
            return redirect('staffraintable')

    locations = RainfallLocation.objects.all()
    return render(request, "staff/staffrain.html", {
        "locations": locations,
        "rainfall_value": rainfall_value
    })

# Function to display rainfall table
def staffraintable(request):
    rainfall_data = RainfallIntensity.objects.all()
    return render(request, "staff/staffraintable.html", {"rainfall_data": rainfall_data})

# Function to edit rainfall data
def staffrainedit(request, rainfall_id):
    rainfall = get_object_or_404(RainfallIntensity, id=rainfall_id)
    locations = RainfallLocation.objects.all()

    if request.method == 'POST':
       
        rainfall.location = get_object_or_404(RainfallLocation, id=request.POST.get('location'))
        rainfall.date = request.POST.get('date')
        rainfall.time = request.POST.get('time')
        rainfall.rainfall_intensity = request.POST.get('rainfall_intensity')
        
        rainfall.save()
        messages.success(request, "Rainfall record updated successfully.")
        return redirect('staffraintable')

    return render(request, "staff/staffrainedit.html", {"rainfall": rainfall, "locations": locations})

# Function to delete rainfall data
def staffrainedit(request, rainfall_id):
    rainfall = get_object_or_404(RainfallIntensity, id=rainfall_id)
    locations = RainfallLocation.objects.all()

    if request.method == 'POST':
        rainfall.location = get_object_or_404(RainfallLocation, id=request.POST.get('location'))
        rainfall.date = request.POST.get('date')
        rainfall.time = request.POST.get('time')
        rainfall.rainfall_intensity = request.POST.get('rainfall_intensity')

        rainfall.save()
        messages.success(request, "Rainfall record updated successfully.")
        return redirect('staffraintable')

    return render(request, "staff/staffrainedit.html", {
        "rainfall_data": rainfall,  # Ensure the key matches the template
        "locations": locations
    })


def staffraindelete(request, rainfall_id):
    rainfall = get_object_or_404(RainfallIntensity, id=rainfall_id)
    rainfall.delete()
    messages.success(request, "Rainfall record deleted successfully.")
    return redirect('staffraintable')


##evacuation - Admin
def evacuationlocation(request):
    if request.method == "POST":
        location_name = request.POST.get("evacuationlocation_name")
        
        if location_name:
            # Check if the location already exists
            if EvacuationLocation.objects.filter(name=location_name).exists():
                messages.error(request, "This location already exists.")
            else:
                EvacuationLocation.objects.create(name=location_name)
                messages.success(request, "Evacuation location added successfully.")
        else:
            messages.error(request, "Please enter a valid evacuation location.")
        
        return redirect("evacuationlocation")  
    return render(request,"evacuationlocation.html")
def transport(request):
    if request.method == "POST":
        transport_name = request.POST.get("transport_name")

        if transport_name:
            # Check if the transport method already exists
            if TransportMethod.objects.filter(name=transport_name).exists():
                messages.error(request, "This transport method already exists.")
            else:
                TransportMethod.objects.create(name=transport_name)
                messages.success(request, "Transport method added successfully.")
        else:
            messages.error(request, "Please enter a valid transport method.")

        return redirect("transport") 
    return render(request,"transport.html")
def emergencysupply(request): 
    if request.method == "POST":
        supply_name = request.POST.get("emergencysupply_name")

        if supply_name:
            # Check if the supply already exists
            if EmergencySupply.objects.filter(name=supply_name).exists():
                messages.error(request, "This emergency supply already exists.")
            else:
                EmergencySupply.objects.create(name=supply_name)
                messages.success(request, "Emergency supply added successfully.")
        else:
            messages.error(request, "Please enter a valid emergency supply.")

        return redirect("emergencysupply")  
                        
    return render(request,"emergencysupply.html")
def evacuation1(request):
    if request.method == "POST":
        print("Received POST request:", request.POST)  # Debugging Step

        location_id = request.POST.get("location")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people_evacuated = request.POST.get("people_evacuated")
        evacuation_center = request.POST.get("evacuation_center")
        contact_person = request.POST.get("contact_person")
        contact_number = request.POST.get("contact_number")
        transport_id = request.POST.get("transport_method")
        emergency_id = request.POST.get("emergency")

        if not time:
            messages.error(request, "Time field is required.")
            return redirect("evacuation1")

        if location_id and transport_id and emergency_id and date and time and people_evacuated and evacuation_center and contact_person and contact_number:
            try:
                location = EvacuationLocation.objects.get(id=location_id)
                transport = TransportMethod.objects.get(id=transport_id)
                emergency = EmergencySupply.objects.get(id=emergency_id)

                evacuation = EvacuationRecord.objects.create(
                    location=location,
                    date=date,
                    time=time,
                    people_evacuated=int(people_evacuated),
                    evacuation_center=evacuation_center,
                    contact_person=contact_person,
                    contact_number=contact_number,
                    transport_method=transport,
                    emergency_supply=emergency,
                )
                print("Evacuation record inserted:", evacuation)  # Debugging Step
                messages.success(request, "Evacuation record added successfully.")
            except Exception as e:
                print("Error:", str(e))  # Debugging Step
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Please fill in all required fields.")

        return redirect("evacuation1")

    evacuationlocations = EvacuationLocation.objects.all()
    transports = TransportMethod.objects.all()
    emergencies = EmergencySupply.objects.all()

    return render(request, "evacuation.html", {
        "evacuationlocation": evacuationlocations,
        "transport": transports,
        "emergencysupply": emergencies
    })

def evacuationtable(request):
    evacuations = EvacuationRecord.objects.all()
    context={
        'evacaution':evacuations
    }
    return render(request, "evacuationtable.html",context)

def editevacuation(request, id):
    evacuation = get_object_or_404(EvacuationRecord, id=id)
    if request.method == "POST":
        evacuation.location_id = request.POST.get("location")
        evacuation.date = request.POST.get("date")
        evacuation.time = request.POST.get("time")  # Added time field to update
        evacuation.people_evacuated = request.POST.get("people_evacuated")
        evacuation.transport_method_id = request.POST.get("transport_method")
        evacuation.emergency_supply_id = request.POST.get("emergency_supply")
        evacuation.save()
        messages.success(request, "Evacuation record updated successfully.")
        return redirect("evacuationtable")

    locations = EvacuationLocation.objects.all()
    transports = TransportMethod.objects.all()
    emergency_supplies = EmergencySupply.objects.all()
    return render(request, "editevacuation.html", {
        "evacuation": evacuation,
        "locations": locations,
        "transports": transports,
        "emergency_supplies": emergency_supplies
    })

def deleteevacuation(request, id):
    evacuation = get_object_or_404(EvacuationRecord, id=id)
    if request.method == "POST":
        evacuation.delete()
        messages.success(request, "Evacuation record deleted successfully.")
        return redirect("evacuationtable")
    return render(request, "deleteevacuation.html", {"evacuation": evacuation})



##evacuation - Staff
def staffevacuationlocation(request):
    if request.method == "POST":
        location_name = request.POST.get("evacuationlocation_name")
        
        if location_name:
            # Check if the location already exists
            if EvacuationLocation.objects.filter(name=location_name).exists():
                messages.error(request, "This location already exists.")
            else:
                EvacuationLocation.objects.create(name=location_name)
                messages.success(request, "Evacuation location added successfully.")
        else:
            messages.error(request, "Please enter a valid evacuation location.")
        
        return redirect("staffevacuationlocation")  
    return render(request,"staff/staffevacuationlocation.html")
def stafftransport(request):
    if request.method == "POST":
        transport_name = request.POST.get("transport_name")

        if transport_name:
            # Check if the transport method already exists
            if TransportMethod.objects.filter(name=transport_name).exists():
                messages.error(request, "This transport method already exists.")
            else:
                TransportMethod.objects.create(name=transport_name)
                messages.success(request, "Transport method added successfully.")
        else:
            messages.error(request, "Please enter a valid transport method.")

        return redirect("stafftransport") 
    return render(request,"staff/stafftransport.html")
def staffemergencysupply(request): 
    if request.method == "POST":
        supply_name = request.POST.get("emergencysupply_name")

        if supply_name:
            # Check if the supply already exists
            if EmergencySupply.objects.filter(name=supply_name).exists():
                messages.error(request, "This emergency supply already exists.")
            else:
                EmergencySupply.objects.create(name=supply_name)
                messages.success(request, "Emergency supply added successfully.")
        else:
            messages.error(request, "Please enter a valid emergency supply.")

        return redirect("staffemergencysupply")  
                        
    return render(request,"staff/staffemergencysupply.html")
def staffevacuation1(request):
    if request.method == "POST":
        print("Received POST request:", request.POST)  # Debugging Step

        location_id = request.POST.get("location")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people_evacuated = request.POST.get("people_evacuated")
        evacuation_center = request.POST.get("evacuation_center")
        contact_person = request.POST.get("contact_person")
        contact_number = request.POST.get("contact_number")
        transport_id = request.POST.get("transport_method")
        emergency_id = request.POST.get("emergency")

        if not time:
            messages.error(request, "Time field is required.")
            return redirect("staffevacuation1")

        if location_id and transport_id and emergency_id and date and time and people_evacuated and evacuation_center and contact_person and contact_number:
            try:
                location = EvacuationLocation.objects.get(id=location_id)
                transport = TransportMethod.objects.get(id=transport_id)
                emergency = EmergencySupply.objects.get(id=emergency_id)

                evacuation = EvacuationRecord.objects.create(
                    location=location,
                    date=date,
                    time=time,
                    people_evacuated=int(people_evacuated),
                    evacuation_center=evacuation_center,
                    contact_person=contact_person,
                    contact_number=contact_number,
                    transport_method=transport,
                    emergency_supply=emergency,
                )
                print("Evacuation record inserted:", evacuation)  # Debugging Step
                messages.success(request, "Evacuation record added successfully.")
            except Exception as e:
                print("Error:", str(e))  # Debugging Step
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Please fill in all required fields.")

        return redirect("staffevacuation1")

    evacuationlocations = EvacuationLocation.objects.all()
    transports = TransportMethod.objects.all()
    emergencies = EmergencySupply.objects.all()

    return render(request, "staff/staffevacuation.html", {
        "evacuationlocation": evacuationlocations,
        "transport": transports,
        "emergencysupply": emergencies
    })

def staffevacuationtable(request):
    evacuations = EvacuationRecord.objects.all()
    context={
        'evacaution':evacuations
    }
    return render(request, "staff/staffevacuationtable.html",context)

def staffeditevacuation(request, id):
    evacuation = get_object_or_404(EvacuationRecord, id=id)
    if request.method == "POST":
        evacuation.location_id = request.POST.get("location")
        evacuation.date = request.POST.get("date")
        evacuation.time = request.POST.get("time")  # Added time field to update
        evacuation.people_evacuated = request.POST.get("people_evacuated")
        evacuation.transport_method_id = request.POST.get("transport_method")
        evacuation.emergency_supply_id = request.POST.get("emergency_supply")
        evacuation.save()
        messages.success(request, "Evacuation record updated successfully.")
        return redirect("staffevacuationtable")

    locations = EvacuationLocation.objects.all()
    transports = TransportMethod.objects.all()
    emergency_supplies = EmergencySupply.objects.all()
    return render(request, "staff/staffeditevacuation.html", {
        "evacuation": evacuation,
        "locations": locations,
        "transports": transports,
        "emergency_supplies": emergency_supplies
    })

def staffdeleteevacuation(request, id):
    evacuation = get_object_or_404(EvacuationRecord, id=id)
    if request.method == "POST":
        evacuation.delete()
        messages.success(request, "Evacuation record deleted successfully.")
        return redirect("staffevacuationtable")
    return render(request, "staff/staffdeleteevacuation.html", {"evacuation": evacuation})
##camp-Admin
def location(request):
    if request.method == 'POST':
        location_name = request.POST.get('Location_name')

        if not location_name:
            messages.error(request, "Location name cannot be empty.")
        elif Location.objects.filter(name=location_name).exists():
            messages.error(request, "Location already exists.")
        else:
            Location.objects.create(name=location_name)
            messages.success(request, "Location added successfully.")
            return redirect('location')  # Ensure this URL name exists in your urls.py
    
    return render(request,"location.html")
def amenities(request):
    if request.method == 'POST':
        amenities_name = request.POST.get('amenities_name')

        if not amenities_name:
            messages.error(request, "Amenities name cannot be empty.")
        elif Amenities.objects.filter(name=amenities_name).exists():
            messages.error(request, "Amenities already exists.")
        else:
            Amenities.objects.create(name=amenities_name)
            messages.success(request, "Amenities added successfully.")
            return redirect('amenities')  # Ensure this URL name exists in urls.py
    return render(request,"amenities.html")
def camp1(request):
    locations = Location.objects.all()
    amenities = Amenities.objects.all()

    if request.method == 'POST':
        camp_name = request.POST.get('camp_name')
        location_id = request.POST.get('location')
        capacity = request.POST.get('capacity')
        current_occupants = request.POST.get('current_occupants')
        contact_person = request.POST.get('contact_person')
        contact_number = request.POST.get('contact_number')
        amenities_ids = request.POST.get('amenities')  # Multiple amenities
        remarks = request.POST.get('remarks')

        if not (camp_name and location_id and capacity and contact_person and contact_number):
            messages.error(request, "Please fill in all required fields.")
        else:
            location = get_object_or_404(Location, id=location_id)
            camp = ReliefCamp.objects.create(
                name=camp_name,
                location=location,
                capacity=capacity,
                current_occupants=current_occupants,
                contact_person=contact_person,
                contact_number=contact_number,
                remarks=remarks,
                amenities_id=amenities_ids
            )
            # Assign multiple amenities
            messages.success(request, "Relief camp added successfully.")
            return redirect('reliefcamptable')

    context = {'locations': locations, 'amenities': amenities}
    return render(request, "relief_camp_management.html", context)

def reliefcamptable(request):
    relief_camps = ReliefCamp.objects.all()
    return render(request, "reliefcamptable.html", {"relief_camps": relief_camps})

def editreliefcamp(request, camp_id):
    camp = get_object_or_404(ReliefCamp, id=camp_id)
    locations = Location.objects.all()
    amenities = Amenities.objects.all()

    if request.method == 'POST':
        camp = get_object_or_404(ReliefCamp, id=camp_id)
    
        camp.name = request.POST.get('camp_name')
        location_id = request.POST.get('location')
        camp.capacity = request.POST.get('capacity')
        camp.current_occupants = request.POST.get('current_occupants')
        camp.contact_person = request.POST.get('contact_person')
        camp.contact_number = request.POST.get('contact_number')
        amenities_ids = request.POST.get('amenities')
        camp.remarks = request.POST.get('remarks')

        if location_id:
            camp.location = get_object_or_404(Location, id=location_id)
        
        camp.save()
        messages.success(request, "Relief camp updated successfully.")
        return redirect('reliefcamptable')

    context = {"camp": camp, "locations": locations, "amenities": amenities}
    return render(request, "editreliefcamp.html", context)

def deletereliefcamp(request, camp_id):
    camp = get_object_or_404(ReliefCamp, id=camp_id)
    camp.delete()
    messages.success(request, "Relief camp deleted successfully.")
    return redirect('reliefcamptable')

##camp-Staff
def stafflocation(request):
    if request.method == 'POST':
        location_name = request.POST.get('Location_name')

        if not location_name:
            messages.error(request, "Location name cannot be empty.")
        elif Location.objects.filter(name=location_name).exists():
            messages.error(request, "Location already exists.")
        else:
            Location.objects.create(name=location_name)
            messages.success(request, "Location added successfully.")
            return redirect('stafflocation')  # Ensure this URL name exists in your urls.py
    
    return render(request,"staff/stafflocation.html")
def staffamenities(request):
    if request.method == 'POST':
        amenities_name = request.POST.get('amenities_name')

        if not amenities_name:
            messages.error(request, "Amenities name cannot be empty.")
        elif Amenities.objects.filter(name=amenities_name).exists():
            messages.error(request, "Amenities already exists.")
        else:
            Amenities.objects.create(name=amenities_name)
            messages.success(request, "Amenities added successfully.")
            return redirect('staffamenities')  # Ensure this URL name exists in urls.py
    return render(request,"staff/staffamenities.html")
def staffcamp1(request):
    locations = Location.objects.all()
    amenities = Amenities.objects.all()

    if request.method == 'POST':
        camp_name = request.POST.get('camp_name')
        location_id = request.POST.get('location')
        capacity = request.POST.get('capacity')
        current_occupants = request.POST.get('current_occupants')
        contact_person = request.POST.get('contact_person')
        contact_number = request.POST.get('contact_number')
        amenities_ids = request.POST.get('amenities') # Multiple amenities
        remarks = request.POST.get('remarks')

        if not (camp_name and location_id and capacity and contact_person and contact_number):
            messages.error(request, "Please fill in all required fields.")
        else:
            location = get_object_or_404(Location, id=location_id)
            camp = ReliefCamp.objects.create(
                name=camp_name,
                location=location,
                capacity=capacity,
                current_occupants=current_occupants,
                contact_person=contact_person,
                contact_number=contact_number,
                remarks=remarks,
                amenities_id=amenities_ids
            )
            # Assign multiple amenities
            messages.success(request, "Relief camp added successfully.")
            return redirect('staffreliefcamptable')

    context = {'locations': locations, 'amenities': amenities}
    return render(request, "staff/staffrelief_camp_management.html", context)

def staffreliefcamptable(request):
    relief_camps = ReliefCamp.objects.all()
    return render(request, "staff/staffcamptable.html", {"relief_camps": relief_camps})

def staffeditreliefcamp(request, camp_id):
    camp = get_object_or_404(ReliefCamp, id=camp_id)
    locations = Location.objects.all()
    amenities = Amenities.objects.all()

    if request.method == 'POST':
        camp = get_object_or_404(ReliefCamp, id=camp_id)
    
        camp.name = request.POST.get('camp_name')
        location_id = request.POST.get('location')
        camp.capacity = request.POST.get('capacity')
        camp.current_occupants = request.POST.get('current_occupants')
        camp.contact_person = request.POST.get('contact_person')
        camp.contact_number = request.POST.get('contact_number')
        amenities_ids = request.POST.get('amenities')
        camp.remarks = request.POST.get('remarks')

        if location_id:
            camp.location = get_object_or_404(Location, id=location_id)
        
        camp.save()
        messages.success(request, "Relief camp updated successfully.")
        return redirect('staffreliefcamptable')

    context = {"camp": camp, "locations": locations, "amenities": amenities}
    return render(request, "staff/staffeditreliefcamp.html", context)

def staffdeletereliefcamp(request, camp_id):
    camp = get_object_or_404(ReliefCamp, id=camp_id)
    camp.delete()
    messages.success(request, "Relief camp deleted successfully.")
    return redirect('staffreliefcamptable')

##requirements
def req1(request):
    return render(request,"requirements.html")
def reqlist(request):
    return render(request,"requirementlist.html")
def editreq(request):
    return render(request,"edit_requirement.html")
def deletereq(request):
    return render(request,"delete_requirement.html")
##ngo
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import NGO

def ngo1(request):

    """Render the main NGO page."""
    """Create a new NGO record."""
    if request.method == "POST":
        ngo_name = request.POST['ngo_name']
        contact_person = request.POST['contact_person']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        mission = request.POST['mission']
        website = request.POST.get('website', '')

        # Create a new NGO instance and save it
        NGO.objects.create(
            ngo_name=ngo_name,
            contact_person=contact_person,
            email=email,
            phone_number=phone_number,
            address=address,
            mission=mission,
            website=website
        )
        messages.success(request, "NGO added successfully.")
        return redirect('ngolist')


    return render(request, "ngo.html")

def ngolist(request):
    """Fetch and display all NGO records."""
    ngo_list = NGO.objects.all()
    return render(request, "ngo_list.html", {"ngo_list": ngo_list})

def ngoedit(request, ngo_id):
    """Edit NGO details."""
    ngo = get_object_or_404(NGO, id=ngo_id)

    if request.method == "POST":
        ngo.ngo_name = request.POST['ngo_name']
        ngo.contact_person = request.POST['contact_person']
        ngo.email = request.POST['email']
        ngo.phone_number = request.POST['phone_number']
        ngo.address = request.POST['address']
        ngo.mission = request.POST['mission']
        ngo.website = request.POST.get('website', '')  # Optional field
        
        ngo.save()
        messages.success(request, "NGO details updated successfully.")
        return redirect('ngolist')  # Redirect to NGO list

    return render(request, "edit_ngo.html", {"ngo": ngo})

def ngodelete(request, ngo_id):
    """Delete an NGO record."""
    ngo = get_object_or_404(NGO, id=ngo_id)

    if request.method == "POST":
        ngo.delete()
        messages.success(request, "NGO deleted successfully.")
        return redirect('ngolist')

    return render(request, "delete_ngo.html", {"ngo": ngo})



##alert
import requests
def alert1(request):
    if request.method == "POST":
        alert_msg = request.POST.get("alert_msg")
        location = request.POST.get("location")
        landscape_level = request.POST.get("landscape_level")
        alert_date = request.POST.get("alert_date")
        route = request.POST["route"]
        alert_date = request.POST["alert_date"]
        FloodAlert.objects.create(
            alert_msg=alert_msg,
            landscape_level=landscape_level,
            route=route,
            alert_date=alert_date,
            location=location
        )
        # Replace with actual phone numbers (comma-separated if multiple)
        recipient_numbers = "6235608419" 
        # Fast2SMS API Endpoint
        url = "https://www.fast2sms.com/dev/bulkV2"

        # Your Fast2SMS API Key (replace with a valid key)
        api_key = "PNG6d2aI3hAXD7neZzcqC4YWmlQHu0LTk5Jx9sVbwBEji8pgrU2EKjhXTgcQMnydk9DwxiNBHbqL16a8"

        # Constructing the message
        message = f"Flood Alert!\nMessage: {alert_msg}\nLocation: {location}\nLandscape Level: {landscape_level}\nDate: {alert_date}\nRoute:{route}"

        # Request payload
        payload = {
            "route": "q",
            "message": message,
            "numbers": recipient_numbers,
            "flash": "0"
        }

        # Headers
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json"
        }

        # Sending the SMS request
        response = requests.post(url, json=payload, headers=headers)

        # Check response
        if response.status_code == 200:
            messages.success(request, "Alert message sent successfully via SMS!")
        else:
            messages.error(request, "Failed to send SMS. Please try again.")

        
        return redirect("alerttable")
    
    return render(request, "alert.html")

def alerttable(request):
    alerts = FloodAlert.objects.all()
    return render(request, "alerttable.html", {"alerts": alerts})

def alertedit(request, alert_id):
    alert = get_object_or_404(FloodAlert, id=alert_id)
    if request.method == "POST":
        alert.alert_msg = request.POST["alert_msg"]
        alert.landscape_level = request.POST["landscape_level"]
        alert.route = request.POST["route"]
        alert.alert_date = request.POST["alert_date"]
        alert.save()
        messages.success(request, "Flood alert updated successfully!")
        return redirect("alerttable")
    
    return render(request, "alertedit.html", {"alert": alert})

def alertdelete(request, alert_id):
    alert = get_object_or_404(FloodAlert, id=alert_id)
    if request.method == "POST":
        alert.delete()
        messages.success(request, "Flood alert deleted successfully!")
        return redirect("alerttable")
    
    return render(request, "alertdelete.html", {"alert": alert})

def staffalert(request):
    if request.method == "POST":
        alert_msg = request.POST.get("alert_msg")
        location = request.POST.get("location")
        landscape_level = request.POST.get("landscape_level")
        alert_date = request.POST.get("alert_date")
        route = request.POST["route"]
        alert_date = request.POST["alert_date"]
        FloodAlert.objects.create(
            alert_msg=alert_msg,
            landscape_level=landscape_level,
            route=route,
            alert_date=alert_date,
            location=location
        )
        # Replace with actual phone numbers (comma-separated if multiple)
        recipient_numbers = "6235608419"
        # Fast2SMS API Endpoint
        url = "https://www.fast2sms.com/dev/bulkV2"

        # Your Fast2SMS API Key (replace with a valid key)
        api_key = "PNG6d2aI3hAXD7neZzcqC4YWmlQHu0LTk5Jx9sVbwBEji8pgrU2EKjhXTgcQMnydk9DwxiNBHbqL16a8"

        # Constructing the message
        message = f"Flood Alert!\nMessage: {alert_msg}\nLocation: {location}\nLandscape Level: {landscape_level}\nDate: {alert_date}\nRoute:{route}"

        # Request payload
        payload = {
            "route": "q",
            "message": message,
            "numbers": recipient_numbers,
            "flash": "0"
        }

        # Headers
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json"
        }

        # Sending the SMS request
        response = requests.post(url, json=payload, headers=headers)

        # Check response
        if response.status_code == 200:
            messages.success(request, "Alert message sent successfully via SMS!")
        else:
            messages.error(request, "Failed to send SMS. Please try again.")

        
        return redirect("staffalerttable")
    
    
    return render(request, "staff/staffalert.html")

def staffalerttable(request):
    alerts = FloodAlert.objects.all()
    return render(request, "staff/staffalerttable.html", {"alerts": alerts})

def staffalertedit(request, alert_id):
    alert = get_object_or_404(FloodAlert, id=alert_id)
    if request.method == "POST":
        alert.alert_msg = request.POST["alert_msg"]
        alert.landscape_level = request.POST["landscape_level"]
        alert.route = request.POST["route"]
        alert.alert_date = request.POST["alert_date"]
        alert.save()
        messages.success(request, "Flood alert updated successfully!")
        return redirect("staffalerttable")
    
    return render(request, "staff/staffalertedit.html", {"alert": alert})

def staffalertdelete(request, alert_id):
    alert = get_object_or_404(FloodAlert, id=alert_id)
    if request.method == "POST":
        alert.delete()
        messages.success(request, "Flood alert deleted successfully!")
        return redirect("staffalerttable")
    
    return render(request, "staff/staffalertdelete.html", {"alert": alert})

##rescue
def rescue1(request):
    return render(request,"rescue.html")
def rescuetable(request):
    return render(request,"rescuetable.html")
def rescueedit(request):
    return render(request,"rescueedit.html")
def rescuedelete(request):
    return render(request,"rescuedelete.html")



def forgot(request):
    return render(request,"forgot.html")

def register(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        phone_number = request.POST["phone_number"]
        location = request.POST["location"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if username or email already exists
        if UserRegistration.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        # Save user data
        user = UserRegistration(
            full_name=full_name,
            gender=gender,
            address=address,
            phone_number=phone_number,
            location=location,
            username=username,
            email=email,
            password=password  # Ideally, hash the password using Django's User model for security
        )
        user.save()
        
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")

    return render(request, "staff/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = UserRegistration.objects.get(username=username, password=password)
            messages.success(request, "Login successful!")
            return redirect('index')
        except:
            messages.error(request, "Invalid username or password!")
            return redirect('user_login')
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the staff member exists with the given username and password
            user = Staffuserregistration.objects.get(username=username, password=password)
            request.session['loginuser'] = user.id 
            
            # Store staff details in session
           
            # Otherwise, redirect to the staff dashboard
          
            messages.success(request, "Login successful!")
            return redirect('userindex')

        except:
            # If the staff is not found, display an error message
            messages.error(request, "Invalid username or password. Please try again.")
            # return redirect('userindex')
    

    return render(request, "user/userlogin.html")
def userforgot(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            st =  Staffuserregistration.objects.get(email=email)
            uid = st.id
            # Send email without link
            reset_url = f"{settings.SITE_URL}/user_reset_password/{uid}/"
            
            # Send the email
            send_mail(
                subject="Password Reset Request",
                message=f"Click the link below to reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            messages.success(request, "Password reset instructions have been sent to your email.")
        except  Staffuserregistration.DoesNotExist:
            messages.error(request, "Email not found. Please enter a registered email.")
    

    return render(request, "user/userforgot.html")
def user_reset_password(request,user_id):
    try:
        user = Staffuserregistration.objects.get(id=user_id)
    except Staffuserregistration.DoesNotExist:
        messages.error(request, "Invalid password reset link.")
        return redirect("forgot_password")

    if request.method == "POST":
        new_password = request.POST.get("get_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            user.password = new_password  # This should be hashed (use Django's set_password)
           
            user.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect("login")  # Redirect after reset

    # return render(request, "j_reset_password.html", {"staff_id":staff_id}
    return render(request,"user/userreset.html", {"user_id":user_id})

def userbase(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
        'userlogid':userlogid,
        'usernm':usernm
    }
    return render(request, "user/userbase.html",context)
def userindex(request):
    userid = request.session['loginuser']
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
        'userlogid':userlogid,
        'usernm':usernm
    }
    return render(request, "user/userindex.html",context)

def adminuserregistration(request):
    if request.method == 'POST':
        # Get staff user data from the form
        name = request.POST.get('name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        marital_status = request.POST.get('marital_status')
        aadhaar_no = request.POST.get('aadhaar_no')
        landscape_level = request.POST.get('landscape_level', '')  # Optional
        phone_number = request.POST.get('phone_number')
        occupation = request.POST.get('occupation', '')  # Optional
        house_no = request.POST.get('house_no')
        location = request.POST.get('location')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email  = request.POST.get('useremail')
        
        # Hash the password before storing it
        
        # Create the Staffuserregistration object
        staff_user = Staffuserregistration.objects.create(
            name=name,
            address=address,
            dob=dob,
            sex=sex,
            marital_status=marital_status,
            aadhaar_no=aadhaar_no,
            landscape_level=landscape_level,
            phone_number=phone_number,
            occupation=occupation,
            house_no=house_no,
            location=location,
            username=username,
            password=password,
            email=email # Store hashed password
        )

        # Handle the dynamic household members
        member_names = request.POST.getlist('member_name[]')
        member_phones = request.POST.getlist('member_phone[]')

        # Save each household member
        for m_name, m_phone in zip(member_names, member_phones):
            if m_name and m_phone:  # Ensure both name and phone are provided
                HouseholdMember.objects.create(
                    name=m_name,
                    phone_number=m_phone,
                    familyid=staff_user  # Link household member to staff user
                )

        messages.success(request, "User successfully registered!")
        return redirect('sendemaildetailsdispaly')  # Redirect to the user table page

    return render(request, "adminuserregistration.html")

def sendemaildetailsdispaly(request):
    userdt=Staffuserregistration.objects.all().last()
    context={
        "user":userdt
    }
    return render(request,"adminusermail.html",context)

def adminusertable(request):
    """View to display all registered users."""
    users = Staffuserregistration.objects.all()  # Fetch all users
    usb=HouseholdMember.objects.all()
    return render(request, "adminusertable.html", {'users': users,'usb':usb})


def adminuseredit(request, user_id):
    """View to edit user details."""
    user = get_object_or_404(Staffuserregistration, id=user_id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.address = request.POST.get('address')
        user.phone_number = request.POST.get('phone_number')
        user.username = request.POST.get('username')

        # Only update password if provided
        new_password = request.POST.get('password')
        if new_password:
            user.password = make_password(new_password)  # Hash new password

        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('adminusertable')

    return render(request, "adminuseredit.html", {'user': user})


def adminuserdelete(request, user_id):
    """View to delete a user."""
    user = get_object_or_404(Staffuserregistration, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('adminusertable')

    return render(request, "adminuserdelete.html", {'user': user})


##mail
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "mail.html", context)

##user-profile
def update_userprofile(request):
    """Handle user profile update."""
    
    # Fetch the logged-in user's ID from the session
    userid = request.session.get('loginuser')  # Using `get` to avoid KeyError if the key is missing
    
    if not userid:
        # If the user is not logged in, redirect to login page
        messages.error(request, "You must be logged in to update your profile.")
        return redirect('login')  # Replace with the actual login page URL name
    
    userlogid = get_object_or_404(Staffuserregistration, id=userid)
    
    if request.method == 'POST':
        # Get form data to update user profile
        userlogid.name = request.POST.get('name', userlogid.name)
        userlogid.address = request.POST.get('address', userlogid.address)
        userlogid.phone_number = request.POST.get('phone_number', userlogid.phone_number)
        userlogid.username = request.POST.get('username', userlogid.username)

        # Update password if provided
        new_password = request.POST.get('password')
        if new_password:
            userlogid.password = new_password  # Hash the new password

        # Save the updated user profile
        userlogid.save()
        
        # Show success message
        messages.success(request, "Your profile has been updated successfully.")
        
        # Redirect to the profile page (or another page if needed)
        return redirect('update_userprofile')  # You can adjust this redirect as per your view's name
    
    # Context data for the profile page
    usernm=userlogid.name
    context = {
        'userlogid': userlogid,
          'usernm':usernm

    }

    return render(request, "user/userprofile.html", context)

from django.template.loader import render_to_string
##admin userregistration -Mail
def adminusermail(request):
    if request.method == 'POST':
        # Collect user profile data from the form
        user_data = {
            'Name': request.POST.get('name'),
            'Address': request.POST.get('address'),
            'Date of Birth': request.POST.get('dob'),
            'Sex': request.POST.get('sex'),
            'Marital Status': request.POST.get('marital_status'),
            'Aadhaar Card No': request.POST.get('aadhaar_no'),
            'Landscape Level': request.POST.get('landscape_level'),
            'Phone Number': request.POST.get('phone_number'),
            'Occupation': request.POST.get('occupation'),
            'House No': request.POST.get('house_no'),
            'Location': request.POST.get('location'),
            'Username': request.POST.get('username'),
            'password': request.POST.get('password'),
            'Email': request.POST.get('mail'),
        }
        # Format the user data as plain text
        message = "\n".join([f"{key}: {value}" for key, value in user_data.items()])
        subject = 'User Profile Details'
        recipient = user_data['Email']
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'User profile sent successfully!')
        except Exception as e:
            messages.error(request, f'Failed to send email: {e}')
        return redirect('adminuserregistration')
    return render(request, 'adminusermail.html')
    
def userrainchart(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }

      
    return render(request, 'user/userrainchart.html',context)

import requests
def send_alert_sms(request):               ###smsapi
    if request.method == "POST":
        alert_msg = request.POST.get("alert_msg")
        location = request.POST.get("location")
        landscape_level = request.POST.get("landscape_level")
        alert_date = request.POST.get("alert_date")
        route = request.POST["route"]
        alert_date = request.POST["alert_date"]
        FloodAlert.objects.create(
            alert_msg=alert_msg,
            landscape_level=landscape_level,
            route=route,
            alert_date=alert_date
        )
        # Replace with actual phone numbers (comma-separated if multiple)
        recipient_numbers = "9876543210"

        # Fast2SMS API Endpoint
        url = "https://www.fast2sms.com/dev/bulkV2"

        # Your Fast2SMS API Key (replace with a valid key)
        api_key = "PNG6d2aI3hAXD7neZzcqC4YWmlQHu0LTk5Jx9sVbwBEji8pgrU2EKjhXTgcQMnydk9DwxiNBHbqL16a8"

        # Constructing the message
        message = f"Flood Alert!\nMessage: {alert_msg}\nLocation: {location}\nLandscape Level: {landscape_level}\nDate: {alert_date}"

        # Request payload
        payload = {
            "route": "q",
            "message": message,
            "numbers": recipient_numbers,
            "flash": "0"
        }

        # Headers
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json"
        }

        # Sending the SMS request
        response = requests.post(url, json=payload, headers=headers)

        # Check response
        if response.status_code == 200:
            messages.success(request, "Alert message sent successfully via SMS!")
        else:
            messages.error(request, "Failed to send SMS. Please try again.")

        return redirect("alert1")  # Redirect back to form page

    return render(request, "alert.html")  




def emergencycontacts(request):
    return render(request, 'emergencycontacts.html')


def useful_resources(request):
    return render(request, 'useful_resources.html')
def ndrf_sdrf(request):
    return render(request, 'ndrf_sdrf.html')

def staffemergencycontacts(request):
    return render(request, 'staff/staffemergencycontacts.html')


def staffuseful_resources(request):
    return render(request, 'staff/staffuseful_resources.html')
def staffndrf_sdrf(request):
    return render(request, 'staff/ndrf_sdrf.html')


def useremergencycontacts(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    
    return render(request, 'user/useremergencycontacts.html',context)


def useruseful_resources(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    return render(request, 'user/useruseful_resources.html',context)

def safety_tips(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    return render(request, 'user/safety_tips.html',context)

def firstaid(request):
    userid = request.session.get('loginuser')
    userlogid=Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    return render(request, 'user/firstaid.html',context)
def settings1(request):
    userid = request.session.get('loginuser')
    userlogid = Staffuserregistration.objects.get(id=userid)
    usernm = userlogid.name
    context = {
        'userlogid': userlogid,
        'usernm': usernm
    }
    return render(request, 'user/settings.html', context)

def settin(request):
    
    return render(request, 'settin.html')



def setti(request):
    
    return render(request, 'staff/setti.html')



def weather_chart_data(request):
    weather_data = Weather.objects.order_by('date')
    labels = [entry.date.strftime('%Y-%m-%d') for entry in weather_data]
    temperature = [entry.temperature for entry in weather_data]
    humidity = [entry.humidity for entry in weather_data]

    return JsonResponse({
        'labels': labels,
        'temperature': temperature,
        'humidity': humidity
    })

def weather_chart_view(request):
    userid = request.session.get('loginuser')
    userlogid = Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    return render(request, 'user/weather_chart.html',context)


def water_level_view(request):
    userid = request.session.get('loginuser')
    userlogid = Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    context={
          'userlogid':userlogid,
        'usernm':usernm
    

    }
    return render(request, 'user/waterlevelchart.html',context)

def water_chart_data(request):
    water_sources = WaterSource.objects.all()
    data = {
        "labels": [f"{source.source_name} - {source.location}" for source in water_sources],
        "water_level": [source.water_level for source in water_sources],
        "timestamps": [source.last_updated.strftime('%Y-%m-%d %H:%M:%S') for source in water_sources]
    }
    return JsonResponse(data)

# def ngo_list_view(request):
#     userid = request.session.get('loginuser')
#     userlogid = Staffuserregistration.objects.get(id=userid)
#     usernm=userlogid.name
#     context={
#           'userlogid':userlogid,
#         'usernm':usernm
    

#     }
#     ngos = NGO.objects.all()  # Fetch all NGO records from the database
#     return render(request, 'user/ngo_list.html', {'ngos': ngos},context)
def ngo_list_view(request):
    userid = request.session.get('loginuser')

    # Ensure userid is valid before querying
    if userid:
        userlogid = Staffuserregistration.objects.get(id=userid)
        usernm = userlogid.name
    else:
        userlogid = None
        usernm = None

    ngos = NGO.objects.all()  # Fetch all NGO records

    # Combine both context dictionaries
    context = {
        'userlogid': userlogid,
        'usernm': usernm,
        'ngos': ngos  # Add NGOs to the context
    }

    return render(request, 'user/ngo_list.html', context)


def user_alerts(request): ##user
    """Show flood alerts specific to the logged-in staff user"""
    try:
        # Get the logged-in user's details
        userid=request.session.get('loginuser')
        staff_user = Staffuserregistration.objects.get(id=userid)
        user_location = staff_user.location
        user_landscape_level = staff_user.landscape_level
        userid = request.session.get('loginuser')
        userlogid = Staffuserregistration.objects.get(id=userid)
        usernm=userlogid.name
       
        # Filter alerts based on the user's location and landscape level
        alerts = FloodAlert.objects.filter(location=user_location, landscape_level=user_landscape_level)
        context={
            'userlogid':userlogid,
            'usernm':usernm,
        'alerts': alerts

        }
        return render(request, 'user/alerts.html',context)
    
    except Staffuserregistration.DoesNotExist:
        return render(request, 'user/alerts.html', {'alerts': [], 'error': "User not found in staff records."})
    
    
def user_relief_camps(request):
    userid = request.session.get('loginuser')
    userlogid = Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name

    relief_camps = ReliefCamp.objects.select_related('location', 'amenities').all()
    return render(request, 'user/user_relief_camp_list.html', {'relief_camps': relief_camps,'userlogid':userlogid,
            'usernm':usernm,
        })


def userevacuationlist(request):
    userid = request.session.get('loginuser')
    userlogid = Staffuserregistration.objects.get(id=userid)
    usernm=userlogid.name
    evacuation_records = EvacuationRecord.objects.all()
    return render(request, 'user/userevacuationlist.html', {'evacuation_records': evacuation_records,'userlogid':userlogid,
            'usernm':usernm,})

