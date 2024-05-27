from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.db.models import F, Sum
from .models import *
from .forms import *

def home(request):
    return render(request, 'myapp/home.html')

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'myapp/animal_list.html', {'animals': animals})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'myapp/animal_detail.html', {'animal': animal})

def animal_new(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'myapp/animal_edit.html', {'form': form})

def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            animal = form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'myapp/animal_edit.html', {'form': form})

def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return redirect('animal_list')

def animalplace_list(request):
    animalplaces = AnimalPlace.objects.all()
    return render(request, 'myapp/animalplace_list.html', {'animalplaces': animalplaces})
    
def animalplace_detail(request, pk):
    animalplace = get_object_or_404(AnimalPlace, pk=pk)
    return render(request, 'myapp/animalplace_detail.html', {'animalplace': animalplace})

def animalplace_new(request):
    if request.method == "POST":
        form = AnimalPlaceForm(request.POST)
        if form.is_valid():
            animalplace = form.save()
            return redirect('animalplace_detail', pk=animalplace.pk)
    else:
        form = AnimalPlaceForm()
    return render(request, 'myapp/animalplace_edit.html', {'form': form})

def animalplace_edit(request, pk):
    animalplace = get_object_or_404(AnimalPlace, pk=pk)
    if request.method == "POST":
        form = AnimalPlaceForm(request.POST, instance=animalplace)
        if form.is_valid():
            animalplace = form.save()
            return redirect('animalplace_detail', pk=animalplace.pk)
    else:
        form = AnimalPlaceForm(instance=animalplace)
    return render(request, 'myapp/animalplace_edit.html', {'form': form})

def animalplace_delete(request, pk):
    animalplace = get_object_or_404(AnimalPlace, pk=pk)
    animalplace.delete()
    return redirect('animalplace_list')


def cages_list(request):
    cages = Cages.objects.all()
    return render(request, 'myapp/cages_list.html', {'cages': cages})

def cages_detail(request, pk):
    cage = get_object_or_404(Cages, pk=pk)
    return render(request, 'myapp/cages_detail.html', {'cage': cage})

def cages_new(request):
    if request.method == "POST":
        form = CagesForm(request.POST)
        if form.is_valid():
            cage = form.save()
            return redirect('cages_detail', pk=cage.pk)
    else:
        form = CagesForm()
    return render(request, 'myapp/cages_edit.html', {'form': form})

def cages_edit(request, pk):
    cage = get_object_or_404(Cages, pk=pk)
    if request.method == "POST":
        form = CagesForm(request.POST, instance=cage)
        if form.is_valid():
            cage = form.save()
            return redirect('cages_detail', pk=cage.pk)
    else:
        form = CagesForm(instance=cage)
    return render(request, 'myapp/cages_edit.html', {'form': form})

def cages_delete(request, pk):
    cage = get_object_or_404(Cages, pk=pk)
    cage.delete()
    return redirect('cages_list')

def cagesneighbours_list(request):
    cagesneighbours = CagesNeighbours.objects.all()
    return render(request, 'myapp/cagesneighbours_list.html', {'cagesneighbours': cagesneighbours})

def cagesneighbours_detail(request, pk):
    cagesneighbour = get_object_or_404(CagesNeighbours, pk=pk)
    return render(request, 'myapp/cagesneighbours_detail.html', {'cagesneighbour': cagesneighbour})

def cagesneighbours_new(request):
    if request.method == "POST":
        form = CagesNeighboursForm(request.POST)
        if form.is_valid():
            cagesneighbour = form.save()
            return redirect('cagesneighbours_detail', pk=cagesneighbour.pk)
    else:
        form = CagesNeighboursForm()
    return render(request, 'myapp/cagesneighbours_edit.html', {'form': form})

def cagesneighbours_edit(request, pk):
    cagesneighbour = get_object_or_404(CagesNeighbours, pk=pk)
    if request.method == "POST":
        form = CagesNeighboursForm(request.POST, instance=cagesneighbour)
        if form.is_valid():
            cagesneighbour = form.save()
            return redirect('cagesneighbours_detail', pk=cagesneighbour.pk)
    else:
        form = CagesNeighboursForm(instance=cagesneighbour)
    return render(request, 'myapp/cagesneighbours_edit.html', {'form': form})

def cagesneighbours_delete(request, pk):
    cagesneighbour = get_object_or_404(CagesNeighbours, pk=pk)
    cagesneighbour.delete()
    return redirect('cagesneighbours_list')

def compatibletype_list(request):
    compatibletypes = CompatibleType.objects.all()
    return render(request, 'myapp/compatibletype_list.html', {'compatibletypes': compatibletypes})

def compatibletype_detail(request, pk):
    compatibletype = get_object_or_404(CompatibleType, pk=pk)
    return render(request, 'myapp/compatibletype_detail.html', {'compatibletype': compatibletype})

def compatibletype_new(request):
    if request.method == "POST":
        form = CompatibleTypeForm(request.POST)
        if form.is_valid():
            compatibletype = form.save()
            return redirect('compatibletype_detail', pk=compatibletype.pk)
    else:
        form = CompatibleTypeForm()
    return render(request, 'myapp/compatibletype_edit.html', {'form': form})

def compatibletype_edit(request, pk):
    compatibletype = get_object_or_404(CompatibleType, pk=pk)
    if request.method == "POST":
        form = CompatibleTypeForm(request.POST, instance=compatibletype)
        if form.is_valid():
            compatibletype = form.save()
            return redirect('compatibletype_detail', pk=compatibletype.pk)
    else:
        form = CompatibleTypeForm(instance=compatibletype)
    return render(request, 'myapp/compatibletype_edit.html', {'form': form})

def compatibletype_delete(request, pk):
    compatibletype = get_object_or_404(CompatibleType, pk=pk)
    compatibletype.delete()
    return redirect('compatibletype_list')

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'myapp/food_list.html', {'foods': foods})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'myapp/food_detail.html', {'food': food})

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm()
    return render(request, 'myapp/food_edit.html', {'form': form})

def food_edit(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm(instance=food)
    return render(request, 'myapp/food_edit.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('food_list')

def foodseller_list(request):
    foodseller = FoodSeller.objects.all()
    return render(request, 'myapp/foodseller_list.html', {'foodseller': foodseller})

def foodseller_detail(request, pk):
    foodseller = get_object_or_404(FoodSeller, pk=pk)
    return render(request, 'myapp/foodseller_detail.html', {'foodseller': foodseller})

def foodseller_new(request):
    if request.method == "POST":
        form = FoodSellerForm(request.POST)
        if form.is_valid():
            foodseller = form.save()
            return redirect('foodseller_detail', pk=foodseller.pk)
    else:
        form = FoodSellerForm()
    return render(request, 'myapp/foodseller_edit.html', {'form': form})

def foodseller_edit(request, pk):
    foodseller = get_object_or_404(FoodSeller, pk=pk)
    if request.method == "POST":
        form = FoodSellerForm(request.POST, instance=foodseller)
        if form.is_valid():
            foodseller = form.save()
            return redirect('foodseller_detail', pk=foodseller.pk)
    else:
        form = FoodSellerForm(instance=foodseller)
    return render(request, 'myapp/foodseller_edit.html', {'form': form})

def foodseller_delete(request, pk):
    foodseller = get_object_or_404(FoodSeller, pk=pk)
    foodseller.delete()
    return redirect('foodseller_list')  

def howeat_list(request):
    howeats = HowEat.objects.all()
    return render(request, 'myapp/howeat_list.html', {'howeats': howeats})

def howeat_detail(request, pk):
    howeat = get_object_or_404(HowEat, pk=pk)
    return render(request, 'myapp/howeat_detail.html', {'howeat': howeat})

def howeat_new(request):
    if request.method == "POST":
        form = HowEatForm(request.POST)
        if form.is_valid():
            howeat = form.save()
            return redirect('howeat_detail', pk=howeat.pk)
    else:
        form = HowEatForm()
    return render(request, 'myapp/howeat_edit.html', {'form': form})

def howeat_edit(request, pk):
    howeat = get_object_or_404(HowEat, pk=pk)
    if request.method == "POST":
        form = HowEatForm(request.POST, instance=howeat)
        if form.is_valid():
            howeat = form.save()
            return redirect('howeat_detail', pk=howeat.pk)
    else:
        form = HowEatForm(instance=howeat)
    return render(request, 'myapp/howeat_edit.html', {'form': form})

def howeat_delete(request, pk):
    howeat = get_object_or_404(HowEat, pk=pk)
    howeat.delete()
    return redirect('howeat_list')   

def offspring_list(request):
    offsprings = Offspring.objects.all()
    return render(request, 'myapp/offspring_list.html', {'offsprings': offsprings})

def offspring_detail(request, pk):
    offspring = get_object_or_404(Offspring, pk=pk)
    return render(request, 'myapp/offspring_detail.html', {'offspring': offspring})

def offspring_new(request):
    if request.method == "POST":
        form = OffspringForm(request.POST)
        if form.is_valid():
            offspring = form.save()
            return redirect('offspring_detail', pk=offspring.pk)
    else:
        form = OffspringForm()
    return render(request, 'myapp/offspring_edit.html', {'form': form})

def offspring_edit(request, pk):
    offspring = get_object_or_404(Offspring, pk=pk)
    if request.method == "POST":    
        form = OffspringForm(request.POST, instance=offspring)
        if form.is_valid():
            offspring = form.save()
            return redirect('offspring_detail', pk=offspring.pk)
    else:
        form = OffspringForm(instance=offspring)
    return render(request, 'myapp/offspring_edit.html', {'form': form})

def offspring_delete(request, pk):
    offspring = get_object_or_404(Offspring, pk=pk)
    offspring.delete()
    return redirect('offspring_list')

def responsibilityforanimal_list(request):
    responsibilityforanimals = ResponsibilityForAnimal.objects.all()
    return render(request, 'myapp/responsibilityforanimal_list.html', {'responsibilityforanimals': responsibilityforanimals}) 

def responsibilityforanimal_detail(request, pk):
    responsibilityforanimal = get_object_or_404(ResponsibilityForAnimal, pk=pk)
    return render(request, 'myapp/responsibilityforanimal_detail.html', {'responsibilityforanimal': responsibilityforanimal})

def responsibilityforanimal_new(request):
    if request.method == "POST":
        form = ResponsibilityForAnimalForm(request.POST)
        if form.is_valid():
            responsibilityforanimal = form.save()
            return redirect('responsibilityforanimal_detail', pk=responsibilityforanimal.pk)
    else:
        form = ResponsibilityForAnimalForm()
    return render(request, 'myapp/responsibilityforanimal_edit.html', {'form': form})

def responsibilityforanimal_edit(request, pk):
    responsibilityforanimal = get_object_or_404(ResponsibilityForAnimal, pk=pk)
    if request.method == "POST":
        form = ResponsibilityForAnimalForm(request.POST, instance=responsibilityforanimal)
        if form.is_valid():
            responsibilityforanimal = form.save()
            return redirect('responsibilityforanimal_detail', pk=responsibilityforanimal.pk)
    else:
        form = ResponsibilityForAnimalForm(instance=responsibilityforanimal)
    return render(request, 'myapp/responsibilityforanimal_edit.html', {'form': form})

def responsibilityforanimal_delete(request, pk):
    responsibilityforanimal = get_object_or_404(ResponsibilityForAnimal, pk=pk)
    responsibilityforanimal.delete()
    return redirect('responsibilityforanimal_list')

def sellers_list(request):
    sellers = Sellers.objects.all()
    return render(request, 'myapp/sellers_list.html', {'sellers': sellers})

def sellers_detail(request, pk):
    seller = get_object_or_404(Sellers, pk=pk)
    return render(request, 'myapp/seller_detail.html', {'seller': seller})

def sellers_new(request):
    if request.method == "POST":
        form = SellersForm(request.POST)
        if form.is_valid():
            seller = form.save()
            return redirect('sellers_detail', pk=seller.pk)
    else:
        form = SellersForm()
    return render(request, 'myapp/seller_edit.html', {'form': form})

def sellers_edit(request, pk):  
    seller = get_object_or_404(Sellers, pk=pk)
    if request.method == "POST":
        form = SellersForm(request.POST, instance=seller)
        if form.is_valid():
            seller = form.save()
            return redirect('seller_detail', pk=seller.pk)
    else:
        form = SellersForm(instance=seller)
    return render(request, 'myapp/seller_edit.html', {'form': form})

def sellers_delete(request, pk):
    seller = get_object_or_404(Sellers, pk=pk)
    seller.delete()
    return redirect('sellers_list')

def typeanimal_list(request):
    typeanimals = TypeAnimal.objects.all()
    return render(request, 'myapp/typeanimal_list.html', {'typeanimals': typeanimals})

def typeanimal_detail(request, pk):
    typeanimal = get_object_or_404(TypeAnimal, pk=pk)
    return render(request, 'myapp/typeanimal_detail.html', {'typeanimal': typeanimal})

def typeanimal_new(request):
    if request.method == "POST":
        form = TypeAnimalForm(request.POST)
        if form.is_valid():
            typeanimal = form.save()
            return redirect('typeanimal_detail', pk=typeanimal.pk)
    else:
        form = TypeAnimalForm()
    return render(request, 'myapp/typeanimal_edit.html', {'form': form})

def typeanimal_edit(request, pk):
    typeanimal = get_object_or_404(TypeAnimal, pk=pk)
    if request.method == "POST":
        form = TypeAnimalForm(request.POST, instance=typeanimal)
        if form.is_valid():
            typeanimal = form.save()
            return redirect('typeanimal_detail', pk=typeanimal.pk)
    else:
        form = TypeAnimalForm(instance=typeanimal)
    return render(request, 'myapp/typeanimal_edit.html', {'form': form})

def typeanimal_delete(request, pk):
    typeanimal = get_object_or_404(TypeAnimal, pk=pk)
    typeanimal.delete()
    return redirect('typeanimal_list')

def vaccinationsanddiseases_list(request):
    vaccinationsanddiseases = VaccinationsAndDiseases.objects.all()
    return render(request, 'myapp/vaccinationsanddiseases_list.html', {'vaccinationsanddiseases': vaccinationsanddiseases})

def vaccinationsanddiseases_detail(request, pk):
    vaccinationsanddiseases = get_object_or_404(VaccinationsAndDiseases, pk=pk)
    return render(request, 'myapp/vaccinationsanddiseases_detail.html', {'vaccinationsanddiseases': vaccinationsanddiseases})

def vaccinationsanddiseases_new(request):
    if request.method == "POST":
        form = VaccinationsAndDiseasesForm(request.POST)
        if form.is_valid():
            vaccinationsanddiseases = form.save()
            return redirect('vaccinationsanddiseases_detail', pk=vaccinationsanddiseases.pk)
    else:
        form = VaccinationsAndDiseasesForm()
    return render(request, 'myapp/vaccinationsanddiseases_edit.html', {'form': form})

def vaccinationsanddiseases_edit(request, pk):
    vaccinationsanddiseases = get_object_or_404(VaccinationsAndDiseases, pk=pk)
    if request.method == "POST":
        form = VaccinationsAndDiseasesForm(request.POST, instance=vaccinationsanddiseases)
        if form.is_valid():
            vaccinationsanddiseases = form.save()
            return redirect('vaccinationsanddiseases_detail', pk=vaccinationsanddiseases.pk)
    else:
        form = VaccinationsAndDiseasesForm(instance=vaccinationsanddiseases)
    return render(request, 'myapp/vaccinationsanddiseases_edit.html', {'form': form})

def vaccinationsanddiseases_delete(request, pk):
    vaccinationsanddiseases = get_object_or_404(VaccinationsAndDiseases, pk=pk)
    vaccinationsanddiseases.delete()
    return redirect('vaccinationsanddiseases_list')

def worker_list(request):
    workers = Workers.objects.all()
    return render(request, 'myapp/worker_list.html', {'workers': workers})

def worker_detail(request, pk):
    worker = get_object_or_404(Workers, pk=pk)
    return render(request, 'myapp/worker_detail.html', {'worker': worker})

def worker_new(request):
    if request.method == "POST":
        form = WorkersForm(request.POST)
        if form.is_valid():
            worker = form.save()
            return redirect('worker_detail', pk=worker.pk)
    else:
        form = WorkersForm()
    return render(request, 'myapp/worker_edit.html', {'form': form})

def worker_edit(request, pk):
    worker = get_object_or_404(Workers, pk=pk)
    if request.method == "POST":
        form = WorkersForm(request.POST, instance=worker)
        if form.is_valid():
            worker = form.save()
            return redirect('worker_detail', pk=worker.pk)
    else:
        form = WorkersForm(instance=worker)
    return render(request, 'myapp/worker_edit.html', {'form': form})

def worker_delete(request, pk):
    worker = get_object_or_404(Workers, pk=pk)
    worker.delete()
    return redirect('worker_list')

def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    return columns, rows

def worker_tenure(request):
    form = WorkerTenureForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        years = form.cleaned_data['years']
        query = "SELECT * FROM workers WHERE (COALESCE(date_layoff, CURRENT_DATE) - date_appointment) / 365 > %s;"
        columns, rows = execute_query(query, [years])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/worker_tenure.html', {'form': form, 'results': results})

def worker_age(request):
    form = WorkerAgeForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        age_min = form.cleaned_data['age_min']
        age_max = form.cleaned_data['age_max']
        query = "SELECT * FROM workers WHERE Age >= %s AND Age <= %s;"
        columns, rows = execute_query(query, [age_min, age_max])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/worker_age.html', {'form': form, 'results': results})

def worker_wages(request):
    form = WorkerWagesForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        wages_min = form.cleaned_data['wages_min']
        query = "SELECT * FROM workers WHERE wages >= %s;"
        columns, rows = execute_query(query, [wages_min])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/worker_wages.html', {'form': form, 'results': results})

def worker_gender(request):
    form = WorkerGenderForm(request.GET or None)
    results = {'query4': {'columns': [], 'rows': []}, 'query5': {'columns': [], 'rows': []}}

    if form.is_valid():
        gender = form.cleaned_data['gender']
        query4 = "SELECT * FROM workers WHERE male = %s;"
        query5 = "SELECT COUNT(*) AS TotalWorkers FROM workers WHERE male = %s;"
        
        columns, rows = execute_query(query4, [gender])
        results['query4'] = {'columns': columns, 'rows': rows}
        
        columns, rows = execute_query(query5, [gender])
        results['query5'] = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/worker_gender.html', {'form': form, 'results': results})

def total_workers_by_animal_type(request):
    form = AnimalTypeForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        type_animal = form.cleaned_data['type_animal']
        query = """
            SELECT COUNT(DISTINCT responsibility_for_animal.worker_id) AS total_workers
            FROM responsibility_for_animal
            LEFT JOIN animal ON responsibility_for_animal.animal_id = animal.id
            LEFT JOIN workers ON responsibility_for_animal.worker_id = workers.id
            LEFT JOIN type_animal ON animal.type = type_animal.id
            WHERE type_animal.name = %s;
        """
        columns, rows = execute_query(query, [type_animal.name])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/total_workers_by_animal_type.html', {'form': form, 'results': results})

def workers_by_animal_type(request):
    form = AnimalTypeForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        type_animal = form.cleaned_data['type_animal']
        query = """
            SELECT workers.name AS worker_name
            FROM responsibility_for_animal
            LEFT JOIN animal ON responsibility_for_animal.animal_id = animal.id
            LEFT JOIN workers ON responsibility_for_animal.worker_id = workers.id
            LEFT JOIN type_animal ON animal.type = type_animal.id
            WHERE type_animal.name = %s;
        """
        columns, rows = execute_query(query, [type_animal.name])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/workers_by_animal_type.html', {'form': form, 'results': results})

def total_workers_by_animal_name(request):
    form = AnimalNameForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        animal_name = form.cleaned_data['animal_name']
        query = """
            SELECT COUNT(DISTINCT responsibility_for_animal.worker_id) AS total_workers
            FROM responsibility_for_animal
            LEFT JOIN animal ON responsibility_for_animal.animal_id = animal.id
            LEFT JOIN workers ON responsibility_for_animal.worker_id = workers.id
            WHERE animal.name = %s;
        """
        columns, rows = execute_query(query, [animal_name.name])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/total_workers_by_animal_name.html', {'form': form, 'results': results})

def workers_by_animal_name(request):
    form = AnimalNameForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        animal_name = form.cleaned_data['animal_name']
        query = """
            SELECT workers.name AS worker_name
            FROM responsibility_for_animal
            LEFT JOIN animal ON responsibility_for_animal.animal_id = animal.id
            LEFT JOIN workers ON responsibility_for_animal.worker_id = workers.id
            WHERE animal.name = %s;
        """
        columns, rows = execute_query(query, [animal_name.name])
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/workers_by_animal_name.html', {'form': form, 'results': results})

def workers_in_by_animal_name(request):
    workers = None
    if request.method == 'POST':
        form = AnimalNameForm(request.POST)
        if form.is_valid():
            animal = form.cleaned_data['animal_name']
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT w.name AS worker_name
                    FROM workers w
                    LEFT JOIN responsibility_for_animal rfa ON w.id = rfa.worker_id
                    LEFT JOIN animal a ON rfa.animal_id = a.id
                    WHERE a.name = %s
                    AND w.profession IN ('ветеринар', 'уборщик', 'депрессировщик');
                """, [animal.name])
                workers = cursor.fetchall()
    else:
        form = AnimalNameForm()

    return render(request, 'myapp/workers_in_by_animal_name.html', {'form': form, 'workers': workers})

def workers_in_by_animal_type(request):
    workers = None
    if request.method == 'POST':
        form = AnimalTypeForm(request.POST)
        if form.is_valid():
            animal_type = form.cleaned_data['type_animal']
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT w.name AS worker_name
                    FROM workers w
                    LEFT JOIN responsibility_for_animal rfa ON w.id = rfa.worker_id
                    LEFT JOIN animal a ON rfa.animal_id = a.id
                    LEFT JOIN type_animal ta ON a.type = ta.id
                    WHERE ta.name = %s
                    AND w.profession IN ('ветеринар', 'уборщик', 'депрессировщик');
                """, [animal_type.name])
                workers = cursor.fetchall()
    else:
        form = AnimalTypeForm()

    return render(request, 'myapp/workers_in_by_animal_type.html', {'form': form, 'workers': workers})

def animal_type_in_cage(request):
    form = AnimalQueryForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        animal_type = form.cleaned_data['animal_type'].name
        cage_id = form.cleaned_data['cage_id'].id
        
        query = """
        SELECT 
            a.name AS animal_name,
            a.type AS animal_type,
            a.height AS animal_height,
            a.weight AS animal_weight,
            a.age AS animal_age,
            a.date_of_entry AS entry_date,
            a.date_of_departure AS departure_date,
            a.departure_zoo AS departure_zoo
        FROM 
            animal_place ap
        LEFT JOIN 
            animal a ON ap.animal_id = a.id
        LEFT JOIN 
            type_animal ta ON a.type = ta.id
        LEFT JOIN 
            cages c ON ap.cage_id = c.id
        WHERE 
            ta.name = %s
            AND c.id = %s
            AND a.date_of_entry <= ap.start_residence
            AND (a.date_of_departure IS NULL OR a.date_of_departure >= ap.end_residence)
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [animal_type, cage_id])
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/animal_type_in_cage.html', {'form': form, 'results': results})

def warm_animals(request):
    query = """
    SELECT 
        a.id AS animal_id,
        a.name AS animal_name,
        a.type AS animal_type,
        a.age AS animal_age,
        a.weight AS animal_weight,
        a.height AS animal_height
    FROM 
        animal a
    JOIN 
        type_animal ta ON a.type = ta.id
    WHERE 
        ta.need_warm = true
        AND (a.date_of_departure IS NULL OR a.date_of_departure >= CURRENT_DATE)
    """
    results = {'columns': [], 'rows': []}
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/warm_animals.html', {'results': results})

def warm_old_animals(request):
    form = AgeForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        min_age = form.cleaned_data['min_age']
        
        query = """
        SELECT 
            a.id AS animal_id,
            a.name AS animal_name,
            a.type AS animal_type,
            a.age AS animal_age,
            a.weight AS animal_weight,
            a.height AS animal_height
        FROM 
            animal a
        JOIN 
            type_animal ta ON a.type = ta.id
        WHERE 
            ta.need_warm = true
            AND a.age >= %s
            AND (a.date_of_departure IS NULL OR a.date_of_departure >= CURRENT_DATE)
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [min_age])
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/warm_old_animals.html', {'form': form, 'results': results})

def animals_with_vaccination_or_disease(request):
    form = VaccinationOrDiseaseForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        name = form.cleaned_data['name']
        
        query = """
        SELECT animal.*, COUNT(*) AS total
        FROM animal
        LEFT JOIN vaccinations_and_diseases ON animal.id = vaccinations_and_diseases.animal_id
        WHERE vaccinations_and_diseases.name = %s
        GROUP BY animal.id
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [name])
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/animals_with_vaccination_or_disease.html', {'form': form, 'results': results})


def compatible_animals(request):
    form = AnimalTypeForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        compatible_type = form.cleaned_data['compatible_type_name']
        
        query = """
        SELECT 
            a.name AS animal_name
        FROM 
            animal a
        JOIN 
            type_animal ta ON a.type = ta.id
        JOIN 
            compatible_type ct ON (ta.id = ct.animal_type_id OR ta.id = ct.compatible_type_id)
        JOIN 
            type_animal c ON ((ct.compatible_type_id = c.id AND c.id != ta.id) OR (ct.animal_type_id = c.id AND c.id != ta.id))
        WHERE c.name = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [compatible_type.name])
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/compatible_animals.html', {'form': form, 'results': results})

def food_sellers(request):
    form = FoodDeliveryForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    if form.is_valid():
        food_name = form.cleaned_data['food_name']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        
        query = """
        SELECT sellers.*
        FROM sellers
        LEFT JOIN food_seller ON sellers.id = food_seller.seller_id
        LEFT JOIN food ON food_seller.food_id = food.id
        WHERE (food.name = %s OR food.name IS NULL)
          AND (food_seller.start <= %s OR food_seller.end >= %s)
        GROUP BY sellers.id;
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [food_name, start_date, end_date])
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/food_sellers.html', {'form': form, 'results': results})

def animal_stats(request):
    form = AnimalStatsForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    query = """
    SELECT 
        animal.*, 
        COUNT(offspring.child_id) AS total_offspring, 
        vaccinations_and_diseases.name
    FROM 
        animal
    LEFT JOIN 
        offspring ON animal.id = offspring.mom_id OR animal.id = offspring.dad_id
    LEFT JOIN 
        vaccinations_and_diseases ON animal.id = vaccinations_and_diseases.animal_id
    GROUP BY 
        animal.id, 
        vaccinations_and_diseases.id;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/animal_stats.html', {'form': form, 'results': results})

def departure_zoos(request):
    form = DepartureZooForm(request.GET or None)
    results = {'columns': [], 'rows': []}

    query = """
    SELECT departure_zoo
    FROM animal
    WHERE departure_zoo IS NOT NULL
    GROUP BY departure_zoo;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        results = {'columns': columns, 'rows': rows}

    return render(request, 'myapp/departure_zoos.html', {'form': form, 'results': results})

def food_supply_status(request):
    required_food = HowEat.objects.annotate(
        total_weight_needed=Sum('animal__weight'),
        food_name=F('food__name')
    ).values('type_id', 'food_name', 'total_weight_needed')

    supplied_food = FoodSeller.objects.filter(seller__name='Zoo').values('food_id').annotate(
        total_weight_supplied=Sum('weight')
    )

    results = []
    for food in required_food:
        supplied = supplied_food.filter(food_id=food['food_name']).first()
        if supplied:
            total_weight_supplied = supplied['total_weight_supplied']
        else:
            total_weight_supplied = 0

        supply_status = 'Достаточно' if total_weight_supplied >= food['total_weight_needed'] else 'Недостаточно'

        results.append({
            'food_name': food['food_name'],
            'total_weight_needed': food['total_weight_needed'],
            'total_weight_supplied': total_weight_supplied,
            'supply_status': supply_status
        })

    return render(request, 'myapp/food_supply_status.html', {'results': results})


