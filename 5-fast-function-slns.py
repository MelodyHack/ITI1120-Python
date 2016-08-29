#####################
#Name : Melody Habbouche
#Student number : 8305782
#Course: ITI 1120
#ASSIGNMENT 5 PART 2
#####################

'''
THE FUNCTIONS THAT I LEFT UNCOMMENTED ARE THE ONES I CHOSE AS THE FASTEST RUNNING SOLUTION
'''
#####
#2A)#
#####


##def largest_two(a): #PYTHON BUILT-IN SORT
##    if len(a)==0:
##        print("The list is empty, try again")
##    elif len(a)==1:
##        print("The list only contains one element, try again")
##    else:
##        tmp=sorted(a)
##        return (tmp[-1]+tmp[-2])

def largest_two_V2(a): #LINEAR SEARCH
    '''
    returns the sum of the two largest
    values in the list a
    '''
    
    large = a[0]
    seco_large = a[1]
    for i in range(len(a)):
        if (a[i]>=large):
            large=a[i]
        elif(a[i]>=seco_large):
            large=a[i]
    
##def largest_two_V3(a): #RECURSIVE
##    if len(a)==0:
##        print("The list is empty, try again")
##    elif len(a)==1:
##        print("The list only contains one element, try again")
##    else:
##        large = max(a)
##        a.remove(large)
##        seco_large = max(a)
##        a.insert(large, seco_large)
##        return(large + seco_large)


#####
#2B)#
#####

def smallest_half(a):
    '''
    sum of the len(a)//2
    smallest values in the list a
    '''
    
    x=0
    a.sort()
    for i in range(len(a)//2):
        x+=a[i]
    return x

#####
#2C)#
#####

def median(a):
    '''
    returns a value, x, such that at least
    half the elements in a are less than or equal to x and at least half the elements in a are
    greater than or equal to x
    '''
    a.sort()
    v=len(a)//2
    return a[v]

#####
#2D)#
#####
def at_least_third(a):
    '''
    returns a value in a that occurs
    at least len(a)//3 + 1 times. If no such element exists in a, then this function returns
    None
    '''

    a.sort()
    for i in range(len(a)-len(a)//3):
        if (a[i]==a[i+len(a)//3]):
            return a[i]
    return None 


#####
#2E)#
#####

def triple_sum(a,x):
    '''
    returns a value in a that occurs
    at least len(a)//3 + 1 times. If no such element exists in a, then this function returns
    None
    '''
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if (a[i]+a[j]+a[k]==x):
                    return True
    return False

def triple_sum_V2(a,x):
    '''similar to what we did in class when we take the begining and end of a list
    examples:
    >>> triple_sum_V2([1, 5, 8, 2, 6, 55, 90],103)
    True
    >>> triple_sum_V2([-1, 1, 5, 8, 2, 6],-3)
    True
    >>> triple_sum_V2([-10,2],-18)
    True
    >>> triple_sum_V2([1, 1, 5, 8, 2, 6],1000)
    False
    '''
    a.sort()
    n=len(a)
    for j in range(n):
        beg=j
        end=n-1

        while end >= beg:
            if (a[j]+a[beg]+a[end])==x:
                return True
            elif (a[j]+a[beg]+a[end])> x:
                end = end - 1
            else:
                beg = beg + 1
    return False

                
    



