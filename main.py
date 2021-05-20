'''
Creating Lists
'''
#List items are enclosed in square brackets
#Lists are ordered
#Lists are mutable 
#list elements do not need to be unique
#Elements can be of different data types

# #Empty lists
# list = []
# #list of intergers
# list = [1,2,3]
# #list of strings
# list = ['orange','apple','pear','apple','banana']
# #list with mixed data types
# list = [1,"Hello",5.0]

'''
List indexing
'''
# fruits = ['orange','apple','pear','apple','banana']
# fruits[0] #output => orange
# fruits[1] #output => apple
# fruits[2] #output => pear
# fruits[3] #output => apple
# fruits[4] #output => banana
# fruits[-1] #output => banana
# fruits[-5] #output => orange

#Nested indexing
# fruits = ['orange',['apple','orange']]
# fruits[1][0] # apple 
# fruits [1][1] #orange

'''
How to Slice Lists in Python
'''
# fruits = ['orange','apple','pear','grapes','banana']
# #beginning to end 
# fruits[:] #output => ['orange','apple','pear','grapes']
# #index 2 to 5th item
# fruits[2:5] #output => [pear','grapes','banana']
# #remove last 2 items
# fruits [:-2] #output => ['orange','apple']
# #index 2 to the end
# fruits[2: ] #output => [pear','grapes','banana']
# #every nth item
# fruits[::2] #output => ['orange','pear',banana']
# #reverse list
# fruits[::-1] #output => ['banana','grapes','pear','apple','orange']

'''
Add Elements to a List
'''
# #Changing a list after it is created (mutable)
# fruits =['orange','apple','pear','grapes','banana']
# #change first item
# fruits[0] = 'Berries'
# print(fruits) #output => ['Berries','apple','pear','grapes','banana']
# # change item in index 1 to 4th item
# fruits [1:4] = ['Mandarins','Peaches','Plums']
# print(fruits) #output => ['apple','pear','grapes']
# #using append
# fruits = ['orange','apple','pear','grapes','banana']
# # add limes to end of the list
# fruits.append('limes')
# print(fruits) #output => ['orange','apple','pear','grapes','banana','limes']

'''
Remove or Delete List items
'''
# fruits = ['orange','apple','pear','grapes','banana']
# delete nth index position
# del fruits[0]
# delete the items from index position 1 to 5th item
# del fruits[1:5]
# delete the entire list
# del fruits 
# adds strawberries to the end of the list 
# fruits = fruits + ['Strawberries']

''''
Python List Methods
'''
# help(dir)
# print(dir(list)) # -list all attributes/Methods
# print(help(list.count))

# #copy() - Returns a copy of the list 
# #append() - Adds one elememt at the end of the list
# #count() - Returns the number of elements with the specified value
# #extend() - Add the elements of a list (or any iterable),to the end of the current list
# #index() - returns the index of the first element with the specified value
# ##insert() - Adds an element at the specified position
# #pop() - Removes the element at the specified position
# #remove() - Removes the first item with the specified value
# #reverse() - Reverses the order of the list
# #clear() - Removes all the elements from the list
# #sort() - Sorts the list 

# fruits = ['orange','apple','pear','grapes','banana']
# fruits.append('cashew')
# print(fruits)

# fruits.insert(0,'guava') #guava goes before orange
# print(fruits)

# fruits = ['orange','apple','pear','grapes','banana']
# fruits.pop(-1)
# print(fruits.index('orange'))

# pos = fruits.index('apple')
# fruits.insert(pos,'guava')
# print(fruits)

# ====================

# fruits = ['orange','apple','pear','grapes','banana']
# fruits.clear()
# print(fruits)

# ======================
# fruits = ['orange','apple','pear','grapes','banana']
# fruits.pop(1)
# print(fruits)

# =====================

# fruits = ['orange','apple','pear','grapes','banana']
# fruits.pop(1)
# pos = fruits.index('pear')
# fruits.pop(pos)
# print(fruits)

# =======================

# fruits = ['orange','apple','pear','grapes','banana']
# print = (fruits.count('pear'))


# result = []
# for x in fruits:
#   result[x] = fruits.count(x)

#   print(result)

#   from collections import Counter

#   print(Counter(fruits))

# ========================
#head over to documentation

# fruits = ['orange','apple','pear','grapes']

# print(fruits .sort())
# print(fruits)

# print(fruits[0])

#use copy 

# ========================


'''
list Membership Test
'''
# fruits = ["orange","apple","pear"]

# #check item is in the list
# print("orange")in fruits #output => True

# #check item,not in the list
# print("orange") not in fruits #output => False