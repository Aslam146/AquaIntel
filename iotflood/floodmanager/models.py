from django.db import models
#create account
# class UserRegistration(models.Model):  
#     full_name = models.CharField(max_length=255,default= None)  
#     gender = models.CharField(max_length=10,default= None)  # You can use choices if needed (e.g., Male/Female/Other)  
#     address = models.TextField(default= None)  
#     phone_number = models.CharField(max_length=15,default= None)  
#     location = models.CharField(max_length=100,default= None)  
#     username = models.CharField(max_length=150, unique=True,default= None)  
#     email = models.EmailField(unique=True,default= None)  
#     password = models.CharField(max_length=255,default= None)  # Store hashed passwords for security  

#     def __str__(self):  
#         return self.username 
#staff
class Department(models.Model):
    deptname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.deptnamename

class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True)    

class Staff(models.Model):
    
    name = models.CharField(max_length=200)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE,default=None)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=None)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_joining = models.DateField()
    contact = models.CharField(max_length=200,default=None,null=True)
    username = models.CharField(max_length=200,default=None,null=True)
    password = models.CharField(max_length=200,default=None,null=True)
    def __str__(self):
        return f"{self.name} - {self.designation.name if self.designation else 'No Designation'}"
    
##staff user registration
class Staffuserregistration(models.Model):
    # Personal Information
    name = models.CharField(max_length=200,null=True)
    address = models.TextField( null=True)
    dob = models.DateField(null=True)
    sex_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    sex = models.CharField(max_length=6, choices=sex_choices, null=True)
    marital_status_choices = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed')
    ]
    marital_status = models.CharField(max_length=9, choices=marital_status_choices,null=True)
    aadhaar_no = models.CharField(max_length=12,null=True)
    landscape_level = models.CharField(max_length=200, blank=True, null=True)

    # Contact Information
    phone_number = models.CharField(max_length=15, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    house_no = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)

    # Members in the house (if any)
   
    # User Authentication
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return f"{self.name} - {self.username}"

class HouseholdMember(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    familyid = models.ForeignKey(Staffuserregistration, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return f"{self.name} - {self.phone_number}"
    
    ##NGO-Details
class NGO(models.Model):
    ngo_name = models.CharField(max_length=255 )
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    mission = models.TextField()
    website = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.ngo_name

##  adding waterstatus
class WaterStatus(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status
    


class TempWaterLevel(models.Model):
    iot_data_id = models.IntegerField(unique=True,default=0)
    water_level = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.iot_data_id} | Water Level: {self.water_level} at {self.last_updated}"



class TempRainfallData(models.Model):
    iot_data_id = models.IntegerField(unique=True,default=0)
    rainfall_intensity = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.iot_data_id} | Rainfall: {self.rainfall_intensity} at {self.created_at}"




class TempWeatherData(models.Model):
    iot_data_id = models.IntegerField(unique=True,default=0)
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.iot_data_id} | Temp: {self.temperature} | Humidity: {self.humidity}"



class WaterSource(models.Model):
    source_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    water_level = models.FloatField()
    water_status = models.ForeignKey(WaterStatus,on_delete=models.CASCADE,default=None)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source_name} - {self.water_level} meters"

##location for camp
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
from django.db import models

class Amenities(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class ReliefCamp(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    current_occupants = models.PositiveIntegerField(default=0)
    contact_person = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    amenities = models.ForeignKey(Amenities, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
##weather
from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"{self.location} - {self.date}"

##rainfallintesnsity
class RainfallLocation(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
    
class RainfallIntensity(models.Model):
    # rainfall_id = models.CharField(max_length=50)
    location = models.ForeignKey(RainfallLocation, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    rainfall_intensity = models.FloatField()

    def __str__(self):
        return f"{self.rainfall_id} - {self.location.name} ({self.date} {self.time})"
    
##evacuation
class EvacuationLocation(models.Model):              ##evacuationlocation
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class TransportMethod(models.Model):              ##evacuationtransport
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

from django.db import models

class EmergencySupply(models.Model):         ##emergencysupplyevaucation
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class EvacuationRecord(models.Model):
    location = models.ForeignKey(EvacuationLocation, on_delete=models.CASCADE)
    evacuationdate = models.DateField()
    evacuationtime = models.TimeField()
    people_evacuated = models.IntegerField()
    evacuation_center = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    transport_method = models.ForeignKey(TransportMethod, on_delete=models.CASCADE)
    emergency_supply = models.ForeignKey(EmergencySupply, on_delete=models.CASCADE)

    def __str__(self):
        return f"Evacuation at {self.location} on {self.date}"
    



class FloodAlert(models.Model):   ##alertmessage
    LANDSCAPE_CHOICES = [
        ('high', 'High'),
        ('moderate', 'Moderate'),
        ('low', 'Low'),
    ]
    location = models.CharField(max_length=100,default=None)
    alert_msg = models.TextField()
    landscape_level = models.CharField(max_length=10, choices=LANDSCAPE_CHOICES)
    route = models.TextField()
    alert_date = models.DateField()
    

    def __str__(self):
        return f"{self.alert_msg} - {self.alert_date}"