from pip._vendor.distlib.compat import raw_input
lst = []#Define an empty list
l=input("please enter total nums:")
num=int(l)
str = raw_input("please enter nums:")#Lst1 is used to store the input string, separated by spaces.
lst1 = str.split(" ")
i = 0
while i <= len(lst1)+1:
	lst.append(int(lst1.pop()))#Convert lst1 data to integer and assign it to lst
	i += 1
#print(lst)
def sum(list):#Summing the values ​​of the list
	s = 0
	for x in list:
		s += x
	return s
def average(list):#Averaging List Data
	avg = 0
	avg = sum(list)/int(l)##call sum function summation
	return avg
print("avg = %.3f"%average(lst))
