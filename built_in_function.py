import operator
# Built in functions
# sorted can be used of any type of Iterable ie. list, tuple, string
num_tup = tuple(range(1,6)) + tuple(range(11,5, -1))

print(num_tup)
print("--------------------------------------")
sorted_tup = sorted(num_tup, reverse=True) # decending order sorted on ACII

print("original num_tup-->",num_tup)
print("sorted_tup -->",sorted_tup) # this will return a list
print("sorted_tup -->",tuple(sorted_tup)) #convert it to tuple
print("--------------------------------------")

# Method 'sort' can be used only for the list

print("--------------------------------------")
num_list = list(range(1,5)) + list(range(11,5, -1))
print("Before sort num_list->",num_list)
num_list.sort(reverse=True)
print("After sort num_list->",num_list)

print("-----------------------------------------")
# itemgetter
print(operator.itemgetter(4)(range(1,11)))

# create the list of tuples

courses = [('Hadoop',2),('nosql',1),('ETL',1), ('Hadoop', 4)]
print("Sorting based on index 1-->", sorted(courses, key=operator.itemgetter(1)))
print("Sorting based on index 0-->", sorted(courses, key=operator.itemgetter(0)))
print("Sorting based on index (0, 1)-->", sorted(courses, key=operator.itemgetter(0,1)))
print("Sorting based on index (1,0)-->", sorted(courses, key=operator.itemgetter(1,0)))

print("--------------------------------------------------")

# dir
print("Dir->", dir()) # It will list out all the functions ,vairalbes that you have difined in the current module
print("Dir->", dir(operator))


print("-----------------------------------------")



print("--------------------------------------")