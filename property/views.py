from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from .filters import *


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist')

    context = {'page': page}
    return render(request, 'property/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, " An error occured dirong registration")

    return render(request, 'property/login_register.html', {'form': form})


@login_required(login_url='login')
def home(request):
    properties = Property.objects.all()
    units = Unit.objects.filter(status="Vacant")
    tenants = Profile.objects.filter(type__name="tenant")
    context = {'properties': properties, 'units': units, 'tenants': tenants}
    return render(request, 'property/home.html', context)


@login_required(login_url='login')
def profile_types(request):
    show_form = False
    profile_types = Profile_Type.objects.all()
    context = {'profile_types': profile_types, 'show_form': show_form}
    return render(request, 'property/profile_types.html', context)


@login_required(login_url='login')
def create_profile_type(request):
    show_form = True
    profile_types = Profile_Type.objects.all()
    context = {'profile_types': profile_types, 'show_form': show_form}

    if request.method == 'POST':
        profile_type = request.POST.get('profiletype')
        Profile_Type.objects.create(name=profile_type)
        return redirect('profile_types')

    return render(request, 'property/profile_types.html', context)


@login_required(login_url='login')
def update_profile_type(request, pk):
    show_form = True
    profile_types = Profile_Type.objects.all()
    profile_type = Profile_Type.objects.get(id=pk)
    context = {'profile_types': profile_types, 'profile_type': profile_type, 'show_form': show_form}

    if request.method == 'POST':
        profile_types = request.POST.get('profiletype')
        Profile_Type.objects.filter(id=pk).update(name=profile_type)
        return redirect('profile_types')

    return render(request, 'property/profile_types.html', context)


@login_required(login_url='login')
def delete_profile_type(request, pk):
    profile_type = Profile_Type.objects.get(id=pk)

    if request.method == 'POST':
        profile_type.delete()
        return redirect('profile_types')
    return render(request, 'property/delete.html', {'obj': profile_type})


@login_required(login_url='login')
def profiles(request):
    show_form = False
    form = ProfileForm()
    profiles = Profile.objects.all()
    myFilter = ProfileFilter(request.GET, queryset=profiles)
    profiles = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'profiles': profiles, 'myFilter': myFilter}
    return render(request, 'property/profiles.html', context)


@login_required(login_url='login')
def create_profile(request, type_pk):
    show_form = True
    form = ProfileForm()
    profile_type = Profile_Type.objects.get(id=type_pk)
    profiles = Profile.objects.filter(type=profile_type)
    myFilter = ProfileFilter(request.GET, queryset=profiles)
    profiles = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'profiles': profiles, 'myFilter': myFilter, 'profile_type': profile_type}

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.type = profile_type
            profile.save()
            return redirect('profiles')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/profiles.html', context)


@login_required(login_url='login')
def update_profile(request, pk):
    show_form = True
    profile = Profile.objects.get(id=pk)
    profile_type = profile.type
    form = ProfileForm(instance=profile)
    profiles = Profile.objects.filter(type=profile_type)
    myFilter = ProfileFilter(request.GET, queryset=profiles)
    profiles = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'profiles': profiles, 'myFilter': myFilter, 'profile_type': profile_type}

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.type = profile_type
            profile.save()
            return redirect('profiles')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/profiles.html', context)


@login_required(login_url='login')
def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        profile.delete()
        return redirect('profiles')
    return render(request, 'property/delete.html', {'obj': profile})


@login_required(login_url='login')
def property_types(request):
    property_types = Property_Type.objects.all()
    context = {'property_types': property_types}
    return render(request, 'property/property_type.html', context)


@login_required(login_url='login')
def create_property_type(request):
    property_types = Property_Type.objects.all()
    context = {'property_types': property_types}

    if request.method == 'POST':
        property_type = request.POST.get('propertytype')
        Property_Type.objects.create(type=property_type)
        return redirect('property-types')

    return render(request, 'property/property_type.html', context)


@login_required(login_url='login')
def update_property_type(request, pk):
    property_types = Property_Type.objects.all()
    property_type = Property_Type.objects.get(id=pk)
    context = {'property_types': property_types,
               'property_type': property_type}

    if request.method == 'POST':
        property_type = request.POST.get('propertytype')
        Property_Type.objects.filter(id=pk).update(name=property_types)
        return redirect('property-types')

    return render(request, 'property/property_types.html', context)


@login_required(login_url='login')
def delete_property_type(request, pk):
    property_type = Property_Type.objects.get(id=pk)

    if request.method == 'POST':
        property_type.delete()
        return redirect('property-types')
    return render(request, 'property/delete.html', {'obj': property_type})


@login_required(login_url='login')
def properties(request):
    show_form = False
    form = PropertyForm()
    principals = Profile.objects.filter(type__name='principal')
    properties = Property.objects.all()
    myFilter = PropertyFilter(request.GET, queryset=properties)
    properties = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'properties': properties, 'myFilter': myFilter, 'principals': principals}
    return render(request, 'property/properties.html', context)


@login_required(login_url='login')
def create_property(request, princ_pk):
    show_form = True
    form = PropertyForm()
    princ = Profile.objects.get(id=princ_pk)
    principals = Profile.objects.filter(type__name='principal')
    properties = Property.objects.filter(principal=princ_pk)
    myFilter = PropertyFilter(request.GET, queryset=properties)
    properties = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'properties': properties, 'myFilter': myFilter, 'principals': principals, 'principal': princ}

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.principal = princ
            property.save()
            return redirect('properties')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/properties.html', context)


@login_required(login_url='login')
def update_property(request, pk):
    show_form = True
    property = Property.objects.get(id=pk)
    principals = Profile.objects.filter(type__name='principal')
    princ = property.principal
    properties = Property.objects.filter(principal=princ)
    form = PropertyForm(instance=property)
    myFilter = PropertyFilter(request.GET, queryset=properties)
    properties = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'properties': properties, 'myFilter': myFilter, 'principals': principals, 'principal': princ}

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.principal = princ
            property.save()
            return redirect('properties')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/properties.html', context)


@login_required(login_url='login')
def delete_property(request, pk):
    property = Property.objects.get(id=pk)

    if request.method == 'POST':
        property.delete()
        return redirect('properties')
    return render(request, 'property/delete.html', {'obj': property})


@login_required(login_url='login')
def unit_types(request):
    show_form = False
    unit_types = Unit_Type.objects.all()
    context = {'unit_types': unit_types, 'show_form': show_form}
    return render(request, 'property/unit_types.html', context)


@login_required(login_url='login')
def create_unit_type(request):
    show_form = True
    unit_types = Unit_Type.objects.all()
    context = {'unit_types': unit_types, 'show_form': show_form}

    if request.method == 'POST':
        unit_type = request.POST.get('unittype')
        Unit_Type.objects.create(type=unit_type)
        return redirect('unit-types')

    return render(request, 'property/unit_types.html', context)


@login_required(login_url='login')
def update_unit_type(request, pk):
    show_form = True
    unit_types = Unit_Type.objects.all()
    unit_type = Unit_Type.objects.get(id=pk)
    context = {'unit_types': unit_types,
               'unit_type': unit_type, 'show_form': show_form}

    if request.method == 'POST':
        unit_type = request.POST.get('unittype')
        Unit_Type.objects.filter(id=pk).update(type=unit_type)
        return redirect('unit-types')

    return render(request, 'property/unit_types.html', context)


@login_required(login_url='login')
def delete_unit_type(request, pk):
    unit_type = Unit_Type.objects.get(id=pk)

    if request.method == 'POST':
        unit_type.delete()
        return redirect('unit-types')
    return render(request, 'property/delete.html', {'obj': unit_type})


@login_required(login_url='login')
def units(request):
    show_form = False
    properties = Property.objects.all()
    form = UnitForm()
    units = Unit.objects.all()
    myFilter = UnitFilter(request.GET, queryset=units)
    units = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'units': units, 'myFilter': myFilter,  'properties': properties}
    return render(request, 'property/units.html', context)


@login_required(login_url='login')
def create_unit(request, pk):
    show_form = True
    property = Property.objects.get(id=pk)
    properties = Property.objects.all()
    form = UnitForm()
    units = Unit.objects.all()
    myFilter = UnitFilter(request.GET, queryset=units)
    units = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'units': units, 'myFilter': myFilter, 'property': property, 'properties': properties}

    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = property
            unit.save()
            return redirect('units')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/units.html', context)


@login_required(login_url='login')
def update_unit(request, pk):
    show_form = True
    unit = Unit.objects.get(id=pk)
    form = UnitForm(instance=unit)
    units = Unit.objects.all()
    myFilter = UnitFilter(request.GET, queryset=units)
    units = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'units': units, 'myFilter': myFilter}

    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('units')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/properties.html', context)


@login_required(login_url='login')
def delete_unit(request, pk):
    unit = Unit.objects.get(id=pk)

    if request.method == 'POST':
        unit.delete()
        return redirect('units')
    return render(request, 'property/delete.html', {'obj': unit})


@login_required(login_url='login')
def occupancies(request):
    show_form = False
    form = Unit_Occupancy()
    occupancies = Unit_Occupancy.objects.all()
    myFilter = UnitOccupancyFilter(request.GET, queryset=occupancies)
    occupancies = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'occupancies': occupancies, 'myFilter': myFilter}
    return render(request, 'property/occupancy.html', context)


@login_required(login_url='login')
def create_occupancy(request):
    show_form = True
    form = UnitOccupancyForm()
    occupancies = Unit_Occupancy.objects.all()
    myFilter = UnitFilter(request.GET, queryset=occupancies)
    occupancies = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'occupancies': occupancies, 'myFilter': myFilter}

    if request.method == 'POST':
        form = UnitOccupancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('occupancies')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/units.html', context)


@login_required(login_url='login')
def update_occupancy(request, pk):
    show_form = True
    occupancy = Unit_Occupancy.objects.get(id=pk)
    form = UnitOccupancyForm(instance=occupancy)
    occupancies = Unit_Occupancy.objects.all()
    myFilter = UnitFilter(request.GET, queryset=occupancies)
    occupancies = myFilter.qs
    context = {'show_form': show_form, 'form': form,
               'occupancies': occupancies, 'myFilter': myFilter}

    if request.method == 'POST':
        form = UnitOccupancyForm(request.POST, instance=occupancy)
        if form.is_valid():
            form.save()
            return redirect('occupancies')
        else:
            messages.error(request, " Something went wrong")

    return render(request, 'property/occupancy.html', context)


@login_required(login_url='login')
def delete_occupancy(request, pk):
    occupancy = Unit_Occupancy.objects.get(id=pk)

    if request.method == 'POST':
        occupancy.delete()
        return redirect('occupancies')
    return render(request, 'property/delete.html', {'obj': occupancy})
