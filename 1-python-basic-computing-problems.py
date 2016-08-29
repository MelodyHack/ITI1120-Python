# Course: ITI 1120



#Question 1 : Fahrenheit to Kelvin
def f2k(t):
    k=round((t+459.67),11)*5/9
    return (k)




#Question 2 : APA Format Citation
def bibformat_apa(author,title,city,publisher,year):
    return (author + "("+ str(year)+ ")." +' '+ title + ". " + city + ": " + publisher + ".")


#Question 3 : Joker
def joker():
    x = input("What is you name: ")
    print ( " Teacher asks 'What is the chemical formula for water'\n" ,x , " says 'HIJKLMO'!\n Teacher says 'What are you talking about?'\n" ,x, "says 'Yesterday you told us its H to O'")


#Question 4 : Input APA Format Citation
def bibformat_apa_display():
    Xtitle = input("Enter the title of a book: ")
    Xauthor = input("Enter the name of the author? ")
    Xyear = input("What year was the book published? ")
    Xpublisher = input("Enter the name of the publisher: ")
    Xcity = input("In what city are the headquarters of the publisher? ")
    print(bibformat_apa(Xauthor,Xtitle,Xcity,Xpublisher,Xyear))


#Question 5 : body-mass-index
def bmi(w,h):
    bmi = (w/ (h**2)) *703
    return bmi


#Question 6 : pair of numbers
def f2fi(f):
    fh = round(f)
    i = 12*(f-fh)
    print("(",fh,",",i,")")


#Question 7 : BMI calculator
def bmi_calculator():
    Xappelation = input("Enter your appelation (Mrs, Mr, Dr., Miss):")
    XFName = input("Enter your first name:")
    XLName = input("Enter your last name:")
    XHeight = int(input("Enter your height in inches:")) 
    XWeight = int(input("Enter your weight in pounds:"))
    Feet = int((XHeight/12))
    Inches =int((XHeight - (Feet*12)))
    print("BMI Record for", Xappelation, XFName, XLName)
    print("Subject is", Feet, "feet", Inches, "inches tall")
    print("and weighs", XWeight, "pounds")
    print("Subject's BMI is", bmi(XWeight,XHeight))
    

#Question 8 : My Fun Drawing
def my_fun_drawing():
    import turtle
    t= turtle.Turtle()
    s=turtle.Screen()
    s.bgcolor('gray')  #background
    s.setup(900,500)

    t.color('magenta')
    t.pencolor('black')
    t.pensize(30)
    t.begin_fill()
    t.penup()
    t.sety(150)
    t.pendown()
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.end_fill()

    t.forward(300)
    t.right(90)
    t.forward(90)
    t.pensize(15)
    t.right(90)
    t.forward(600)

    t.forward(-380)
    t.circle(50)
    t.penup()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()
    t.circle(80)
    t.penup()

    t.pensize(3)
    
    t.right(90)
    t.forward(70)
    t.color('black')
    t.begin_fill()
    t.pendown()
    t.right(45)
    t.forward(30)
    t.right(45)
    t.forward(70)
    t.right(45)
    t.forward(30)
    t.right(135)
    t.forward(110)
    t.end_fill()
    
    t.penup()
    t.left(90)
    t.forward(115)
    t.right(55)
    t.pendown()
    t.speed(0)
    
    for sideNum in range(200):
        if sideNum % 2 == 0:
            t.color("white")
        else:
            t.color("black")
        t.forward(40)
        t.left(70)





    
#Question 9 : Triangle
def forms_triangle(a, b, c):
    if (a+b > c)and (a+c > b) and (c+b >a):
        return True
    else:
        return False


#Question 10 : Change to Coins
def change_to_coins(amount):
    cent=int(round(amount*100))
    quarters = int((cent-(cent%25))/25)
    cent2=cent-(25*quarters)
    dime = int(((cent2-(cent-quarters*25)%10))/10)
    cent3=cent2-(dime*10)
    nickel = int(((cent3-(cent-dime*10)%5))/5)
    pennies = int((cent-(quarters*25)-(dime*10)-(nickel*5)))
    return (quarters+dime+nickel+pennies)
    




