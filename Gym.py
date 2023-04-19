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

    def get_all_gyms(self):
        pass

    def get_gyms(self):
        pass

    def __repr__(self):
        member_response = self.name + ',' + self.age + ':' + self.trainers
        return member_response
    
class Gym:
    def __init__(self, name:str, max_members_number:int):
        self.name = name
        self.max_members_number = max_members_number
        self.member_list = []
        self.stamina_list = []
        self.age_list = []
    
    def add_member(self):
        pass
    
    def can_add_member(self):
        pass

    def remove_member(self):
        pass

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
        gym_list = []

    def build_gym(self):
        pass

    def can_build_gym(self):
        pass

    def destroy_gym(self):
        pass

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
        pass
