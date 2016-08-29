#Course : ITI 1120


########################
# Question 1
########################

#x,y -> coordinates of bottom left corner of square
#length -> length of side of square
#x1,y1 -> coordinates of some query point

def in_or_out_square(x,y,length,x1,y1):
    x= float(x)
    y = float(y)
    length = float(length)
    x1 =float(x1)
    y1 = float(y1)
    if length <0:
        return("invalid side length")
    if  x1 <= x+length and x1 >= x and y1 <= x+length and y1 >= y:
        return("'The given query point",(x1,y1),"is inside of the square'")
    else:
        return("The given query point("+str(x1)+","+str(y1)+")is outside of the square")
        

########################
# Question 2
########################

def factorial(n):
     if n == 0:
        return 1
     else:
        #factorial is a RECURSIVE function ---> function references itself 
        return (n * factorial(n-1))


########################
# Question 3
########################

def strange_count (s):
    for char in s:
        if chars>='b' and char<='s' and char>='3' and char<='7':
        #s>='b' and s<='s' and s>='3' and s<='7':
            print(char)
            
    
