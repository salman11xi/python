# time=int(input("soo gali inta saac aad shaqeysid : "))
# mushaar=int(input(" soo gali musharkaga : "))
# if time > 40 :
    
#     a = 1.5;
#     b = 40
#     overtime = time - b
#     oversalary = overtime * mushaar * a
#     normalsalry = mushaar * b
#     realsalary = normalsalry + oversalary
#     print("mushaarka dheerigaa waa :",realsalary,"$")
    
# else:
#     salary = time * mushaar
    
#     print("mushaarka waa :",salary,"$")

# temp = eval(input( 'Enter number: '))
# print("the square of 5 is : ",temp*temp)



# name = {"10","20","30"}
# for i in range(2,len(name)):
#     print(name)

# for i in range(4):
#     print("*"*(1+i))

# for i in range(5):
#     print("*"*(5-i))

# for i in range(3):
    
#     num = eval(input("enter a number :"))
#     print("the square o your number is : ", num*num)
    
# for i in range(1,10):
#     print(i)
# from random import randint
# x = randint(1,10)
# print( 'A random number between 1 and 10: ', x)

# grade = eval(input("Enter your score for the grade : "))
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("F")
# else:
#     print("failed")
    
# count1 = 0
# count2 = 0
# for i in range(2):
#     num = eval(input( 'Enter a number: '))
# if num>10:
#     count1=count1+1
# if num==0:
#     count2=count2+1
# print( 'There are ', count1, 'numbers greater than 10. ')
# print( 'There are ', count2, 'zeroes. ')

# numbers = [0]*6
# for index in range(len(numbers)):
#     numbers[index]=99
#     print(numbers)

# num = [1,2,3,4,]
# for i in range(len(num)):
#     print(num[i])
# d = {1,2,3,4}
# print(len(d)) 

# num=list(range(1,10,2))
# for n in num:
#    print(n)


# import os
# os.system("shutdown now -h")


# name = "sub zero"
# print(name.title())

# first_name = "ada"
# last_name = "lovelace"

# full_name =f"{first_name} {last_name}"
# full_name = first_name + last_name
# print(full_name)


# motorcycles =["honda","yamaha","suzuki"]
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles[0].title())
# print(motorcycles)

# f = open("python.txt", "a") # Append to an existing file
# f.write("The file will include more text..")
# f.close()

# g = open("filepy.txt","w")
# g.write("filepy file created, with this content in! ")
# g.close()

# f = open("filepy.txt","r")
# print(f.read())

# name = "fileptxt"
# if name == f :
#     print(f.read())
# else:
#     print("file is not found")

# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
# for key, value in user_0.items():
#  print(f"\nKey: {key}")
#  print(f"Value: {value}")
 
 
# favorite_languages = {
#  'subzero': 'python',
#  'phil': 'python',
#  'sarah': 'c',
#  }
# for magaca, luuqada in favorite_languages.items():
#  print(f"{magaca.title()}'s favorite language is {luuqada.title()}.")
#    print(luuqada.title())

# friends = {'phil','sarah'}
# for magaca in favorite_languages.keys():
#  print(magaca.title())
 
# if magaca in friends:
#     luuqada = favorite_languages[magaca].title()
#     print(f"\t{magaca.title()},wxaa arkay luuqadada {luuqada}")



# friends = ['sarah', 'subzero']
# for name in favorite_languages.keys():
#  print(name.title())

# if name in friends:
#  language = favorite_languages[name].title()
#  print(f"\t{name.title()}, I see you love {language}!")


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#  print(alien)


# def get_formatted_name(first_name, last_name):
# # ""Return a full name, neatly formatted."""
#  full_name = f"{first_name} {last_name}"
#  return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formatted_name(first_name, last_name):
#      """Return a full name, neatly formatted."""
#      full_name = f"{first_name} {last_name}"
#      return full_name.title()
# while True:
#      print("Enter u name ")
#      f_name = input("frist name : ")
#      if f_name == 'q':
#          break
#      l_name = input("last name  :")
#      if l_name == 'q':
#              break
#      fullname = get_formatted_name(f_name,l_name)
#      print("full name is {fullname}")
     
# def greet_users(names):
#      """Print a simple greeting to each user in the list."""
#      for name in names:
#        msg = f"Hello, {name.title()}!"
#        print(msg)
# usernames = ['farax', 'Ali', 'Geele']
# greet_users(usernames)    
    

# def full_names(name1,name2,name3):
    
#     names = full_names(n1,n2,n3)
#     return names

# for i in range(1):
#         n1 = input("name1 : ")
#         n2 = input("name 2 :")
#         n3 = input("name 3 :")
#         all_names = n1+n2+n3
# print(f"names{all_names}")

# def build_profile(first, last, **user_info):
#         # """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
#  location='princeton',
#  field='physics')
# print(user_profile)


# class Dog:
#     # v """A simple attempt to model a dog."""

#  def __init__(self, name, age):
# #  """Initialize name and age attributes."""
#   self.name = name
#   self.age = age

#  def sit(self):
# #  """Simulate a dog sitting in response to a command."""
#     print(f"{self.name} is now sitting.")
#  def roll_over(self):
# #  """Simulate rolling over in response to a command."""
#     print(f"{self.name} rolled over!")
    
name = ""
while(True):
    name = input("Entert you name ")
    if name == "exit":
        break;
    print("Name :" + name)

