# -*- coding: utf-8 -*-
#Faro Shuffle
def Faro_shuffle(in_list,order):
    result=[]
    half =len(in_list)//2
    first_half=in_list[:half]
    last_half= in_list[half:]
    
    
    for i in range(half):
        if order==False:
            result.append(last_half[i])
            result.append(first_half[i])
        else:
            result.append(first_half[i])
            result.append(last_half[i])

                
    return result

if __name__ == "__main__":
    print(Faro_shuffle([1,2,3,4,5,6,7,8], True))
