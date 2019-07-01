start,end=[int(x) for x in input().split()]
for val in range(start,end+1):
   if val>1:
      for i in range(2,val):
         if(val%i)==0:
            break
         else:
            print(val,end=" ")
