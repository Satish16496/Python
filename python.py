'''a="welcome to python"
print(a)

a=b=c=50
print(a)
print(b)
print(c)

a,b,c=3,4,5
print(a)
print(b)
print(c)

t1=(1,"satish",65)
t2=("abc",45,6,5,4)
print(t1[2:])
print(t2[1:])
print(t1[0:3])
print(t1+t2)

dictionary={'name':'satish','id':12,'age':20}
print(dictionary.keys())
print(dictionary.values())

s1="satish"
s2='satish'
s3="satish\
sharma"
s4="""my name is 
satish sharma"""
print(s1)
print(s2)
print(s3)
print(s4)

var1=10
var2=None
print(var1)
print(var2)


list1=[1,"satish","sa","fd",34,5,6]
list2=[2,"sharma","css"]
print(list1+list2)
print(list1[0:7])
print(list2*3)
list1[1]="deepak"
print(list1)

c=45
c


print(10+20)
print(50-30)
print(2*5)
print(9//2)
print(2**3)
print(6%3)

print(10<20)
print(3>2)
print(34<=56)
print(32>=32)
print(45!=56)
print(48==48)
print(21<>20)



a=23 and 23
print (a)
b=34
b>34 or 23
print(b)

a=not(5>4)
print(a)

a=45
b=23
list=[1,45,6,7,89,]

if(a in list):
	print("a is part of list")
else: 
	print("not")
if(b not in list):
	print("b is not part of list")

a=10
if(a==10):
	print("program execute")
else:
	print("eror")
y=2000
if(y%4==0):
	print("leap year")
else:
	print("not")
a=20

if(a>=30):
	print("condition is  true")
else:
	if(a<=15):
		print("second condition is true")

	else:
		print("all condition are false")


a=10  
if a>=20:  
        print "Condition is True"  
else:  
        if a>=15:  
            print "Checking second value"  
        else:  
            print "All Conditions are false"   
'''

'''
for i in range(1,10):
	print("*")

	print '''
'''sum=0
for i in range(1,11):
	sum+=i
print(sum)
'''
'''for i in range(1,6):
	for j in range(1,i+1):
        	print(i),
	print'''

'''a=10
while a>0:
	print(a)

	a-=1'''

'''sum=0
num=153
while num>0:
	r=num%10
	sum=sum+r
	num/=10
print(sum)
'''

'''for i in [1,2,3,4,5]:
	if i==4:
		print ("element found")
	break
	print i,
'''	
'''class myclass:
	"this is python"
	a=50

	def fun(self):
		print("object oriented programing")	
print(myclass.a)
print(myclass.__doc__)

ob=myclass()
ob.fun()
'''
'''def add(a,b):
	c=a+b
	print(c)'''
obj=open("abcd.txt","w")  
obj.write("Welcome to the world of Python")  
obj.close()  
'''obj1=open("abcd.txt","r")  
s=obj1.read()  
    print s  
    obj1.close()  
    obj2=open("abcd.txt","r")  
    s1=obj2.read(20)  
    print s1  
    obj2.close()  
'''





















