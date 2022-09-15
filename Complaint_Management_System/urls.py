from django.urls import path
from . import views
urlpatterns = [
    path('',views.login , name="login"),
    
    path('addcomplaint/',views.addcomplaint, name='addcomplaint'),
    path('login/' , views.login , name="login"),
    path('logout/' , views.logout , name="logout"),

    path('maintainancedashboard/' ,views.maintainancedashboard , name='maintainancedashboard'),
    path('itdashboard/' ,views.itdashboard , name='itdashboard'),
    path('electricdashboard/' ,views.electricdashboard , name='electricdashboard'),
    path('messdashboard /' ,views.messdashboard , name='messdashboard'),
    path('showstatus/' ,views.showstatus , name='showstatus'),
    path('status/' , views.status , name="status"),
    path('seen/<str:pk>/' , views.seen , name="seen"),
    path('Deletecomp/<str:pk>/' , views.Deletecomp , name="Deletecomp"),
    
    
]