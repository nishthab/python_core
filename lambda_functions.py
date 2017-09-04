import operator
# Lambda functions

sqr = lambda num: num**2
print(sqr(25))

chk_location = lambda loc: loc.startswith("B")

print(chk_location('Banglore'))
calc = lambda a,c,d: (a*d)+ (c*d) + a
print(calc(2,3,4))

increment = lambda num, inc=5: num+inc
print(increment(4,10))

print("--------------------------------------------------")

# itemgetter
print(operator.itemgetter(4)(range(1,11)))

# create the list of tuples

courses = [('Hadoop',2),('nosql',1),('ETL',1), ('Hadoop', 4)]
print("Sorting based on index 1-->", sorted(courses, key=operator.itemgetter(1)))
print("Sorting based on index 0-->", sorted(courses, key=operator.itemgetter(0)))
print("Sorting based on index (0, 1)-->", sorted(courses, key=operator.itemgetter(0,1)))
print("Sorting based on index (1,0)-->", sorted(courses, key=operator.itemgetter(1,0)))

print("--------------------------------------------------")