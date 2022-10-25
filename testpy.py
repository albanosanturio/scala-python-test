import numpy as np

print("\n TEST TUPLE")
tuple1 = (1,2,3)
print("tuple1=",tuple1)

print("\n TEST NPARRAY")
nparray1 = ["one",2,3]
print("nparray1=",nparray1)

print("\n TEST LIST")
list1 = [1,2,3]
print("list1=",list1)

print("\n TEST DICT")
dict1 = {
  "key1": "value1",
  "key2": "value2",
  "key3": 3
}
print("dict1=",dict1)

print("\n Differences tuple/array/list/dict")

print("\n TEST WHILE")
i=0
while (i<=10):
    print(i)
    i+=1

print("\n TEST FOR")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

nums = [20,30,40]
for x in nums:
  print(x)

print("\n TEST DEF FUNC")
def funcion1():
  print("printeo funcion 1")
funcion1()

print("\n TEST LAMBDA")
x = lambda a : a + 10
print(x(5))

print("\n TEST LAMBDA+MAP")
print("its used: map(function, list)")
print("test square root")
nums1 = [1, 2, 4, 7]
numssq = list(map(lambda x : x ** 2, nums1))
print("nomap: ",nums1)
print("map: ",numssq)






