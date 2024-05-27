from django.contrib import admin
from .models import Animal, AnimalPlace, Cages, CagesNeighbours, CompatibleType, Food, FoodSeller, HowEat, Offspring, ResponsibilityForAnimal, Sellers, TypeAnimal, VaccinationsAndDiseases, Workers

admin.site.register(Animal)
admin.site.register(AnimalPlace)
admin.site.register(Cages)
admin.site.register(CagesNeighbours)
admin.site.register(CompatibleType)
admin.site.register(Food)
admin.site.register(FoodSeller)
admin.site.register(HowEat)
admin.site.register(Offspring)
admin.site.register(ResponsibilityForAnimal)
admin.site.register(Sellers)
admin.site.register(TypeAnimal)
admin.site.register(VaccinationsAndDiseases)
admin.site.register(Workers)

