from collections import Counter
import math

def second(a):
    min=math.inf
    for i in a:
        dist=sum([a[x]*abs(int(x)-int(i))*(abs(int(x)-int(i))+1)//2 for x in a])
        min=dist if dist<min else min
    return min

def first(a):
    min=math.inf
    for i in a:
        dist=sum([a[x]*abs(int(x)-int(i)) for x in a])
        min=dist if dist<min else min
    return min
        

if __name__=="__main__":
    with open("./Day7/input.txt","r") as f:
        nums=f.readline().split(",")
        a= Counter(nums)     
        print(first(a))
        print(second(a))

