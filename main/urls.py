from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>> FILTER employee <<<<<<<<<< #
    path('filter-employee-user/', filter_employee_username),
    path('filter-employee-status/', filter_emoloyee_status),
    path('filter-employee-experinese/', filter_emoloyee_experinese),
    path('filter-employee-room/', filter_emoloyee_room),
    path('filter-employee-department/', filter_emoloyee_department),
    path('filter-employee-selrey/', filter_emoloyee_selrey),


    # >>>>>>>>>> FILTER patient <<<<<<<<<< #
    path('filter-patient-doctor/', filter_patient_doctor),
    path('filter-patient-gender/', filter_patient_gender),
    path('filter-patient-phone_number/', filter_patient_phone_number),
    path('filter-patient-room/', filter_patient_room),
    path('filter-patient-payment-status/', filter_patient_payment_status),


    # >>>>>>>>>> FILTER room <<<<<<<<<< #
    path('filter-room-name/', filter_room_name),
    path('filter-room-status/', filter_room_status),
    path('filter-room-capasity/', filter_room_capasity),
    path('filter-room-equipment/', filter_room_equipment),
    path('filter-room-department/', filter_room_department),
    path('filter-room-is-booked/', filter_room_is_booked),


    # >>>>>>>>>> FILTER payment <<<<<<<<<< #
    path('filter-comment-status/', filter_comment_status),
    path('filter-payment-patient/', filter_payment_patient),
    path('filter-payment-created-at/', filter_payment_created_at),
    path('filter-payment-payment-type/', filter_payment_payment_type),


    # >>>>>>>>>> FILTER income <<<<<<<<<< #
    path('filter-income-create-at/', filter_income_created_at),
    path('filter-income-amount/', filter_income_amount),


    # >>>>>>>>>> FILTER ravenue <<<<<<<<<< #
    path('filter-ravenue-patient/', filter_ravenue_created_at),
    path('filter-ravenue-amount/', filter_ravenue_amount),


    # >>>>>>>>>> FILTER Operation <<<<<<<<<< #
    path('filter-operation-employees/', filter_operation_employee),
    path('filter-operation-date-time/', filter_operation_date_time),
    path('filter-operation-patient/', filter_operation_patient),
    path('filter-operation-room/', filter_operation_room),


    # >>>>>>>>>> FILTER department <<<<<<<<<< #
    path('filter-department-name/', filter_department_name),
    path('filter-equiment-name/', filter_equiment_name),


    # >>>>>>>>>> FILTER attendence <<<<<<<<<< #
    path('filter-attendence-employee/', filter_attendence_employee),
    path('filter-attendence-date/', filter_attendence_date),

]