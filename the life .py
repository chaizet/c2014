import random
class Human:
      def __init__(self,name="Human",car=None,home=None,job=None):
          self.name=name
          self.money=100
          self.gladness=50
          self.satiety=50
          self.job=job
          self.home=home
          self.car=car

      def get_home(self):
          self.home=House()
      def get_car(self):
       self.car=Auto(brand_of_car)
      def get_job(self):
          self.car=Auto(brand_of_car)
          self.car.drive():
          pass
          else:
          self.to_repair()
        return
        self.job = job(job_list)

      def eat(self):
          if self.home.food<=0
              self.shopping("food")
      else:
          if self.satiety>=100:
              self.satiety=100
              return
      def work(self):
          pass
      def shopping(self,manage):
          pass
      def to_repair(self):
          pass
      def clean_home(self):
          pass
      def chill(self):
          pass
      def days_indexes(self,day):
          pass
      def is_alive(self):
          pass
      def live(self):
          pass

class auto:
    def __init__ (self, brand_list):
        self.brand=random.choice(list(brand_list))
        self.hp = brand_list[self.brand]["hp"]
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.hp>0 and self.fuel>self.consumption:
            self.fuel-=self.consumption
            self.hp-=1
            return True
        else:
            print(" the car can not move")
            return False

class House:
    def __init__(self):
        self.mess=0
        self.food=0
brand_of_car={
    "bmw": {"fuel": 100, "hp": 100, "consumption": 12},
    "toyota": {"fuel": 50, "hp": 60, "consumption": 10},
    "volvo": {"fuel": 70, "hp": 120, "consumption": 8},
    "porsche": {"fuel": 80, "hp": 150, "consumption": 14}}

job_list={
    "java developer":{"salary":50, "gladness_less":10},
    "python developer": {"salary": 40, "gladness_less": 3},
    "c++ developer": {"salary": 45, "gladness_less": 25},
    "rust developer": {"salary": 70, "gladness_less": 1}}
class job:
        def __init__(self,job_list):
            self.job=random.choice(list(job_list))
            self.salary=job_list[self.job]["salary"]
