from nano_topology import *
from itertools import permutations
def equality(d1,d2):
     node1=[]
     node2=[]
     true=[]
     for i in d1:
        node1.append(i)
     for i in d2:
        node2.append(i)
     vh1=vh(node1)
     vh2=vh(node2)
     la1=lower_approximation(vh1,d1)
     la2=lower_approximation(vh2,d2)
     ua1=upper_approximation(vh1,d1)
     ua2=lower_approximation(vh2,d2)
     br1=boundary_region(la1,ua1)
     br2=boundary_region(la2,ua2)
     result1=nanoset(la1,ua1,br1)
     result2=nanoset(la2,ua2,br2)
     Nano1=singleton(vh1,result1)
     Nano2=singleton(vh2,result2)
     perm=permutations(node2)
     l=[]
     l1=[]
     l2=[]
     x=list(perm)
     counter=0
     for r in range(len(x)):
       for i in Nano1:
           for j in i:
           	y=list(x[r]) 
           	ind=node1.index(j)
           	l.append(y[ind])
           l1.append(l)
           l=[]        
       for i in l1:
         for j in Nano2:
            if(set(i)==set(j)):
                counter+=1
       print(counter,node1,set(i),set(j))
       if(counter==len(node1)):
             true.append(y)
       l1=[]
       counter=0      
     if(true==[]):
        print("two graphs are not similar")
     else:
        print("two graphs are similar")
        print("matching nodes")
        print(true)   

