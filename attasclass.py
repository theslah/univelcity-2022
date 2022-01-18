#for i in range(10):
    #for j in range(10):
        # print(i, ":", j)

#for i in range(10):
    #for j in range(10):
        #for s in range(60):
            #print(i, ":", j, ":", s)

#for i in range(10):
    #for j in range(10):
       # for s in range(60):
            #for n in range(60):
               # print(i, ":", j, ":", s, ":", n )

#for i in range(10, 0, -1):
    #for j in range(10, 0, -1):
        #for s in range(60, 0, -1):
            #for n in range(60, 0, -1):
                #print(i, ":", j, ":", s, ":", n )

#for i in range(1, 1000):
 #   sum_num = i + i + i
  #  placeholder = str(i)[-1]
   # triple_holder= placeholder * 3
    #if int(triple_holder) == sum_num:
        #print("hurray our num is : ", i, "->", sum_num)
        #break
   # print(i, sum_num)

#def useless():
    
 #   for i in range(10):
  #      for j in range(10):
   #         for s in range(60):
    #            print(i, ":", j, ":", s)
#useless()


#def useless2(hours, mins, secs):
    
 #   for i in range(hours+1):
  #      for j in range(mins+1):
   #         for s in range(secs+1):
    #            print(i, ":", j, ":", s)
#useless2(2, 10, 6)

def increment(num):
    return num + 2

def restructure(hours, mins, secs):
    return f"{hours}hours {mins}mins {secs}secs"

def useless2(hours, mins, secs):
    
    for i in range(increment(hours)):
        for j in range(increment(mins)):
            for s in range(increment(secs)):
                print(restructure(i,j,s))
#useless2(2, 10, 6)

import random as rd
import time

# def collect_data():

#     guess = input("enter number here: ")
#     name = input("input name: ")
#     guess = guess.split(" ")
#     number = map(lambda a: int(a), guess)
#     num = list(number)
#     #print(num) 

#     rand = rd.randrange(num[0], num[1])
#     #print(rand)

#     return rand, name

# def play_game():
#     tries = 0 #add a counter and makes it empty at first

#     rand, name = collect_data()

#     while True:
#         guess2 = input("guess number here: ")
#         guess2 = int(guess2) #type casting
#         tries += 1 #increment at every trial
#         if rand == guess2:
#             print("winner")
#             break
#         elif guess2 < rand:
#             print("hint: your number is less")
#         elif guess2 > rand:
#             print("hint: your number is more")
#         else:
#             pass
# write_to_file(name, tries)
# print("you tried :", tries, "times") #print tries 

# def write_to_file(name, tries):
#     with open("database.csv", "a")as our_log_file: # file open context manager
#         our_log_file.write(f"{name}, {tries}")
#     print("logged session")
# #play_game()   
# #write_to_file("bridget", 5)


# # set limit to 10 tries max and then delay with 10 secs
# def collect_data():

#     guess = input("enter number here: ")
#     name = input("input name: ")
#     guess = guess.split(" ")
#     number = map(lambda a: int(a), guess)
#     num = list(number)
#     #print(num) 

#     rand = rd.randrange(num[0], num[1])
#     #print(rand)

#     return rand, name

# def play_game():
#     tries = 0 #add a counter and makes it empty at first

#     rand, name = collect_data()

#     while True:
#         guess2 = input("guess number here: ")
#         guess2 = int(guess2) #type casting
#         tries += 1 #increment at every trial
#         limit += 1

#         if rand == guess2:
#             print("winner")
#             break
#         elif guess2 < rand:
#             print("hint: your number is less")
#         elif guess2 > rand:
#             print("hint: your number is more")
#         if limit == 10:
#             print("you missed it", tries, "times")
#             print("we are now delaying")
#             limit = 1
#             time.sleep(10)

# write_to_file(name, tries)
# print("you tried :", tries, "times") #print tries 

# def write_to_file(name, tries):
#     with open("database.csv", "a")as our_log_file: # file open context manager
#         our_log_file.write(f"{name}, {tries}")
#     print("logged session")
# #play_game()   
# #write_to_file("bridget", 5)


# #OOPS
# class HumanKind: # class creation     
#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"
# human_kind_object = HumanKind() # object creation class instantiation
# print(human_kind_object)

# print(HumanKind.skin)
# print(HumanKind.species)

# #using in a for loop
# object =[]
# for i in range (1000):
#     objects.append(HumanKind())
# print(object[105 ])

# class HumanKind: # class creation     
#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

#     def describe(self):
#         print(f"hello my species is {self.species}")

#     def makenoise(self):
#         print("hello !!!")
#         winsound.Beep(2000, 500)
#         time.sleep(1)
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(3000, 500)


#varname = HumanKind()
#varname.describe()
#varname.makenoise()

#pip install winsound to make sound

##task

# class Cat:
#     name = "snuggles"
#     furcolour = "white"
#     family = "ragdoll"

#     def feline(self):
#         print(f"hello i am a cat, my fur colour is {self.furcolour} and my name is {self.name}")

# specs = Cat()
# specs.feline()

##instance attributes
# methiclass Person():
#     species = "hommo-sapien"
#     _class  = "mammal"

#     def __init__(self, name, complexion, height) -> None:
#         self.name = name
#         self.complexion = complexion
#         self.height = height
#         self.voice_freq = random. randinit(50, 1500)

#     def say_something(self):
#          print(f"hello, my name is {self.name} i am a {self._class}, and my height is {self.height}")
#          winsound.Beep(self.voice_freq, 500)
#          time.sleep(0.5)
#          winsound.Beep(self.voice_freq, 500)
#          time.sleep(0.5)
#          winsound.Beep(self.voice_freq, 500)

# person1 = person(name = "ade", complexion = "brown skin", height = "5ft7")
# person1.say_something()

# person2 = person(name = "segun", complexion = "fair skin", height = "6ft2")
# person2.say_something

 ### oop continued by dami
# class student:
#     def __init__(self, name, gender, age):
#         self.name   = name
#         self.gender = gender
#         self.age    = age

#     def get_name(self):
#         return self.name

#     def get_gender(self): 
#         return self.gender

#     def get_age(self):
#         return self.age

#     def set_name(self, value): # mutator instance
#         self.name = 

#     def set_gender(self, value):
#         self.gender = value

#     def set_age(self, value):
#         self.age = value

# stu_one   = student("kelsey", "female", 22)
# stu_two   = student("brian", "male", 35)
# stu_three = student("ernie", "male", 27)

# #print(stu_one.get_name())
# print(stu_two.set_age())
# stu_two.set_age(33)
# print(stu_two.get_age())

class school: ## including class attribute and class method
    no_of_students = 0 ##attribute
    sum_of_scores = 0

    def __init__(self, student_name, student_score):
        self.student_name = student_name
        self.student_score = student_score
        school.increase_count()
        school.sum_of_scores += self.get_student_scores( )

    def get_student_name(self):
        return self.student_name  ###return can have multiple lines codes
  
    def get_student_scores(self):
        return self.student_score

    def set_student_name(self, value):
        self.student_name = value

    def set_student_score(self, value):
        self.student_score = value

#classmethod
    def increase_count(cls):
         cls.no_of_students += 1
 
    def average_score(cls):
        output = cls.sum_of_scores / cls.no_of_students
        return round(output, 2)

edu_one = school("emeka", 24.56)
edu_one.increase_count()
print(school.no_of_students)
edu_two = school("oluwagbemisola", 99.00)
edu_two.increase_count()
print(school.no_of_students)
print(school.average_score)

instance_collection = [school("ifeoma", 64.22), school("musa", 76.75), school("bamishe", 58.40)]
print(instance_collection[1].get_student_scores())

                    

















