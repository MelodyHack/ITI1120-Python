def read_initial_info():
    ''' None->(float, 2D-list)
    Reads the file a4-input.txt and returns a tuple. The first element of that tuple is the limit,
    the second is a 2D list called banks of a format as follows (for this particular file a4-input.txt_:
    [[25.0, 1, 100.5, 4, 320.5], [125.0, 2, 40.0, 3, 85.0], [175.0, 0, 125.0, 3, 75.0], [75.0, 0, 125.0], [181.0, 2, 125.0]]


    Before returning the tuple the function should also print the 2D list banks by calling print(banks) 
    '''
    # YOUR CODE GOES HERE
    line = open('a4-input.txt','r').readlines()
    data=[]
    for i in line:
        data.append(i.split())
    for j in range(len(data)):
        for k in range(0,len(data[j]),2):
            data[j][k]=float(data[j][k])
        for k in range(1,len(data[j]),2):
            data[j][k]=int(data[j][k])       
    limit=data[0][0]
    banks=data[1:]
    print(banks)
    
    return (limit,banks)

def current_Assets(banks):
    ''' (2D-list)->list
    given the 2D list banks, returns a (1D) list with the current_assets of all banks
    Precondition: the format of the 2D list banks is as explained in the assignment
    and as produced in read_initial_info()
    '''

    # YOUR CODE GOES HERE TOO
    current_assets=[]
    for i in range(0,len(banks)):
        count = 0
        for j in range(0,len(banks[i]),2):
            count += (banks[i][j]) 
        if count !=0:
            current_assets.append(i)
            current_assets.append(count)
    #print (current_assets)
    return (current_assets)

def spaces():
    '''
    This is simply used when need of spaces
    '''
    print("\n")
    

def bankruptcy_unsafe_banks(bankname,banks):
    for j in range(len(banks[bankname])):
        banks[bankname][j]=0



    for j in range(len(banks)):
        current = len(banks[j])-1
        m=0
        while current >= m:
            if bankname==banks[j][m]:
                #dont forget to remove the last pair
                banks[j].pop(m)
                banks[j].pop(m)
                current = current -2
            m = m+1
   

        
def find_unsafe():
    '''None->None

    Your solution goes here. This function should start off by calling read_initial_info()
    and then work with the data read_initial_info() returns, i.e. with limit and 2D list banks
    It should call other helper functions
    '''
    pair=read_initial_info()
    limit=pair[0]
    spaces()
    print("Safe limit is:", limit,"million dollars\n\n")
    banks=pair[1]

    # YOUR CODE GOES HERE TOO
    spaces()
    print("Curent unsafe banks are: ")
    print("Current assests of the banks which are not yet in unsafe list:")
    values = current_Assets(banks)
    #ignore comments- they are only for when I test a part of my program
    #print(values)
    for i in range(0,len(values),2):
        print("Bank ",values[i],": Current assets: ",values[i+1]," millions")

    a=0
    unsafe=[]

    while True:
        spaces()
        for i in range(1,len(values),2):
            if limit > values[i]:
                print("Adding bank",values[i-1],"to the list of unsafe banks.")
                unsafe.append(values[i-1])
                print("Current unsafe banks are: ")

                for j in range(len(unsafe)):
                    print(unsafe[j])
                bankruptcy_unsafe_banks(values[i-1],banks)
                values = current_Assets(banks)
        
                print("Current assests of the banks which are not yet in unsafe list:")
                for m in range(1,len(values),2):
                    print("Bank",values[m-1],"Current assets:",values[m] ,"millions")
                b = False
                break
                
            if (i == len(values)/2):
                b = True
        if b:
            break

    

    print("\nUnsafe banks are:")
    unsafe.sort()







    for i in unsafe:
        print(i)
    print("Safe banks are: ")
    for i in range(0,len(values),2):
        print (values[i],end=" ")
                          
    
# main
# main can only have this function call and nothing else. Do not modify after this line
find_unsafe()
    
