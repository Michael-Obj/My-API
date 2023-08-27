from django.urls import path
from . import views

urlpatterns = [
   path("stafftwo/", views.GetAllStaffs ),
   path("stafftwos", views.RegisterStaff),
   path("staff/<str:staffId>/", views.GetById),
   path("stafflevel/<str:levelId>/", views.GetByStaffId),
   # path("staff/edit/<str:id>/", views.UpdateStaff),
   # path("staff/delete/<str:id>/", views.DeleteStaff)
]