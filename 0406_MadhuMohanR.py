# 1. Implement palindrome using iterator(for loop) and generator mechanism.
# num = int(input('Enter number : '))
# b = str(num)
# c = 0
# for i in range(len(b)-1,-1,-1):
#     c = c * 10 + int(b[i])
# if num == c:
#     print('It is palindrome number')
# else:
#     print('It is not palindrome number')
# -----------------------------------------------------------------------------------------------------------------------
# 2. Sum of 2 digits into output
# 		n1 = 1234 # int(input("Enter number1 :" ))
# 		n2 = 9999 # int(input("Enter number2 :" ))
# 		Output: 9+1 2+9 3+9 4+9
# 		         10 + 11 + 12 + 13
# 				 46

# n1 = int(input('Enter number1 : '))
# n2 = int(input('Enter number2 : '))
# a = str(n1)
# b = str(n2)
# c = len(a)
# sum = 0
# for i in range(c):
#     add = int(a[i]) + int(b[i])
#     sum = sum + add
# print('sum of two numbers :',sum)
# -----------------------------------------------------------------------------------------------------------------------
# 4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# find-out elements duplicate count output in  dict format

# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# count = 1
# dict = {}
# for i in some_list:
#     if i in dict:
#         dict[i] = count + 1
#     else:
#         dict[i] = count
# print('After Count in Dictionary format :', dict)
# ----------------------------------------------------------------------------------------------------------------------
# 6 .Write a Python program to remove leading zeros from an IP address.
# inp = "216.08.094.196"
# o/p =  216.8.94.196

# inp = "216.08.094.196"
# a = ''
# for i in inp:
#     if i == '0':
#         continue
#     else:
#         a += i
# print('After remove leading zeros from an IP address : ', a)
# -----------------------------------------------------------------------------------------------------------------------
# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output= [1,2,3,4,5,6,7,8,9,10]
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# list1 = []
#
#
# def list2(l):
#     for i in l:
#         if type(i) is list:
#             list2(i)
#         else:
#             list1.append(i)
#
#
# list2(l)
# print(list1)
# -----------------------------------------------------------------------------------------------------------------------


