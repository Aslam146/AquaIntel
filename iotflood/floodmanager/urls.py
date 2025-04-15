from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login,name="login"),
    path('index/',views.index,name="index"),
    path('reg/',views.registration,name="registration"), 
    path('staffdetails/',views.staffdetails,name="staffdetails"), ##staff
    path('staffindex/',views.staffindex,name="staffindex"),
    path('stafflogin/',views.stafflogin,name="stafflogin"),
    path('reset/',views.reset,name="reset"),  ##staff login reset
    path('staff_reset_password/<int:staff_id>/',views.staffreset,name="staffreset"),
    path('user_reset_password/<int:user_id>/',views.user_reset_password,name="user_reset_password"),##userreset
    path('staffuserregistration',views.staffuserregistration,name="staffuserregistration"),    
    path('users/', views.staffusertable, name='staffusertable'),   ##staffside user regisration
    path('users/edit/<int:user_id>/', views.staffuseredit, name='staffuseredit'),
    path('users/delete/<int:user_id>/', views.staffuserdelete, name='staffuserdelete'),  


    path('staffdashboard/',views.staffdashboard,name="staffdashboard"),##for staff login
    path('designation/',views.adddesignation,name="adddesignation"),
    path('department/',views.adddepartment,name="adddepartment"),
    path('staff/', views.staff_table, name='staff_table'),  # Staff List Page
    path('staff/edit/<int:staff_id>/', views.edit_staff, name='edit_staff'),  # Edit Staff
    path('staff/delete/<int:staff_id>/', views.delete_staff, name='delete_staff'),  # Delete Staff
    
    path('water1',views.water1,name="water1"), ##waterlevel-Admin
    path('update-temp-water-level/', views.update_temp_water_level, name='update_temp_water_level'),
    
    path('addwaterstatus',views.addwaterstatus,name="addwaterstatus"),
    path('watertable',views.watertable,name="watertable"), 
    path('wateredit/<int:source_id>/', views.wateredit, name='wateredit'),  # Edit water 
    path('waterdelete/<int:source_id>/', views.waterdelete, name='waterdelete'),

    path('staffwaterlevel',views.staffwaterlevel,name="staffwaterlevel"), ##waterlevel-Staff
    path('staffwatertable',views.staffwatertable,name="staffwatertable"),##for staff view login
    path('staffwateredit/<int:source_id>/', views.staffwateredit, name='staffwateredit'),  # Edit water 
    path('staffwaterdelete/<int:source_id>/', views.staffwaterdelete, name='staffwaterdelete'),
     path('staffwaterstatus',views.staffwaterstatus,name="staffwaterstatus"),

    path('weather/', views.weather, name='weather'), ##weatherprediction-Admin
    path('weathertable/', views.weathertable, name='weathertable'),
    path('weather/edit/<int:weather_id>/',views.weather_edit, name='weather_edit'),
    path('weather/delete/<int:weather_id>/',views.weather_delete, name='weather_delete'),

    path('staffweather/', views.staffweather, name='staffweather'), ##weatherprediction-Staff
    path('staffweathertable/', views.staffweathertable, name='staffweathertable'),
    path('staffweather/edit/<int:weather_id>/', views.staffweather_edit, name='staffweatheredit'),
    path('staffweather/delete/<int:weather_id>/', views.staffweather_delete, name='staffweatherdelete'),


    path('rain/', views.rain1, name='rain1'),##rain intensity-Admin
    path('addrainfalllocations',views.addrainfalllocations,name="addrainfalllocations"),
    path('rainchart',views.rainchart,name="rainchart"),
    path('raintable/', views.raintable, name='raintable'),
    path('raindelete/<int:rainfall_id>/', views.raindelete, name='raindelete'),  # Delete rainfall record
    path('rainedit/<int:rainfall_id>/', views.rainedit, name='rainedit'),

    
    path('staffrain/', views.staffrain1, name='staffrain1'),##rain intensity-staff
    path('staffaddrainfalllocations',views.staffaddrainfalllocations,name="staffaddrainfalllocations"),
    path('staffrainchart',views.staffrainchart,name="staffrainchart"),
    path('staffraintable/', views.staffraintable, name='staffraintable'),
    path('staffraindelete/<int:rainfall_id>/', views.staffraindelete, name='staffraindelete'),  # Delete rainfall record
    path('staffrainedit/<int:rainfall_id>/', views.staffrainedit, name='staffrainedit'),
    
    path('evacuationlocation',views.evacuationlocation,name="evacuationlocation"), ##evacuation Admin
    path('transport',views.transport,name="transport"),
    path('emergencysupply',views.emergencysupply,name="emergencysupply"),
    path('evacuation1',views.evacuation1,name="evacuation1"),##evacuation
    path('evacuationtable/', views.evacuationtable, name='evacuationtable'),
    path('editevacuation/edit/<int:id>/', views.editevacuation, name='editevacuation'),
    path('deleteevacuation/delete/<int:id>/', views.deleteevacuation, name='deleteevacuation'),

    path('staffevacuationlocation',views.staffevacuationlocation,name="staffevacuationlocation"), ##evacuation Staff
    path('stafftransport',views.stafftransport,name="stafftransport"),
    path('staffemergencysupply',views.staffemergencysupply,name="staffemergencysupply"),
    path('staffevacuation1',views.staffevacuation1,name="staffevacuation1"),##evacuation
    path('staffevacuationtable/', views.staffevacuationtable, name='staffevacuationtable'),
    path('staffeditevacuation/edit/<int:id>/', views.staffeditevacuation, name='staffeditevacuation'),
    path('staffdeleteevacuation/delete/<int:id>/', views.staffdeleteevacuation, name='staffdeleteevacuation'),


    path('location',views.location,name="location"), ##camp-location-Admin
    path('camp1',views.camp1,name="camp1"), ## relief camp
    path('amenities',views.amenities,name="amenities"),
    path('reliefcamptable',views.reliefcamptable,name="reliefcamptable"),
    path('editreliefcamp/<int:camp_id>/',views.editreliefcamp,name="editreliefcamp"),
    path('deletereliefcamp/<int:camp_id>/',views.deletereliefcamp,name="deletereliefcamp"),

    path('stafflocation',views.stafflocation,name="stafflocation"), ##camp-location-Staff
    path('staffcamp1',views.staffcamp1,name="staffcamp1"), ## relief camp
    path('staffamenities',views.staffamenities,name="staffamenities"),
    path('staffreliefcamptable',views.staffreliefcamptable,name="staffreliefcamptable"),
    path('staffeditreliefcamp/<int:camp_id>/',views.staffeditreliefcamp,name="staffeditreliefcamp"),
    path('staffdeletereliefcamp/<int:camp_id>/',views.staffdeletereliefcamp,name="staffdeletereliefcamp"),
    

    path('req1',views.req1,name="req1"), ##requirement
    path('reqlist',views.reqlist,name="reqlist"),
    path('editreq',views.editreq,name="editreq"),
    path('deletereq',views.deletereq,name="deletereq"),



    path('ngo1',views.ngo1,name="ngo1"), ###ngo
    path('ngolist',views.ngolist,name="ngolist"),
    path('ngo/edit/<int:ngo_id>/', views.ngoedit, name='ngoedit'),
    path('ngo/delete/<int:ngo_id>/', views.ngodelete, name='ngodelete'),



    path('alert1',views.alert1,name="alert1"), ##alert
    path('alerttable',views.alerttable,name="alerttable"),
    path('alertedit/<int:alert_id>/', views.alertedit, name='alertedit'),
    path('alertdelete/<int:alert_id>/', views.alertdelete, name='alertdelete'),


    path('staffalert',views.staffalert,name="staffalert"), ##alert   staff
    path('staffalerttable',views.staffalerttable,name="staffalerttable"),
    path('staffalertedit/<int:alert_id>/', views.staffalertedit, name='staffalertedit'),
    path('staffalertdelete/<int:alert_id>/', views.staffalertdelete, name='staffalertdelete'),



    path('rescue1',views.rescue1,name="rescue1"), ##rescue management
    path('rescuetable',views.rescuetable,name="rescuetable"),
    path('rescueedit',views.rescueedit,name="rescueedit"),
    path('rescuedelete',views.rescuedelete,name="rescuedelete"),

    
    path('register',views.register,name="register"),
    
    path('userlogin/',views.userlogin,name="userlogin"),  ##userlogin for user
    path('userforgot/',views.userforgot,name="userforgot"),
    path('userindex/',views.userindex,name="userindex"),
    path('adminuserregistration/',views.adminuserregistration,name="adminuserregistration"), ##admin side user registration
    path('adminusertable/', views.adminusertable, name='adminusertable'),
    path('adminusertable/edit/<int:user_id>/', views.adminuseredit, name='adminuseredit'),
    path('adminusertable/delete/<int:user_id>/', views.adminuserdelete, name='adminuserdelete'),  



    path('update_userprofile/',views.update_userprofile,name='update_userprofile'), ##userprofile                                                                   
    path('adminusermail/',views.adminusermail,name='adminusermail'), ##admin userregistration mail
    path('staffusermail/',views.staffusermail,name='staffusermail'),  ##staff userregistration mail
    path('mail/', views.send_mail_page,name="send_mail_page"),
    
    path('sendemaildetailsdispaly/', views.sendemaildetailsdispaly,name="sendemaildetailsdispaly"),
    path('staffsendemaildetailsdispaly/', views.staffsendemaildetailsdispaly,name="staffsendemaildetailsdispaly"),
    
    path('rainfall_chart_data/', views.rainfall_chart_data,name="rainfall_chart_data"),
    path("daily_rainfall_chart_data/", views.daily_rainfall_chart_data, name="daily_rainfall_chart_data"),  
    path("userrainchart/", views.userrainchart, name="userrainchart"),


    path("emergencycontacts/", views.emergencycontacts, name="emergencycontacts"),
    path('useful-resources/', views.useful_resources, name='useful_resources'),
    path('ndrf-sdrf/', views.ndrf_sdrf, name='ndrf_sdrf'),

    
    path("staffemergencycontacts/", views.staffemergencycontacts, name="staffemergencycontacts"),
    path('staffuseful-resources/', views.staffuseful_resources, name='staffuseful_resources'),
    path('staffndrf-sdrf/', views.staffndrf_sdrf, name='staffndrf_sdrf'),

    path("useremergencycontacts/", views.useremergencycontacts, name="useremergencycontacts"),
    path('useruseful-resources/', views.useruseful_resources, name='useruseful_resources'),
    path('safety-tips/', views.safety_tips, name='safety_tips'),
    path('firstaid/', views.firstaid, name='firstaid'),
    path('settings1/', views.settings1, name='settings1'),
    path('settin/', views.settin, name='settin'),
    path('setti/', views.setti, name='setti'),

    path('weather_chart/',views.weather_chart_view, name='weather_chart_view'),
    path('weather_chart_data/', views.weather_chart_data, name='weather_chart_data'),
    path('water-level/', views.water_level_view, name='water_level_view'),
    path('water-chart-data/', views.water_chart_data, name='water_chart_data'),
    path('ngos/', views.ngo_list_view, name='ngo_list'),
    path('alerts/', views.user_alerts, name='user_alerts'),
    path('user_relief_camps/', views.user_relief_camps, name='user_relief_camps'),
    path('userevacuationlist/', views.userevacuationlist, name='userevacuationlist'),

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
]