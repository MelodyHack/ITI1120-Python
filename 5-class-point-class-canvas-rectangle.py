#####################
#Name : Melody Habbouche
#Student number : 8305782
#Course: ITI 1120
#ASSIGNMENT 5 PART 3
#####################
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord


    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def getx(self):
        '''(xcoord) -> New x coord
        Return a new xcoord
        '''
        return (self.x)

    def gety(self):
        '''(ycoord) -> New y coord
        Return a new ycoord
        '''
        return (self.y)
        

    def move(self, dx, dy):
        
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In the case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    ' represents a 2D (axis-parallel) rectangle that a user can draw on a computer screen'

    def __init__(self, Point1,Point2, color):
        '''(Rectangle, Point, Point, color)-> None
        will take two objects of class Point as input and a string for the color

        Precondition: assume that the first point (sent to the constructor, i.e. __init__)
        will always have smaller than or qual x coordinate than the x coordinate of the
        second point and smaller than or equal y coordinate than the y coordinate of
        the second point.
        '''
        self.color = color
        self.Point1 = Point1
        self.Point2 = Point2
       
    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if Point1 and Point2 have the same coordinates BUT not the same color (see discussion board)
        '''
        return self.p1==other.p1 and self.p2==other.p2
    
    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(Point(x,y),Point(x,y), 'color')
        '''
        return 'Rectangle(Point('+str(self.Point1.x)+','+str(self.Point1.y)+'), Point('+str(self.Point2.x)+','+str(self.Point2.y)+"), '"+self.color+"')"

    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Rectangle(Point(x,y),Point(x,y), 'color').
        In the case we chose the same representation as in __repr__'''
        return "I am a "+str(self.color)+" rectangle with bottom left corner at "+str(self.Point1.get())+" and top right corner at "+str(self.Point2.get())+"."


    def get_bottom_left(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point located on the bottom left of the rectangle'''
        return self.Point1
        
    def get_top_right(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point located on the top right of the rectangle'''
        return self.Point2
    
    def get_color(self):
        '''(Point)->string (color)
        Returns a string of the color of the Point'''
        return self.color

    def reset_color(self,color):
        '''(Point,color)-> None
        '''
        self.color=color

    def get_perimeter(self):
        '''(Point)-> Number
        Returns a number calculated by perimeter formula
        '''
        return 2*((self.Point2.y-self.Point1.y)+(self.Point2.x-self.Point1.x))
    
    def get_area(self):
        '''(Point)-> Number
        Returns a number calculated by area formula
        '''
        return (self.Point2.gety()-self.Point1.gety())*(self.Point2.getx()-self.Point1.getx())

    def move(self,x,y):
        '''(Point, Number, Number)-> None
        given numbers dx and dy this method moves the calling rectangle by dx in
        the x direction and by dy in the y-direction. This method should not change directly the
        coordinates of the two corners of the calling rectangle, but must instead call move method
        from the Point class.
        '''
        self.Point1.move(x,y)
        self.Point2.move(x,y)
        
    def intersects(self,other):
        '''

        '''
        return ((self.Point1.getx()<=other.Point1.getx()<=self.Point2.getx()) or (self.Point1.getx()<=other.Point2.getx()<=self.Point2.getx()) or (other.Point1.getx()<=self.Point1.getx()<=other.Point2.getx()) or (other.Point1.getx()<=self.Point2.getx()<=other.Point2.getx()))  and ((self.Point1.gety()<=other.Point1.gety()<=self.Point2.gety()) or (self.Point1.gety()<=other.Point2.gety()<=self.Point2.gety()) or (other.Point1.gety()<=self.Point1.gety()<=other.Point2.gety()) or (other.Point1.gety()<=self.Point2.gety()<=other.Point2.gety()))


    def contains(self,x,y):
        '''

        '''
        return (self.Point2.getx()>=x>=self.Point1.getx()) and (self.Point2.gety()>=y>=self.Point1.gety())
        

class Canvas:
#8 methods : add_one_rectangle, count_same_color, total_perimeter, min_enclosing_rectangle, ancommon_point + built-in
    
    def __init__(self):
        '''(Canvas)->None
        '''
        self.lst= []
        
    def __repr__(self):
        '''(Canvas)->string
        '''
        return "Canvas("+str(self.lst)+")"
        
    def __len__ (self):
        '''(Canvas)->integer
        '''
        return len(self.lst)

    def add_one_rectangle(self, x):
        '''(Canvas, Rectangle)-> None
        '''
        self.lst.append(x)

    def count_same_color(self,color):
        '''(Canvas,color)->number
        '''
        count= 0
        for i in range(len(self.lst)):
            if (self.lst[i].get_color() == color):
                count = count +1
        return count
        

    def total_perimeter(self):
        '''(Canvas)->Number
        '''
        t = 0
        for i in range(len(self.lst)):
            t += self.lst[i].get_perimeter()
        return t
    def min_enclosing_rectangle(self):
        '''
        (Canvas)-> Rectangle(Point, Point, color)

        >>> c.min_enclosing_rectangle()
        Rectangle(Point(-2,-100),Point(4,100),'red')
        '''
        x = []
        y = []
        for i in range(len(self.lst)):
            x.append(self.lst[i].Point1.getx())
            x.append(self.lst[i].Point2.getx())
            y.append(self.lst[i].Point1.gety())
            y.append(self.lst[i].Point2.gety())
        x.sort()
        y.sort()
        return Rectangle(Point(x[0],y[0]),Point(x[-1],y[-1]),'red')



    def common_point(self):
        '''(Canvas)-> Boolean
           returns true if a common point is found, or false if not found
        '''
        for i in range(len(self.lst)):
            for j in range(len(self.lst)):
                if(not(self.lst[i].intersects(self.lst[j]))):
                    return False
        return True
        

        
