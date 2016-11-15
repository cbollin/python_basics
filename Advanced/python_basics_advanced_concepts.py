# def varargs(arg1, *restOfArg):
#     print "Got " + arg1 + " and " + ", ".join(restOfArg)
#
# varargs("one")
# varargs("one", "two")
# varargs("one", "two", "three")
#
# class MathDojo(object):
#     def __init__(self):
#         self.sum = 0
#
#     def add(self, *restOfArg):
#         for i in restOfArg:
#             if type(i) == int:
#                 self.sum += i
#             else:
#                 for j in i:
#                     self.sum += j
#         return self
#
#     def subtract(self, *restOfArg):
#         for i in restOfArg:
#             if type(i) == int:
#                 self.sum -= i
#             else:
#                 for j in i:
#                     self.sum -= j
#         return self
#     def result(self):
#         print self.sum
#         return self
# md = MathDojo()
# md.add(1,[2,3],(4,5.6)).subtract(1,[2,3],(4,5)).result()
#
# stacks = 4
# print("Coding is totally sweet" if stacks >= 3 else "You dont know jack!")
#
# add = lambda num1, num2: num1 + num2
# print(add(3,4))
#
# # first param of map is a function , second param is actual argument we're passing in
# result = map(lambda x:x**2, [1,2,4,99])
# print(list(result))
# print(result)
#
# my_list = ["test_string", 99, lambda x:x**2]
# print my_list[2]
# my_list[2](5)
# # passing 5 into our lambda
#
def invoker(callback):
    print callback(2)
invoker(lambda x: 2*x)
invoker(lambda y: 3+y)
# passing the argument 2 into the lambda

add10 = lambda x:x+10
add10(2)
# returns 12, simply storing a lambda in a variable
print add10(2)

def incrementor(num):
    start = num
    return lambda x:num+x
print incrementor(5)
# returns the lambda function

my_arr = [1,2,3]

def square(num):
    return num ** 2
map(square, my_arr)

# can also be written as
my_arr = [1,2,3]
map(lambda x:x**2, my_arr)
