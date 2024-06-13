# დავალება 6
# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.



from abc import ABC, abstractmethod

class Country(ABC):
    @abstractmethod
    def get_budget(self):
        pass

    @abstractmethod
    def get_population(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Georgia(Country):
    def __init__(self, budget, population, area):
        self.budget = budget
        self._population = population
        self.__area = area

    def get_budget(self):
        return self.budget

    def get_population(self):
        return self._population

    def get_area(self):
        return self.__area

georgia = Georgia(100000000, 3400000, 70000)

print("Budget of Georgia:", georgia.get_budget())
print("Population of Georgia:", georgia.get_population())
print("Area of Georgia:", georgia.get_area())
