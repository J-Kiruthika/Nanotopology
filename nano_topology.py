def vh(s):
  if s==[]:
      return[s]
  sets=[s]
  for i in range(0,len(s)):
          tmp=vh(s[:i]+s[(i+1):])
          for sub in tmp:
            if sub not in sets:
               sets.append(sub)
  return sets
def lower_approximation(vh,d):
  temp=set()
  ru=[]
  for m in vh:
     for n in m:
       temp=temp.union(set(d[n]))
     ru.append(list(temp))
     temp=set()
  return ru
def upper_approximation(vh,d):
  rl=[]
  temp=[]
  for i in vh:
     for j in i:  
       if(set(d[j]).issubset(set(i))): 
            temp.append(j)   
     rl.append(temp) 
     temp=[]
  return rl
def boundary_region(a,b):
  sym=[]
  for i,j in zip(a,b):
     x=set(i).symmetric_difference(j)
     sym.append(list(x))
  return sym
def nanoset(a,b,c):
     final=[]
     for j in range(len(a)):
         if(a[j]==b[j]==c[j]):
               result=a[j]                    
         elif(a[j]==b[j]):
               result=a[j]+c[j]
         elif(a[j]==c[j]):
               result=a[j]+b[j]
         elif(b[j]==c[j]):
               result=a[j]+b[j]
         else:
               result=a[j]+b[j]+c[j]
         final.append(result)    
     return final
def singleton(x,y):
    result=[]
    for a,b in zip(x,y):
      if(len(a)==1):
         result.append(b)
    return result
