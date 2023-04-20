class Trainers:
    def __init__(self, stamina:int, color:str):
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        return f'Trainers: [{self.stamina}, {self.color}]'
    
class Member:
    def __init__(self, name:str, age:int, trainers:Trainers):
        self.name = name
        self.age = age
        self.trainers = trainers
        self.__gym_list = []

    def get_all_gyms(self):
        return self.__gym_list

    def get_gyms(self):
        return [x.name for x in self.gyms]

    def __repr__(self):
        return f'[{self.name}], [{self.age}]: [{self.trainers}]'
    
class Gym:
    def __init__(self, name:str, max_members_number:int):
        self.name = name
        self.max_members_number = max_members_number
        self.member_list = []
    
    def can_add_member(self, member):
        if len(self.member_list) < self.max_members_number\
        and isinstance(member, Member)\
        and member.trainers != ''\
        and member.trainers.stamina >= 0\
        and member not in self.member_list:   
            return True
        elif len(self.member_list) >= self.max_members_number\
        and isinstance(member, Member)\
        and member.trainers != ''\
        and member.trainers.stamina >= 0\
        and member not in self.member_list:
            remove_list = []
            for member in self.member_list:
                if member.trainers.stamina == min(member.trainers.stamina for member in self.member_list):
                    remove_list.append(member)
            for member in remove_list:
                self.remove_member(member)
            return True

        else:
            return False
    
    def add_member(self, member: Member) -> Member:
        if self.can_add_member(member) == True:
            self.member_list.append(member)
            return f'{member}'
        else:
            return f'Gym full'

    def remove_member(self, member:Member):
        if member in self.member_list:
            self.member_list.remove(member)

    def get_total_stamina(self) -> list:
        stamina = 0
        for member in self.member_list:
            stamina += member.trainers.stamina
        return stamina

    def get_members_number(self) -> list:
        return len(self.member_list)

    def get_all_members(self) -> list:
        return self.member_list

    def get_average_age(self) -> list:
        age = 0
        for member in self.member_list:
            age += member.age
            average_age = age / len(self.member_list)
        return round(average_age, 2)

    def __repr__(self):
        return f'Gym: [{self.name}] : [{len(self.member_list)}] member(s)'
    
class City:
    def __init__(self, max_gym_number:int):
        self.max_gym_number = max_gym_number
        self.gym_list = []

    def can_build_gym(self, gym) -> bool:
        if len(self.gym_list) < self.max_gym_number\
        and gym not in self.gym_list :
            return True
        else:
            return False

    def build_gym(self, gym: Gym) -> Gym:
        if self.can_build_gym(gym) == True:
            self.gym_list.append(gym)
            return f'{gym}'
        else:
            return f'gym limit reached'

    def destroy_gym(self, gym:Gym):
        if gym in self.gym_list:
            self.gym_list.remove(gym)

    def get_max_members_gym(self) -> list:
        for gym in self.gym_list:
            if gym.get_members_number() == max([gym.get_members_number() for gym in self.gym_list]):
                return gym.name
                
    def get_max_stamina_gym(self) -> list:
        for gym in self.gym_list:
            if gym.get_total_stamina() == max([gym.get_total_stamina() for gym in self.gym_list]):
                return gym.name

    def get_max_average_ages(self) -> list:
        for gym in self.gym_list:
            if gym.get_average_age() == max([gym.get_average_age() for gym in self.gym_list]):
                return gym.name
            
    def get_min_average_ages(self) -> list:
        for gym in self.gym_list:
            if gym.get_average_age() == min([gym.get_average_age() for gym in self.gym_list]):
                return gym.name

    def get_gyms_by_trainers_color(self, color:str) -> list:
        Gyms_with_color = [gym.name for gym in self.gym_list for gym.member in gym.member_list if gym.member.trainers.color == color]
        gym_name = {}
        for color in Gyms_with_color:
            if color in gym_name:
                gym_name[color] += 1
            else:
                gym_name[color] = 1
        return sorted(set(Gyms_with_color), key=lambda x: gym_name[x], reverse=True)

    def get_gyms_by_name(self, name:str) -> list:
        Gyms_with_name = [gym.name for gym in self.gym_list if gym.name == name]
        gym_name = {}
        for name in Gyms_with_name:
            if name in gym_name:
                gym_name[name] += 1
            else:
                gym_name[name] = 1
            return sorted(set(Gyms_with_name), key=lambda x: gym_name[x], reverse=True)

    def get_all_gyms(self) -> list:
        return self.gym_list

if __name__ == '__main__':
    trainers1 = Trainers(67, "Blue")
    trainers2 = Trainers(30, "Red")
    trainers3 = Trainers(100, "Acqua")

    member1 = Member("Andrus", 43, trainers1)
    member2 = Member("Mati", 41, trainers2)
    member3 = Member("Annela", 23, trainers3)

    gym1 = Gym("Golds", 2)
    gym2 = Gym("247", 70)

    gym1.add_member(member1)
    gym1.add_member(member2)
    print(gym1.add_member(member3))
    #gym2.add_member(member1)
    
    #print(gym1.can_add_member())
    print(gym1.get_all_members())
    #print(gym1.get_total_stamina())
    #print(gym1.get_members_number())
    #print(gym1.get_average_age())

    city1 = City(27)
    print(city1.build_gym(gym1))
    print(city1.build_gym(gym2))
    #print(city1.get_max_members_gym())
    #print(city1.get_max_stamina_gym())
    #print(city1.get_max_average_ages())
    #print(city1.get_min_average_ages())
    #print(city1.get_gyms_by_trainers_color("Blue"))
    #print(city1.get_gyms_by_name("Golds"))
    #print(city1.get_all_gyms())
