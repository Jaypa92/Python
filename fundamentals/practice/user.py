class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points <= 0:
            print("Not enough points!")
            self.gold_card_points = self.gold_card_points + amount
        return self


john = User("John", "Green", "j.green1@aol.com", 31)
john.display_info().enroll().spend_points(50).enroll().display_info()
# # john.enroll()
donnie = User("Donnie", "Walden", "d.walden@gmail.com", 50)
tina = User("Tina", "Murray", "t.murray@outlook.com", 60)
donnie.enroll().spend_points(80).display_info().spend_points(200)
tina.display_info()
# # john.spend_points(50)
# print(john.gold_card_points)
# donnie.enroll()
# donnie.spend_points(80)
# john.display_info()
# donnie.display_info()
# tina.display_info()
# john.enroll()
# donnie.spend_points(200)
