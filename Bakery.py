class Pastry:
    def __init__(self, name:str, complexity_level:int):
        self.name = name
        self.complexity_level = complexity_level

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Baker:
    def __init__(self, name:str, experience_level:int, money:int):
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __str__(self):
        return f'Baker: {self.name}({self.experience_level})'

    def __repr__(self):
        return self.__str__()
    
class Bakery:
    def __init__(self, name:str, min_experience_level:int, budget:int):
        self.__name = name
        self.__min_experience_level = min_experience_level
        self.__budget = budget
        self.bakers = []
        self.recipes = []
        self.pastries = []
        
    def add_baker(self, baker: Baker) -> Baker:
        if isinstance(baker, Baker) and \
        baker not in self.bakers and \
        self.__min_experience_level <= baker.experience_level:
            self.bakers.append(baker)
            assert baker.experience_level >= self.__min_experience_level, f'Baker has too low experience level'
            return f'{baker}'
        else:
            return f'None'

    def add_recipe(self, name:str):
        recipe_price = len(name)
        if self.__budget - recipe_price > 0 and \
        len.self.__bakers != [] and \
        name not in self.recipes:
            self.__budget -= recipe_price
            complexity_level = abs(recipe_price * len(self.bakers) - min([baker.experience_level for baker in self.bakers]))
            self.recipes[name] = complexity_level
            self.recipes.append(name)
            return f'Recipe added'
        else:
            return f'None'
            

    def make_order(self, name:str) -> Pastry:
        

        if name in self.recipes.keys():
            pass

    def remove_baker(self, baker: Baker):
        if baker in self.bakers:
            self.bakers.remove(baker)

    def get_recipes(self) -> dict:
        return self.recipes

    def get_bakers(self) -> Baker:
        return self.bakers

    def get_pastries(self) -> Pastry:
        return self.pastries

    
if __name__ == '__main__':
    pastry1 = Pastry("cake", 100)
    pastry2 = Pastry("tart", 50)
    print([pastry1, pastry2])

    baker1 = Baker("Bob", 75, 100)
    baker2 = Baker("Alice", 100, 150)
    print([baker1, baker2])

    bakery1 = Bakery("Rongu Pagarid", 25, 500)
    bakery1.add_baker(baker2)
    print(bakery1.get_bakers())