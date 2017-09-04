import sys

print('Number of Argumnets', len(sys.argv));
print(sys.argv[0])
print(str(sys.argv))

#name = input("enter your name");
#print(type(name))

print(range(4))

for i in range(0 ,5 ,3):
    print(i)

list = ['Python','Hadoop','data science','Android']
l= list[1:5]
print(l)

St = 'Nishtha a bhardwaj '

ts = ('python', 'hadoop')
t =tuple( enumerate(ts))
print(t)
print(type(ts))
print(max(ts))

D = {}
D['key']='valeu'
print(D)

s = set("Nishtha")
s.add("nishth")
print(s)






#help(range)