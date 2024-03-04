from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator



class User(AbstractUser):
    full_name = models.CharField(max_length=200, db_index=True, verbose_name='Isim familyangini yozing')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Manzilingizni kriting')
    phone_number = models.CharField(max_length=13, unique=True,verbose_name='Telefon raqamingizni kiriting', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number',
        )])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'


class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name='Odam')
    STATUS_EMPLOYEE = (
        (1,"doctor"),
        (2,"manager"),
        (3,"admin"),
        (4,"nurse"),
        (5,"director"),
        (6,"cooker"),
    )
    status = models.IntegerField(choices=STATUS_EMPLOYEE, verbose_name='Qaysi lavozimda ishlashingizni kiriting')
    salary = models.PositiveIntegerField(verbose_name='oylik maoshingizni kiriting')
    work_time = models.CharField(max_length=255, null=True, blank=True,verbose_name='ish vaqtingizni kiriting')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='honangizni tanleng')
    experience = models.CharField(max_length=255, verbose_name='tajriba')
    bio = models.CharField(max_length=200, null=True, blank=True, verbose_name='Oziz haqizda malumotlar')
    age = models.IntegerField(verbose_name='Yoshingizni kriting')
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name='Bolimingizni tanleng')


    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Doktorlar'

    def __str__(self):
        return self.user.full_name


class Patient(models.Model):
    doctor = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='Doktoringizni tanleng')
    full_name = models.CharField(max_length=200, verbose_name='Isim familyanginzi kiriting')
    age = models.IntegerField(default=18, verbose_name='Yoshingizni kiriting')
    gender = models.IntegerField(default=1, verbose_name='Jinsigniz tangleng', choices=(
        (1, 'Male'),
        (2, 'Female'),
    ))
    address = models.CharField(max_length=200, verbose_name='Manzilignizni kiriting')
    photo = models.ImageField(upload_to='patient_photo/',  validators=[ImageFileValidator()], verbose_name='Rasimingizni kiritng')
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number',
        )])
    extra_phone_number = models.CharField(max_length=13, null=True,  blank=True, verbose_name='qoshimcha telefon raqimingizi kiriting')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='xonangizni kiriting')
    bio = models.TextField(verbose_name='oziz haqizda malumotlar kiriting')
    stayed_day = models.DateField(verbose_name='Nech kun qolishingizni kriitng')
    payment_status = models.IntegerField(default=3, verbose_name='Tolovdi kiriting', choices=(
        (1, 'paid'),
        (2, 'part_paid'),
        (3, 'unpaid')
    ))


    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Bemor'


    def __str__(self):
        return self.full_name



class Room(models.Model):
    name = models.CharField(max_length=200, verbose_name='Xonani nomini yoki raqamini kiriting')
    capacity = models.IntegerField(null=True, blank=True, verbose_name='Xonani sigimini kiriitng')
    status = models.IntegerField(max_length=200, default=2, verbose_name='Holati', choices=(
        (1, 'Lux'),
        (2, 'Standard'),
        (3, 'other')
    ))
    is_booked = models.BooleanField(default=False, verbose_name='Zakaz qilish')
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name='Bolim')
    equipment = models.ForeignKey(to='Equipment', on_delete=models.CASCADE, verbose_name='jihozlar')
    other_info = models.TextField(null=True, blank=True, verbose_name='Qoshimcha malumotlar')


    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Xona'

    def __str__(self):
        return self.name


class Payment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='Bemor')
    payment_amount = models.IntegerField(verbose_name='Tolov miqdori')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Yaratish')
    payment_type = models.IntegerField(default=2, verbose_name='Tolash yoli', choices=(
        (1,'card'),
        (2,'cash'),
        (3,'other')
    ))
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, verbose_name='QR code')

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constents.ERROS_CORRECT_L,
            box_siz=5,
            border=3,
        )
        qr.add_date(f"Yourto encode in the QR code: {self.patient.full_name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesID()
        img.save(buffer)
        buffer.seek(0)


        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Tolov'


    def __str__(self):
        return self.Patient.full_name


class Comment(models.Model):
    patient = models.ForeignKey(to='Patient',on_delete=models.CASCADE, verbose_name='Bemor')
    comment = models.CharField(max_length=200, verbose_name='Izoh')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Yaratish')


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Izoh'


class Income(models.Model):
    amount = models.IntegerField(verbose_name='Miqdori')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Yaratish')
    reason = models.CharField(max_length=255, verbose_name='Sabab')


    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Kirim'


class Ravenue(models.Model):
    amount = models.IntegerField(verbose_name='Miqdori')
    reason = models.CharField(max_length=255, verbose_name='Sabab')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Yaratish')


    class Meta:
        verbose_name = 'Ravenue'
        verbose_name_plural = 'Chiqim'


class Cassa(models.Model):
    total_summa = models.PositiveIntegerField(default=0, verbose_name='Hisob')


    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Kassa'


class Operation(models.Model):
    employees = models.ManyToManyField(to='Employee', verbose_name='Duhtir')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Kun vaqt')
    satrt_time = models.CharField(max_length=200, verbose_name='Boshlanishi')
    end_time = models.CharField(max_length=200, verbose_name='Tugash')
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name='Bemor')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, verbose_name='Hone')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Yaratish')


    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operatsiya'


    def __str__(self):
        return self.Employye.user.full_name



class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')


    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Bolim'


    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=200, verbose_name='hona')
    number = models.CharField(max_length=200, verbose_name='raqam')
    extra_info = models.TextField( verbose_name='qoshimcha malumot')

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Jihozlar'

    def __str__(self):
        return self.name


class Info_about_cilinc(models.Model):
    total_patients_number = models.CharField(max_length=255,  verbose_name='umumiy hisob')
    total_employee_number = models.CharField(max_length=255,  verbose_name='umumiy bemorlar')
    address = models.CharField(max_length=200,  verbose_name='Manzil')
    phone_number = models.CharField(max_length=13,  verbose_name='Telefon raqam')

    class Meta:
        verbose_name = 'Info_about_cilinc'
        verbose_name_plural = 'Qisqacha malumotlar'

    def __str__(self):
        return self.total_patients_number


class Attendence(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='bemor')
    date = models.DateField(verbose_name='kun')
    check_in = models.TimeField(null=True, blank=True, verbose_name='Kirish')
    check_out = models.TimeField(null=True, blank=True, verbose_name='chiqish')


    class Meta:
        unique_together = ['employee', 'date']


    def clean(self):
        if self.check_out and self.check_out < self.check_in:
            raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"





