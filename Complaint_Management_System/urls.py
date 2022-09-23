from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('Autoreg/' , views.Autoreg , name="Autoreg"),
    path('Contactus/' , views.Contactus , name="Contactus"),
    path('Displayperfomance/' , views.Displayperfomance , name="Displayperfomance"),

    path('reset_password/' , auth_views.PasswordResetView.as_view() , name = 'reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done" ),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view() , name  = "password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetView.as_view() , name ="password_reset_complete" ),

    
    
]