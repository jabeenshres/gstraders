from .views import LoginView, LogoutView
from django.urls import path


app_name = 'accounts'

urlpatterns=[
    #login and logout included 
    path("",LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),



    # path('signup/',SignUpView.as_view(),name='signup'),

    # path("profile/create/", EmployeeProfileAddView.as_view(),name='create'),
    # path('profile/list/', UserListView.as_view(), name='list'),
    # path('profile/update/<int:pk>', UserProfileUpdateView.as_view(), name='update'),
    
    # path('profile/changepassword/<int:pk>', SetPasswordView.as_view(), name='change-password' ),
    # path('profile/delete/<int:pk>', UserProfileDeleteView.as_view(), name='delete' ),


]
