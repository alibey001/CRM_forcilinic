from django.urls import path
from .views import *

urlpatterns = [
    # >>>>>>>>>> CRUD Employee Model <<<<<<<<<< #
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee-items/', CreateAllEmployeeItems.as_view()),
    path('update-employee-items/<int:pk>/', UpdateAllEmployeeItems.as_view()),
    path('delete-employee-items/<int:pk>/', DeleteAllEmployeeItems.as_view()),


    # >>>>>>>>>> CRUD Patient Model <<<<<<<<<< #
    path('get-patient-items/', GetAllPatientItems.as_view()),
    path('create-patient-items/', CreateAllPatientItems.as_view()),
    path('update-patient-items/<int:pk>/', UpdateAllPatientItems.as_view()),
    path('delete-patient-items/<int:pk>/', DeleteAllPatientItems.as_view()),


    # >>>>>>>>>> CRUD Room Model <<<<<<<<<< #
    path('get-room-items/', GetAllRoomItems.as_view()),
    path('create-room-items/', CreateAllRoomItems.as_view()),
    path('update-room-items/<int:pk>/', UpdateAllRoomItems.as_view()),
    path('delete-room-items/<int:pk>/', DeleteAllRoomItems.as_view()),


    # >>>>>>>>>> CRUD Payment Model <<<<<<<<<< #
    path('get-payment-items/', GetAllPaymentItems.as_view()),
    path('create-payment-items/', CreateAllPaymentItems.as_view()),
    path('update-payment-items/<int:pk>/', UpdateAllPaymentItems.as_view()),
    path('delete-payment-items/<int:pk>/', DeleteAllPaymentItems.as_view()),


    # >>>>>>>>>> CRUD Comment Model <<<<<<<<<< #
    path('get-comment-items/', GetAllCommentItems.as_view()),
    path('create-comment-items/', CreateAllCommentItems.as_view()),
    path('update-comment-items/<int:pk>/', UpdateAllCommentItems.as_view()),
    path('delete-comment-items/<int:pk>/', DeleteAllCommentItems.as_view()),


    # >>>>>>>>>> CRUD Income Model <<<<<<<<<< #
    path('get-income-items/', GetAllIncomeItems.as_view()),
    path('create-income-items/', CreateAllIncomeItems.as_view()),
    path('update-income-items/<int:pk>/', UpdateAllIncomeItems.as_view()),
    path('delete-income-items/<int:pk>/', DeleteAllIncomeItems.as_view()),


    # >>>>>>>>>> CRUD Employee Model <<<<<<<<<< #
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee-items/', GetAllEmployeeItems.as_view()),
    path('update-employee-items/<int:pk>/', GetAllEmployeeItems.as_view()),
    path('delete-employee-items/<int:pk>/', GetAllEmployeeItems.as_view()),


    # >>>>>>>>>> CRUD Ravenue Model <<<<<<<<<< #
    path('get-ravenue-items/', GetAllRavenueItems.as_view()),
    path('create-ravenue-items/', CreateAllRavenueItems.as_view()),
    path('update-ravenue-items/<int:pk>/', UpdateAllRavenueItems.as_view()),
    path('delete-ravenue-items/<int:pk>/', DeleteAllRavenueItems.as_view()),


    # >>>>>>>>>> CRUD Cassa Model <<<<<<<<<< #
    path('get-cassa-items/', GetAllCassaItems.as_view()),
    path('create-cassa-items/', CreateAllCassaItems.as_view()),
    path('update-cassa-items/<int:pk>/', UpdateAllCassaItems.as_view()),
    path('delete-cassa-items/<int:pk>/', DeleteAllCassaItems.as_view()),


    # >>>>>>>>>> CRUD Operation Model <<<<<<<<<< #
    path('get-operation-items/', GetAllOperationItems.as_view()),
    path('create-operation-items/', CreateAllOperationItems.as_view()),
    path('update-operation-items/<int:pk>/', UpdateAllOperationItems.as_view()),
    path('delete-operation-items/<int:pk>/', DeleteAllOperationItems.as_view()),


    # >>>>>>>>>> CRUD Department Model <<<<<<<<<< #
    path('get-department-items/', GetAllDepartmentItems.as_view()),
    path('create-department-items/', CreateAllDepartmentItems.as_view()),
    path('update-department-items/<int:pk>/', UpdateAllDepartmentItems.as_view()),
    path('delete-department-items/<int:pk>/', DeleteAllDepartmentItems.as_view()),


    # >>>>>>>>>> CRUD Equipment Model <<<<<<<<<< #
    path('get-Equipment-items/', GetAllEquipmentItems.as_view()),
    path('create-equipment-items/', CreaetAllEquipmentItems.as_view()),
    path('update-equipment-items/<int:pk>/', UpdateAllEquipmentItems.as_view()),
    path('delete-equipment-items/<int:pk>/', DeleteAllEquipmentItems.as_view()),


    # >>>>>>>>>> CRUD Info_about_cilinc Model <<<<<<<<<< #
    path('get-info-about-cilinc-items/', GetAllInfo_about_cilincItems.as_view()),
    path('create-info-about-cilinc-items/', CreateAllInfo_about_cilincItems.as_view()),
    path('update-info-about-cilinc-items/<int:pk>/', UpdateAllInfo_about_cilincItems.as_view()),
    path('delete-info-about-cilinc-items/<int:pk>/', DeleteAllInfo_about_cilincItems.as_view()),
    ]