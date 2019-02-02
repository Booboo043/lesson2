from collections import deque
from pip._vendor.distlib.compat import raw_input
str = raw_input("please enter nums:")#Lst1 is used to store the input string, separated by spaces.
queue = str.split(" ")
l=input("please add nums:")
num=int(l)
i = input("please chose the function: deque or enque a or b")
num1 = input(i)
a = 0
b = 0
queue
if i == a:
    queue = deque(queue)
    print(queue)
elif i == b:
    queue.append("l")           # 4 arrives
    print(queue)
