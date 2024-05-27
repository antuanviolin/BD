from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('animals/', views.animal_list, name='animal_list'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal/new/', views.animal_new, name='animal_new'),
    path('animal/<int:pk>/edit/', views.animal_edit, name='animal_edit'),
    path('animal/<int:pk>/delete/', views.animal_delete, name='animal_delete'),

    path('animalplace/', views.animalplace_list, name='animalplace_list'),
    path('animalplace/<int:pk>/', views.animalplace_detail, name='animalplace_detail'),
    path('animalplace/new/', views.animalplace_new, name='animalplace_new'),
    path('animalplace/<int:pk>/edit/', views.animalplace_edit, name='animalplace_edit'),
    path('animalplace/<int:pk>/delete/', views.animalplace_delete, name='animalplace_delete'),

    path('cages/', views.cages_list, name='cages_list'),
    path('cages/<int:pk>/', views.cages_detail, name='cages_detail'),
    path('cages/new/', views.cages_new, name='cages_new'),
    path('cages/<int:pk>/edit/', views.cages_edit, name='cages_edit'),
    path('cages/<int:pk>/delete/', views.cages_delete, name='cages_delete'),
    
    path('cagesneighbours/', views.cagesneighbours_list, name='cagesneighbours_list'),
    path('cagesneighbours/<int:pk>/', views.cagesneighbours_detail, name='cagesneighbours_detail'),
    path('cagesneighbours/new/', views.cagesneighbours_new, name='cagesneighbours_new'),
    path('cagesneighbours/<int:pk>/edit/', views.cagesneighbours_edit, name='cagesneighbours_edit'),
    path('cagesneighbours/<int:pk>/delete/', views.cagesneighbours_delete, name='cagesneighbours_delete'),

    path('compatibletype/', views.compatibletype_list, name='compatibletype_list'),
    path('compatibletype/<int:pk>/', views.compatibletype_detail, name='compatibletype_detail'),
    path('compatibletype/new/', views.compatibletype_new, name='compatibletype_new'),
    path('compatibletype/<int:pk>/edit/', views.compatibletype_edit, name='compatibletype_edit'),
    path('compatibletype/<int:pk>/delete/', views.compatibletype_delete, name='compatibletype_delete'),

    path('food/', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('food/new/', views.food_new, name='food_new'),
    path('food/<int:pk>/edit/', views.food_edit, name='food_edit'),
    path('food/<int:pk>/delete/', views.food_delete, name='food_delete'),

    path('foodseller/', views.foodseller_list, name='foodseller_list'),
    path('foodseller/<int:pk>/', views.foodseller_detail, name='foodseller_detail'),
    path('foodseller/new/', views.foodseller_new, name='foodseller_new'),
    path('foodseller/<int:pk>/edit/', views.foodseller_edit, name='foodseller_edit'),
    path('foodseller/<int:pk>/delete/', views.foodseller_delete, name='foodseller_delete'),

    path('howeat/', views.howeat_list, name='howeat_list'),
    path('howeat/<int:pk>/', views.howeat_detail, name='howeat_detail'),
    path('howeat/new/', views.howeat_new, name='howeat_new'),
    path('howeat/<int:pk>/edit/', views.howeat_edit, name='howeat_edit'),
    path('howeat/<int:pk>/delete/', views.howeat_delete, name='howeat_delete'),
    
    path('offspring/', views.offspring_list, name='offspring_list'),
    path('offspring/<int:pk>/', views.offspring_detail, name='offspring_detail'),
    path('offspring/new/', views.offspring_new, name='offspring_new'),
    path('offspring/<int:pk>/edit/', views.offspring_edit, name='offspring_edit'),
    path('offspring/<int:pk>/delete/', views.offspring_delete, name='offspring_delete'),

    path('responsibilityforanimal/', views.responsibilityforanimal_list, name='responsibilityforanimal_list'),
    path('responsibilityforanimal/<int:pk>/', views.responsibilityforanimal_detail, name='responsibilityforanimal_detail'),
    path('responsibilityforanimal/new/', views.responsibilityforanimal_new, name='responsibilityforanimal_new'),
    path('responsibilityforanimal/<int:pk>/edit/', views.responsibilityforanimal_edit, name='responsibilityforanimal_edit'),
    path('responsibilityforanimal/<int:pk>/delete/', views.responsibilityforanimal_delete, name='responsibilityforanimal_delete'),

    path('sellers/', views.sellers_list, name='sellers_list'),
    path('sellers/<int:pk>/', views.sellers_detail, name='sellers_detail'),
    path('sellers/new/', views.sellers_new, name='sellers_new'),
    path('sellers/<int:pk>/edit/', views.sellers_edit, name='sellers_edit'),
    path('sellers/<int:pk>/delete/', views.sellers_delete, name='sellers_delete'),

    path('typeanimal/', views.typeanimal_list, name='typeanimal_list'),
    path('typeanimal/<int:pk>/', views.typeanimal_detail, name='typeanimal_detail'),
    path('typeanimal/new/', views.typeanimal_new, name='typeanimal_new'),
    path('typeanimal/<int:pk>/edit/', views.typeanimal_edit, name='typeanimal_edit'),
    path('typeanimal/<int:pk>/delete/', views.typeanimal_delete, name='typeanimal_delete'),

    path('vaccinationsanddiseases/', views.vaccinationsanddiseases_list, name='vaccinationsanddiseases_list'),
    path('vaccinationsanddiseases/<int:pk>/', views.vaccinationsanddiseases_detail, name='vaccinationsanddiseases_detail'),
    path('vaccinationsanddiseases/new/', views.vaccinationsanddiseases_new, name='vaccinationsanddiseases_new'),
    path('vaccinationsanddiseases/<int:pk>/edit/', views.vaccinationsanddiseases_edit, name='vaccinationsanddiseases_edit'),
    path('vaccinationsanddiseases/<int:pk>/delete/', views.vaccinationsanddiseases_delete, name='vaccinationsanddiseases_delete'),

    path('worker/', views.worker_list, name='worker_list'),
    path('worker/<int:pk>/', views.worker_detail, name='worker_detail'),
    path('worker/new/', views.worker_new, name='worker_new'),
    path('worker/<int:pk>/edit/', views.worker_edit, name='worker_edit'),
    path('worker/<int:pk>/delete/', views.worker_delete, name='worker_delete'),

    path('worker_tenure/', views.worker_tenure, name='worker_tenure'),
    path('worker_age/', views.worker_age, name='worker_age'),
    path('worker_wages/', views.worker_wages, name='worker_wages'),
    path('worker_gender/', views.worker_gender, name='worker_gender'),

    path('total_workers_by_animal_type/', views.total_workers_by_animal_type, name='total_workers_by_animal_type'),
    path('workers_by_animal_type/', views.workers_by_animal_type, name='workers_by_animal_type'),
    path('total_workers_by_animal_name/', views.total_workers_by_animal_name, name='total_workers_by_animal_name'),
    path('workers_by_animal_name/', views.workers_by_animal_name, name='workers_by_animal_name'),

    path('workers_in_by_animal_name/', views.workers_in_by_animal_name, name='workers_in_by_animal_name'),
    path('workers_in_by_animal_type/', views.workers_in_by_animal_type, name='workers_in_by_animal_type'),

    path('animal_type_in_cage/', views.animal_type_in_cage, name='animal_type_in_cage'),
    path('warm_animals/', views.warm_animals, name='warm_animals'),
    path('warm_old_animals/', views.warm_old_animals, name='warm_old_animals'),

    path('animals_with_vaccination_or_disease/', views.animals_with_vaccination_or_disease, name='animals_with_vaccination_or_disease'),
    path('compatible_animals/', views.compatible_animals, name='compatible_animals'),
    path('food_sellers/', views.food_sellers, name='food_sellers'),
    path('animal_stats/', views.animal_stats, name='animal_stats'),
    path('departure_zoos/', views.departure_zoos, name='departure_zoos'),
    path('food_supply_status/', views.food_supply_status, name='food_supply_status'),
]
