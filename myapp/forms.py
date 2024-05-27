from django import forms
from .models import *

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'type', 'height', 'weight', 'age', 'date_of_entry', 'date_of_departure', 'departure_zoo']

class AnimalPlaceForm(forms.ModelForm):
    class Meta:
        model = AnimalPlace
        fields = ['animal', 'cage', 'start_residence', 'end_residence']

class CagesForm(forms.ModelForm):
    class Meta:
        model = Cages
        fields = ['is_warm']

class CagesNeighboursForm(forms.ModelForm):
    class Meta:
        model = CagesNeighbours
        fields = ['cage', 'cage_id_n']

class CompatibleTypeForm(forms.ModelForm):
    class Meta:
        model = CompatibleType
        fields = ['animal_type', 'compatible_type']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name']

class FoodSellerForm(forms.ModelForm):
    class Meta:
        model = FoodSeller
        fields = ['seller', 'food', 'weight', 'start', 'end', 'price']

class HowEatForm(forms.ModelForm):
    class Meta:
        model = HowEat
        fields = ['type', 'season', 'food', 'weight', 'age_from', 'age_to']

class OffspringForm(forms.ModelForm):
    class Meta:
        model = Offspring
        fields = ['mom', 'dad', 'child']

class ResponsibilityForAnimalForm(forms.ModelForm):
    class Meta:
        model = ResponsibilityForAnimal
        fields = ['animal', 'worker', 'date_start', 'date_end']

class SellersForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['name']

class TypeAnimalForm(forms.ModelForm):
    class Meta:
        model = TypeAnimal
        fields = ['name', 'predator', 'need_warm']

class VaccinationsAndDiseasesForm(forms.ModelForm):
    class Meta:
        model = VaccinationsAndDiseases
        fields = ['animal', 'name']

class WorkersForm(forms.ModelForm):
    GENDER_CHOICES = [
        (True, 'Мужчина'),
        (False, 'Женщина')
    ]

    male = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Workers
        fields = ['name', 'wages', 'male', 'age', 'profession', 'date_appointment', 'date_layoff']


class WorkerTenureForm(forms.Form):
    years = forms.IntegerField(label='Years of tenure', min_value=0)

class WorkerAgeForm(forms.Form):
    age_min = forms.IntegerField(label='Minimum age', min_value=0)
    age_max = forms.IntegerField(label='Maximum age', min_value=0)

class WorkerWagesForm(forms.Form):
    wages_min = forms.IntegerField(label='Minimum wages', min_value=0)

class WorkerGenderForm(forms.Form):
    GENDER_CHOICES = [
        (True, 'Male'),
        (False, 'Female')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

class AnimalTypeForm(forms.Form):
    type_animal = forms.ModelChoiceField(queryset=TypeAnimal.objects.all(), label="Type of Animal")

class AnimalNameForm(forms.Form):
    animal_name = forms.ModelChoiceField(queryset=Animal.objects.all(), label="Name of Animal")

class AnimalQueryForm(forms.Form):
    animal_type = forms.ModelChoiceField(queryset=TypeAnimal.objects.all(), label='Animal Type')
    cage_id = forms.ModelChoiceField(queryset=Cages.objects.all(), label='Cage ID')

class AgeForm(forms.Form):
    min_age = forms.IntegerField(label='Minimum Age', min_value=0)

class VaccinationOrDiseaseForm(forms.Form):
    name = forms.CharField(label='Vaccination or Disease Name', max_length=100)

class AnimalTypeForm(forms.Form):
    compatible_type_name = forms.ModelChoiceField(
        queryset=TypeAnimal.objects.all(), 
        label="Compatible Animal Type"
    )

class FoodDeliveryForm(forms.Form):
    food_name = forms.CharField(label='Food Name', max_length=100)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')

class AnimalStatsForm(forms.Form):
    pass

class DepartureZooForm(forms.Form):
    pass


