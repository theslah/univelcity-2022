first_integer = 99
#print(first_integer)

real_life = "this stuff is sort of confusing"
#print(real_life)

my_verdict = True
#print(my_verdict)

randoms = [5, "aiko", "big", True, 2.56]
#print(randoms)

states = {"abia", "kogi", "abuja"}
#print(states)

my_info = {"name" : "lola", "gender" : "female", "age" : "22"}
#print(my_info)

the_reminder = 55 % 6
#print(the_reminder)

the_quotent = 55 // 6
#print(the_quotent)

the_exponential = 6 ** 3
#print(the_exponential)

comparison = 59 == 91
#print(comparison)

logical = (22 >= 71) or (92 != 92)
#print(logical)

logical_2 = (22 == 22) and (92 >= 80)
#print(logical_2)

feedback = 25 is 25
#print(feedback)

first = [29, "true", "sunny"]
second = [29, "true", "sunny"]
#print(first)
#print(second)
third = first is second
#print(third)

check_member = "e" in "money"
#print(check_member)

list_of_scores = [63, 78, 90, 52, 99, 81]
check_score = 90 in list_of_scores
#print(check_score)

first_phrase = "the boy"
second_phrase = "in my class is handsome"
full_sent = first_phrase + " " + second_phrase
#print(full_sent)
new_chunck = full_sent[3:11]
#print(new_chunck)
new_chunk = first_phrase[ : : 2]
#print(new_chunk)
new_chunk = full_sent[-23 : -12]
#print(new_chunk)

##formatting
weather = "sunny"
temperature = "39 degrees"
#weather_report = "it is quite {} with a temperature of {}".format(weather)
#print(weather_report)

weather_report2 = f"it is quite {weather} with a temperature of {temperature}"
#print(weather_report2)

new_weather_report = "!it's quite sunny despite the downpour"
mod_one = new_weather_report.title()
#print(mod_one)

mod_two = new_weather_report.startswith("!it")
#print(mod_two)

mod_three = new_weather_report.index("sunny")
#print(mod_three)

mod_four = new_weather_report.find("sunny")
#print(mod_four)

mod_five = new_weather_report.split(" ")
#print(mod_five)

mod_six = new_weather_report.split("downpour")
#print(mod_six)

mod_seven = ",".join(mod_five)
#print(mod_seven)^

mod_eight = new_weather_report.count("the")
#print(mod_eight)

mod_nine = new_weather_report.replace("p", "e")
#print(mod_nine) 

mod_ten = new_weather_report.strip("t")
#print(mod_ten) *

new_collection = [6, True, 12, 9, False, "name", "bentley"]
desired_item = new_collection[4]
#print(desired_item)

#desired_portion = new_collection[-6: -2: 2]
#print(desired_portion)

new_collection[5] = "school"
#print(new_collection)

#new_collection[1 : : 3] = ["money", "food", "ikoyi", "glass"]
#print(new_collection)

first_list = [1, 2, 3]
second_list = [7, 8, 9]
full_list = first_list + second_list
#print(full_list)

sports = ["basketball", "boxing", "swimming"]
stars = ["kobe bryant", "mike tyson", "micheal phelps"]
sports.extend(stars)
#print(sports)

new_collection.remove(9)
#print(new_collection)

new_collection.append("biscuits")
#print(new_collection)

backup_collection = new_collection.copy()
#print(backup_collection)

new_collection.insert(2, "holiday")
#print(new_collection)

integers = [2, 4, 7, 6, 8]
integers.sort(reverse = True)
#print(integers) *

###TUPLES
scores = (58, 73, 85, 67)
desired_score = scores[-1]
#print(desired_score)

first_tuple = (False, "true", 100)
second_tuple = (1, 4, 9)
full_tuple = first_tuple + second_tuple
#print(full_tuple)

###set
grocery_cart1 = {"ham", "burger", "yogurt", "eggs", "cookies"}
grocery_cart2 = {"beverage", "cookies", "wine", "frozen turkey"}
#print(grocery_cart1)
#print(grocery_cart2)

grocery_cart1.discard("ham")
grocery_cart1.add("cheese")
#print(grocery_cart1)

full_cart = grocery_cart1.union(grocery_cart2)
#print(full_cart)

grocery_cart1.update(grocery_cart2)
#print(grocery_cart1)

#grocery_cart2.difference_update(grocery_cart1)
#print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
#print(common_groceries)

grocery_cart1.symmetric_difference_update(grocery_cart2)
#print(grocery_cart1)

###dict
customer_info = {
    "name" :["Adam Freeman", "Alisa Banks", "Ngozi chukuka"],
    "gender" :["Male", "Female", "Female"],
    "Nationality" :["American", "Canadaian", "Nigerian"]
}
#print(customer_info)
all_names = customer_info["name"]
#print(all_names)
all_names[2] = "Ngozi Amadi"
#print(customer_info)
all_nationalities = customer_info.get("Nationality")
#print(all_nationalities)
all_entries = customer_info.items()
#print(all_entries)
customer_info.update({"age" :[31, 24, 30]})
#print(customer_info)

###builtinfunctions
#input
#get_data = input("enter data here: ")
#print(get_data)
#random = get_data.split(" ")
#print(random)
#int_1 = int(random[0])
#int_2 = int(random[1])
#average = (int_1 + int_2)/2
#print(average)

#len
scores= [55, 87, 93,71]
#no_of_scores = len(scores)
#print(no_of_scores)
#total_scores = sum(scores) #sum
#print(total_scores)
#print(min(scores)) #min
#print(max(scores)) #max
#see how len is used the other tasks during further study

#zip
name = ["john", "dave", "bill"]
age = [22, 24, 26]
zipped_info =list(zip(name, age))
#print(zipped_info)

#enumerate
animals = ["dog", "cat", "lion"]
no_of_animals = [5, 7, 10]
zipped_animals = zip(animals, no_of_animals) 
counter = list(enumerate(zipped_animals))
#print(counter)

#lambda see how lambda is used in the succeeding tasks
my_multiplier = lambda x, y, z : x * 2 - y
output = my_multiplier(20, 30, 40)
#print(output)

checker = lambda a : a.startswith("is")
output2 = checker("this is just a basic string")
#print(output2)

#map
upgraded_scores = map(lambda a : a + 2, scores)
output3 = list(upgraded_scores)
#print(output3)

list_of_names = ["steve", "dwayne", "freya", "nelson"]
checker2 = map(lambda a : a.title(), list_of_names)
output4 = list(checker2)
#print(output4)

#filter
num = [20, 31, 45, 60, 10, 77]
my_filter = filter(lambda x : x % 2, num)
#print(list(my_filter))

list_of_names = ["steve", "dwayne", "freya", "nelson", "sam", "john", "abu", "binta"]
my_filter = filter(lambda a : "a" not in(a), list_of_names)
#print(list(my_filter))

#range
my_range = range(-5, -1)
#print(list(my_range))

my_range = range(-5, -1, 2)
#print(list(my_range))

my_list = ["30", "33"]
new_list = str(["30", "33"])
#print(new_list[2])

# BUILTINMODULES
import time

#print("this is line 141")
#time.sleep(2)
# print("this is line 143")

import random as rd
rd.seed(99)
#print(num)
#print()
#rd.shuffle(num)
 #print(rd.shuffle(num))
#print(num)

random_picks = rd.choice(num)
#print(random_picks)

multiple_picks = rd.sample(num, k = 3)
#print(multiple_picks)

random_num = rd.randrange(9, 23, 3)
#print(random_num)

from datetime import datetime as dt

current_dt = dt.now()
#print(current_dt)

#output = current_dt.year
#print(output)

output = current_dt.strftime("%A")
#print(output)

fake_date = "9/4/2021"
real_date = dt.strptime(fake_date, "%d/%m/%Y")
#print(real_date)

#task
notable_days = ["01/01/2021", "15/01/2021", "14/02/2021", "01/04/2021", "29/05/2021", "12/06/2021", "01/10/2021", "25/12/2021", "26/12/2021"]
actual_days = list(map(lambda a : dt.strptime(a, "%d/%m/%Y"), notable_days))
#print(list(actual_days))
#print(actual_days[0])

#conditionals
#if 77 > 77:
    #print("Yes")
#else:
    #print("No")

#if "y" in "Rukayat":
    #print("spelt correctly")
#else:
    #print("incorrect")

#get_data = input("Enter data here:")

#if len(get_data) == len(set(get_data)):
    #print("There are no duplicates")
#else:
    #print:("There are duplicates")


#if int(get_data) % 2 == 0:
    #print("even number")
#else:
   # print("odd number")

#if int(get_data) % 2 == 0 and int(get_data) > 20:
    #print("both conditions are met")
#else:
   #print("they are not met")

 
#cracker = 0
#while(cracker < 5):
  #  print("cracker less than 5")
   # cracker += 1

###LOOPS
#cracker = 0
#while (cracker < 5):
    #if cracker == 3:
   #     print("this is my ride outta the loop!")
  #      break
#   else:
#        print("cracker is less than 5")
#       cracker += 1

###task
#get_password1 = input("enter password here: ")
#while True:
 #   get_password2 = input("repeat password here: ")
  #  if get_password1 == get_password2:
   #    print("sign up successful")
    #   break
    #else:
     #   pass

#get_password1 = input("enter password here: ")
#limit = 0
#while (limit < 2):
 #   get_password2 = input("repeat password here: ")
  #  if get_password1 == get_password2:
   #     print("login successful")
      #  break
    #else:
     #   limit += 1

#guess = input("enter number here: ")
#guess = guess.split(" ")
#number = map(lambda a: int(a), guess)
#num = list(number)
#print(num) 
#import random as rd
#rand = rd.randrange(num[0], num[1])
#print(rand)
#while True:
 #   guess2 = input("guess number here: ")
  #  guess2 = int(guess2)
   # if rand == guess2:
    #    print("winner")
     #   break
    #elif guess2 < rand:
     #   print("hint: your number is less")
    #elif guess2 > rand:
     #   print("hint: your number is more")
    #else:
     #   pass

#entry_data ="Universe"
#for a in entry_data:
 #   print("home for all!")

#entry_data = input("enter here: ")
#for a in entry_data:
    #print(a.)

#people = ["Sheldon", "Penny", "Howard", "Leonard", "Rajesh"]
#for index, item in enumerate(people):
 #   print(index, item)

#collection = input()
#collection = collection.split(" ")
#collection = map(lambda x : int(x), collection)
#collect = list(collection)
#print(collect)
#for index, entry in enumerate(collect):
 #   if entry % 2 == 0:
  #      collect[index] *= 0.9
   #     print(collect[index])
   # elif entry % 2 != 0:
    #    collect[index] *= 1.1
     #   print(collect[index])
    #else:
       # pass

### assignment
#get_data = input("enter integers here: ")
#con_list = get_data.split(" ")
#real_integers = list(map(lambda a : int(a), con_list))
#print(real_integers)
#odd_number = list(filter(lambda a : a % 2, real_integers))
#no_of_inputs = len(real_integers)
#no_of_odd = len(odd_number)
#no_of_even = no_of_inputs - no_of_odd
#print(f"there are {no_of_odd} odd numbers.")
#print(f"there are {no_of_even} even numbers")

#odd = 0
#even = 0
#for entry in real_integers:
 #   if entry % 2 == 0:
  #      even += 1
   # elif entry % 2 != 0:
    #    odd += 1
    #else:
     #   pass
#print(f"there are {odd} odd numbers.")
#print(f"there are {even} even numbers")

#inputs1 = input()
#inputs2= inputs1.split()
#inputs3 = "".join(input2)
#inputs4 = len(inputs3)

#digit = 76.5
#digit = str(digit)
#num = digit.replace(".", "")
#digit = digit.split(".")
#num = "".join(digit)
#con_num = list(map(lambda a : a.isdigit(), num))
#num_of_digits = len(con_num)
#print(num_of_digits)

#get_data = input("enter here: ")
#integers = get_data.split(" ")
#integers = list(integers)
#integers.reverse()
#print(integers)


#from datetime import datetime as dt

#get_date = input("enter date: ")
#update_hour = dt.now().hour
#update_hour = str(update_hour)
#update_min = dt.now().minute
#update_min = str(update_min)
#update_sec = dt.now().second
#update_sec = str(update_sec)
#date = get_date + "/" + update_hour + "/" + update_min + "/" + update_sec 
#final_date = dt.strptime(date, "%d/%m/%Y/%H/%M/%S")
#  print(final_date)

#list comprehension
#scores = [42, 53, 61, 81, 57]
#upgraded_scores = [num + 2 for num in scores]
#print(upgraded_scores)
#upgraded_scores = [num + 2 for num in scores if num % 2 != 0]
#print(upgraded_scores)

#new_input = [("high", 3), ("low", 2), ("nan", 6)]
#new_output =sorted(new_input, key = lambda a : a[1])
#print(new_output)

#for i in range(20, 0, -1):
    #print(i)

   





