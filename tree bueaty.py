from collections import Counter

numbers  = [12,27,18,50,75]

def suqare_free(x):
   result = 1
   d = 2

   while d *d<=x:
       count = 0

       print(d*d,x)

       while x%d == 0:
           x = x//d
           print("X after division: "+str(x))
           count+=1
           print("count: "+str(count))

       if count%2==1:
           result = result*d
           print("result:"+str(result))

       d = d +1
       print(d)

   if x>1:
       result = result*x
   print("result: " + str(result))
   return result

freq = Counter()

for num in numbers:
   sf = suqare_free(num)
   print("square free + "+str(sf))
   freq[sf] = freq[sf]+1
   print(freq[sf])

print(freq)

piars = 0
for i in freq.values():
   piars = piars + i * (i-1)//2
   print(piars)

print(piars)
