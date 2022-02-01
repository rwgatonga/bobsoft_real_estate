from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile_Type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(
        Profile_Type, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    idno = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True,  blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bank_Name(models.Model):
    name = models.CharField(max_length=50, unique=True)
    swift_code = models.CharField(max_length=12)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bank_Detail(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, blank=True, null=True)
    bankname = models.ForeignKey(
        Bank_Name, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile}-{self.bankname}'


class Self_Bank_detail(models.Model):
    bankname = models.ForeignKey(
        Bank_Name, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bankname}-{self.branch}'


class Property_Type(models.Model):
    type = models.CharField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Property(models.Model):
    name = models.CharField(max_length=50, unique=True)
    principal = models.ForeignKey(
        Profile, related_name='property_principal', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=50)
    type = models.ForeignKey(
        Property_Type, on_delete=models.SET_NULL, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.location}'

    class Meta:
        verbose_name_plural = 'Properties'


class Property_Image(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images', default="./uploads/images/zebra.jpeg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Unit_Type(models.Model):
    type = models.CharField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Unit(models.Model):
    occupancy = [
        ('Vacant', 'Vacant'),
        ('Occupied', 'Occupied'),
        ('Under Repair', 'Under Repair'),
        ('On Notice', 'On Notice'),
    ]

    name = models.CharField(max_length=50)
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.ForeignKey(
        Unit_Type, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=100, choices=occupancy)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['property', 'name']


class Unit_Image(models.Model):
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images', default="./uploads/images/zebra.jpeg", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Unit_Occupancy(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)
    date_notice = models.DateTimeField(null=True, blank=True)
    date_out = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.unit}-{self.tenant}'
