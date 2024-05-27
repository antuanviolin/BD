# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Animal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    type = models.ForeignKey('TypeAnimal', models.DO_NOTHING, db_column='type')
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    date_of_entry = models.DateField()
    date_of_departure = models.DateField(blank=True, null=True)
    departure_zoo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal'

    def __str__(self):
        return self.name


class AnimalPlace(models.Model):
    animal = models.ForeignKey(Animal, models.DO_NOTHING)
    cage = models.ForeignKey('Cages', models.DO_NOTHING)
    start_residence = models.DateField()
    end_residence = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal_place'

    def __str__(self):
        return f"{self.animal} in {self.cage}"


class Cages(models.Model):
    id = models.IntegerField(primary_key=True)
    is_warm = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cages'

    def __str__(self):
        return f"Cage {self.id}"


class CagesNeighbours(models.Model):
    cage = models.ForeignKey(Cages, models.DO_NOTHING)
    cage_id_n = models.ForeignKey(Cages, models.DO_NOTHING, db_column='cage_id_n', related_name='cagesneighbours_cage_id_n_set')

    class Meta:
        managed = False
        db_table = 'cages_neighbours'

    def __str__(self):
        return f"{self.cage} - {self.cage_id_n}"


class CompatibleType(models.Model):
    animal_type = models.ForeignKey('TypeAnimal', models.DO_NOTHING)
    compatible_type = models.ForeignKey('TypeAnimal', models.DO_NOTHING, related_name='compatibletype_compatible_type_set')

    class Meta:
        managed = False
        db_table = 'compatible_type'

    def __str__(self):
        return f"{self.animal_type} compatible with {self.compatible_type}"


class Food(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'food'
    
    def __str__(self):
        return self.name


class FoodSeller(models.Model):
    id = models.IntegerField(primary_key=True)
    seller = models.ForeignKey('Sellers', models.DO_NOTHING)
    food = models.ForeignKey(Food, models.DO_NOTHING)
    weight = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'food_seller'
    
    def __str__(self):
        return f"{self.seller} sells {self.food}"


class HowEat(models.Model):
    SEASON_CHOICES = [
        (1, 'Winter'),
        (2, 'Spring'),
        (3, 'Summer'),
        (4, 'Autumn'),
    ]
    type = models.ForeignKey('TypeAnimal', models.DO_NOTHING)
    season = models.IntegerField(choices=SEASON_CHOICES)
    food = models.ForeignKey(Food, models.DO_NOTHING)
    weight = models.IntegerField()
    age_from = models.IntegerField()
    age_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'how_eat'

    def __str__(self):
        return f"{self.type} eats {self.food} ({self.season})"


class Offspring(models.Model):
    mom = models.ForeignKey(Animal, models.DO_NOTHING)
    dad = models.ForeignKey(Animal, models.DO_NOTHING, related_name='offspring_dad_set')
    child = models.ForeignKey(Animal, models.DO_NOTHING, related_name='offspring_child_set')

    class Meta:
        managed = False
        db_table = 'offspring'
    
    def __str__(self):
        return f"{self.child} offspring of {self.mom} and {self.dad}"

class ResponsibilityForAnimal(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, models.DO_NOTHING)
    worker = models.ForeignKey('Workers', models.DO_NOTHING)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsibility_for_animal'

    def __str__(self):
        return f"{self.animal} is responsible for {self.worker}"


class Sellers(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'sellers'

    def __str__(self):
        return self.name


class TypeAnimal(models.Model):
    name = models.TextField()
    predator = models.BooleanField()
    need_warm = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'type_animal'

    def __str__(self):
        return self.name


class VaccinationsAndDiseases(models.Model):
    animal = models.ForeignKey(Animal, models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'vaccinations_and_diseases'

    def __str__(self):
        return f"{self.animal}: {self.name}"

class Workers(models.Model):
    name = models.TextField()
    wages = models.IntegerField()
    male = models.BooleanField()
    age = models.IntegerField()
    profession = models.TextField()
    date_appointment = models.DateField()
    date_layoff = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers'

    def __str__(self):
        return self.name
