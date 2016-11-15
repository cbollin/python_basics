# print 'Hello World'
#
# greeting = 'Whats your name'
# print greeting
# name = raw_input()
# print 'how old are ya?'
# age = input()
#
# print 'your name is', name
# print 'you are', age, 'years old'

# raw_input('\n\nPress the enter key to exit')

# first_name = 'Zen'
# last_name = 'Coder'
# print 'My name is {} {}'.format(first_name, last_name)
#
# my_string = 'hello world'
# print my_string.capitalize()
#
# my_string = 'hello WORLD'
# print my_string.lower()
#
# my_string = 'hello WORLD'
# print my_string.swapcase()
#
# my_string = 'hello world'
# print my_string.upper()
#
# my_string = 'hello world'
# print my_string.find('el')
#
#
# my_string = 'hello world'
# print my_string.replace('world', 'kitty')
#
# my_string = 'egg, egg, egg, Spam, egg and Spam'
# print my_string.replace('egg', 'Spam', 2)
#
#
# x = [1,2,3,4,5]
# x.append(99)
# print x
#
# x = [1,2,3,4,5]
# x.insert(2,99)
# print x
#
# x = [1,2,3,4,5]
# x.remove(3)
# print x
#
# x = [1,2,3,4,5]
# x.pop()
# print x
#
# y = [10,11,12,13,14]
# y.pop(1)
# print y
#
# x = [99,4,2,5,-3];
# x.sort()
# print x
#
# x = [99,4,2,5,-3];
# print x[:]
# print x[1:]
# print x[:4]
# print x[2:4]
#
# for num in range(1,1001):
#     if num % 2 != 0:
#         print num
#
# for num in range(5, 1000001):
#     if num % 5 == 0:
#         print num

# a = [1,2,5,10,255,3]
# sum = 0
# for x in a:
#     sum += x
# print sum

# b = [1,2,5,10,255,3]
# sum = 0
# for x in b:
#     sum += x
# avg = sum / len(b)
# print avg

# Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the number and specify whether it's an odd or even number.
#
# def Looper(a, b):
#     for x in range(a, b):
#         if x % 2 == 0:
#             print x, "is even"
#         elif x % 2 != 0:
#             print x, "is odd"
# Looper(1,11)

# def multiply(a, c):
#     b = []
#     for x in a:
#         b.append(x * c)
#     return b
# t = multiply([2,4,10,16], 5)
# print t

# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this...

# for x in range(0,10):
#     print "please enter a score"
#     score = input()
#     if score <= 59:
#         print "Score: ", score, "Your Grade is F"
#     elif score <= 69 and score >= 60:
#         print "Score: ", score, "Your Grade is D"
#     elif score <= 79 and score >= 70:
#         print "Score: ", score, "Your Grade is C"
#     elif score <= 89 and score >= 80:
#         print "Score: ", score, "Your Grade is B"
#     elif score >= 90 and score <= 100:
#         print "Score: ", score, "Your Grade is A"
# print "End of the program bye!"

# import random
#
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1

# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
#
# count = 0
# headscount = 0
# tailscount = 0
# for x in range(0, 10):
#     random_num_new = round(random.random())
#     count = count + 1
#     if random_num_new == 0:
#         headscount += 1
#         print "Attempt # {} : Throwing a coin... It's a tail! ..Got {} tail(s) so far and {} head(s) so far!".format(count, tailscount, headscount)
#     if random_num_new == 1:
#         tailscount += 1
#         print "Attempt # {} : Throwing a coin... It's a head! ..Got {} tail(s) so far and {} head(s) so far!".format(count, tailscount, headscount)
# print "Ending the program thank you!"

# def drawstars(list):
#     for x in list:
#         if type(x) is str:
#             print x[0].lower() * len(x)
#         else:
#             print "*" * x
# drawstars([1,2,3,"Tom", "ASDF"])

# users = {
#  'Students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
#
# for key, data in users.items():
#     print "\n%s" %key.title()
#     counter = 0
#
#     for value in data:
#         counter = counter + 1
#         full_name = value['first_name'] + " " + value['last_name']
#         full_name_upper = full_name.upper()
#         name_count = len(value['first_name']) + len(value['last_name'])
#
#         print "%d - %s - %d" %(counter, full_name_upper, name_count)
#
#
# import random
# def bubble_sort(my_list):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(my_list) - 1):
#             if my_list[i] > my_list[i + 1]:
#                 my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
#                 swapped = True
#     return my_list
#
# random_list = [random.randint(0, 10) for count in range(10)]
#
# print(random_list)
# print(bubble_sort(random_list))
