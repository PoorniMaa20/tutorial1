from django.urls import path
from .views import add_patient,view_patients,edit_patient,delete_patient,user_login,register,user_logout

urlpatterns=[
    path('add-patient/',add_patient,name="add_patient"),
    path('view-patients/',view_patients,name="view_patients"),
    path('edit-patient/<int:id>/',edit_patient,name="edit_patient"),
    path('delete-patient/<int:id>/',delete_patient,name="delete_patient"),
    path('login/',user_login,name="login"),
    path('register/',register,name="register"),
    path('logout/',user_logout,name="logout"),
]