def binarySearch(list, item):
    #list should be ordered 
    #item that is searched
    low=0 #first position
    high=len(list)-1 #high position
    while low <=high:  #list> one element
        mid= (low+high)//2 #find middle
        print (low,high,mid)
        guess= list[mid] # find the position 
        if guess==item: # found item
            #print (mid)
            return mid # return position where was found
        if guess>item: #  half inferior 
            high= mid-1 # high is mid -1 because mid was evaluated previously
        if guess < item:  #half superior
            low=mid+1  # low is mid +1 because mid was evaluated previously
    
    return None
      
lista= list(range(1,129,1))      
print (len(lista))  
print (lista)
print (binarySearch(lista,-1))


        


