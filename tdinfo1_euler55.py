def décomposition(x):
   L=[]
   s=x
   while s>=10:
      y=s%10
      L=[y]+L
      s=(s-y)/10
   L=[s]+L
   return(L)

#print(décomposition(130908675314289))

def palindrome(x):
   D=décomposition(x)
   i=int(len(D)/2)
   for n in range (i):
      if D[n]!=D[-(n+1)]:
         return False
   return True
#print(palindrome(1002))

def reverse_and_add(x):
   D=décomposition(x)
   d=len(D)
   inv=0
   for i in range (d):
      inv+=D[i]*10**i
   return(inv+x)

#print(reverse_and_add(1292))

def comptage_Lychrel_sous(x):
   s=0
   for i in range (1,x+1):
      j=0
      test=i
      while not palindrome(test) or j>50:
         test=reverse_and_add(test)
         j+=1
      if j==50:
         s+=1
   return(s)
print(comptage_Lychrel_sous(10000))      #le programme est trop long et meme en une heure il ne rétourne rien
        
        