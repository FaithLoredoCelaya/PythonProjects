import math
def is_prime(n):
    check = int(math.sqrt(n))
    if n==1 or n ==2:
        return True
    if n%2==0:
        return False
    if n%2==1:
        
        #this is a better check since it reduces the ammount of numbers to check
       for i in range(3,check):
           for m in range(3,check-1):
               if i*m==n:
                   return False
         
    #check from a website option. if each digit in the number is divisible by 3 it should not be a prime. not sure about the accuracy of this
       test = str(n)
       add=0
       for i in test:
           add+=int(i)
       if add%3==0:
           return False
       return True
    
    return False 

if __name__ =="__main__":
    print(is_prime(9999))
