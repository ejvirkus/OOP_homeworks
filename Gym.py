class Trainers:
    def __init__(self, stamina:int, color:str):
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        trainers_response = 'Trainers: [' + self.stamina + ',' + self.color + ']'
        return trainers_response
    
class Member:
    def __init__(self, name:str, age:int, trainers:Trainers):
        self.name = name
        self.age = age
        self.trainers = trainers
        self.__gym_list = []

    def get_all_gyms(self):
        return self.__gym_list

    def get_gyms(self):
        pass

    def __repr__(self):
        member_response = self.name + ',' + self.age + ':' + self.trainers
        return member_response
    
class Gym:
    def __init__(self, name:str, max_members_number:int):
        self.name = name
        self.max_members_number = max_members_number
        self.member_list = [[],[],[]]
    
    def add_member(self, member: Member) -> Member:
        if self.max_members_number < len(self.member_list):
            self.member_list[0].append(member.name)
            self.member_list[1].append(member.trainers)
            self.member_list[2].append(member.age)
            print(member, " added!")
            return f'{member}'
        else:
            return f'Gym full'
    
    def can_add_member(self):
        if len(self.member_list) < self.max_members_number:
            return f'A new member can be added'
        else:
            return f'Gym full'

    def remove_member(self, member:Member):
        if member in self.member_list:
            self.member_list.remove(member)

    def get_total_stamina(self):
        return sum(self.stamina_list)

    def get_members_number(self):
        return len(self.member_list)

    def get_all_members(self):
        return self.member_list

    def get_average_age(self):
        return (sum(self.age_list)/len(self.age_list))

    def __repr__(self):
        gym_response = 'Gym ' + self.name + ':' + len(self.member_list) + 'member(s)'   
        return gym_response
class City:
    def __init__(self, max_gym_number:int):
        self.max_gym_number = max_gym_number
        self.gym_list = []
        self.gym_members_number_list = []

    def build_gym(self, gym: Gym) -> Gym:
        if len(self.gym_list) < self.max_gym_number:
            self.gym_list.append(gym)
            return f'{gym}'
        else:
            return f'gym limit reached'

    def can_build_gym(self):
        if len(self.gym_list) < self.max_gym_number:
            return f'A new gym can be added'
        else:
            return f'Gym limit reached'

    def destroy_gym(self, gym:Gym):
        if gym in self.gym_list:
            self.gym_list.remove(gym)

    def get_max_members_gym(self) -> list:
        pass

    def get_max_stamina_gym(self) -> list:
        pass

    def get_max_average_ages(self) -> list:
        pass

    def get_min_average_ages(self) -> list:
        pass

    def get_gyms_by_trainers_color(self, color:str) -> list:
        pass

    def get_gyms_by_name(self, name:str) -> list:
        pass

    def get_all_gyms(self) -> list:
        return self.gym_list

if __name__ == '__main__':
    trainers1 = Trainers(67, "Blue")
    member1 = Member("Jaanus", 25, trainers1)
    gym1 = Gym("Golds", 55)
    gym1.can_add_member()
    gym1.add_member(member1)