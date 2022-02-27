# Ip Project to find the surface area volume of a given figure
print ()
print ()
print ("   ███████╗ ██████╗ ██████╗ ███╗   ███╗██╗   ██╗██╗      █████╗         ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗") 
print ("   ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██║   ██║██║     ██╔══██╗        ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗")
print ("   █████╗  ██║   ██║██████╔╝██╔████╔██║██║   ██║██║     ███████║        █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝")
print ("   ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║██║     ██╔══██║        ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")
print ("   ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║        ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║")
print ("   ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝        ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
print ()
print ("                                                                                                  By: Techwithzenith ")
print ()
print ()
print ( "     1. Rectangle            6. Rhombus        11. Sphere ")  
print ( "     2. Sqaure               7. Trapezium      0. Exit    ")
print ( "     3. Traingle             8. Cuboid                    ")
print ( "     4. Circle               9. Cube                      ")
print ( "     5. Parallelogram       10. Cylinder                  ")
print ()
print ("                Enter 0 to exit       ")
print ()

# (1) Retangle
ch = (float (input ( "    Enter your choice: ")))
if ch == 1:
    print ()
    print ( " 1. Area of rectangle ")
    print ( " 2. Perimeter of rectangle ")
    print ()
    choice = int ( input (" Select any one:"))
    
        # For Area of rectangle
    if choice == 1:
        print ()
        print (" AREA OF RECTANGLE ")
        print ()
        lenght = float (input(" Lenght:"))
        breath = float (input(" Breath:"))
        area = (lenght * breath) * 100
        print ()
        print (" Area of Rectangle is:",area,"Cm") 
        
        # For perimeter of rectangle
    elif choice == 2:
        print ()
        print (" PERIMETER OF RECTANGLE ")
        print ()
        lenght = float (input(" Lenght:"))
        breath = float (input(" Breath:"))
        perimeter = 2 * (lenght + breath) * 100
        print ()
        print (" Perimeter of recrangle:",perimeter, 'Cm' )
    
# (2) Sqaure
elif ch == 2:
    print ()
    print ( " 1. Area of square")
    print ( " 2. Perimeter of square")
    print ()
    choice = int ( input (" Select any one:"))
    if choice == 1:
        print ()
        print (" AREA OF SQUARE ")
        Side = float (input (" Side of sqaure: ")) 
        area = ( Side * Side ) * 100
        print ()
        print (" Area of sqaure =",area,"Cm")
    elif choice == 2:
        print ()
        print (" PERIMETER OF SQUARE ")
        Side = float (input (" Side of sqaure: ")) 
        perimeter = ( 4 * Side ) * 100
        print ()
        print (" Perimeter of square =",perimeter,"Cm")  
    
# (3) Triangle   
elif ch == 3:
    print ()
    print ( " 1. Area of Traingle")
    print ( " 2. Perimeter of Triangle")
    print ()
    choice = int ( input (" Enter any one:"))
    if choice == 1:
        print ()
        print (" AREA OF TRAINGLE ")
        base = float ( input ( "  Base: "))
        height = float ( input (" Height:"))
        area = ( 1/2 * ( base * height ) ) * 100
        print ()
        print (" Area of Triangle is",area,"Cm")
    elif choice == 2:
        print (" PERIMETER OF TRAINGLE ")
        print ()
        side1 = float (input ( " Side1: "))
        side2 = float (input ( " Side2: "))
        side3 = float (input ( " Side3: "))
        perimeter = ( side1 + side2 + side3 ) * 100
        print ()
        print (" Perimeter of Triangle is",perimeter,"Cm")
    
# (4) Circle    
elif ch == 4:
    print ()
    print ( " 1. Area of Circle")
    print ( " 2. Circumfrence of circle")
    print ()
    choice = int ( input (" Enter any one: "))
    if choice == 1:
        print (" AREA OF CIRCLE ")
        print ()
        dia = float ( input (" Diameter of circle: "))
        r = dia / 2
        area = ( 3.14 * r * r ) * 100
        print ()
        print (" Area of circle is",area,"Cm")
    elif choice == 2:
        print ()
        print (" CIRCUMFRENCE OF CIRCLE ")
        dia = float ( input (" Diameter of circle: "))
        radius = dia / 2
        cir = ( 2 * 3.14 * radius ) * 100
        print ()
        print ( " Circumfrece of Circle is",cir,"Cm")
    
# (5) Parallelogram   
elif ch == 5:
    print ()
    print ( " 1. Area of Parallelogram")
    print ( " 2. Perimeter of Parallelogram")
    print ()
    choice = int ( input (" Enter your choice: "))
    if choice == 1:
        print ()
        print (" AREA OF PARALLELOGRAM ")
        base = float (input ( " Base: "))
        height = float (input ( " Height: "))
        area = ( base * height ) * 100
        print ()
        print ( " Area of parallelogram is",area,"Cm")
    elif choice == 2:
        print ()
        print (" PERIMETER OF PARALLELOGRAM ")
        side1 = float ( input ( " Side1: "))
        side2 = float ( input ( " Side2: "))
        perimeter = ( 2 * ( side1 + side2 )) * 100
        print()
        print (" Perimeter of Parallelogram is",perimeter,"Cm")
        
        
# (6) Rhombus
elif ch == 6:
    print ()
    print ( " 1. Area of Rhombus")
    print ( " 2. Perimeter of Rhombus")
    print ()
    choice = int ( input (" Enter any one:"))
    if choice == 1:
        print ()
        print (" AREA OF RHOMBUS ")
        diagonalone = float (input (" Diagonal 1: "))
        diagonaltwo = float (input (" Diagonal 2: "))
        area = (diagonalone * diagonaltwo) * 100
        print ()
        print (" Area of Rhombus is",area,"Cm")
    if choice == 2:
        print ()
        print (" PERIMETER OF RHOMBUS ")
        side = float (input (" Side of Rhombus: "))
        perimeter = ( 4 * side ) * 100
        print ()
        print (" Perimeter of Rhombus is",perimeter,"Cm")
        
# (7) Trapezium
elif ch == 7:
    print ()
    print (" 1. Area of Trapezium")
    print (" 2. Perimeter of Trapezium")
    print ()
    choice = int ( input (" Enter your choice: "))
    if choice == 1:
        print ()
        print (" AREA OF TRAPEZIUM ")
        print ()
        sideone = float (input (" Side 1: "))
        sidetwo = float (input (" Side 2: "))
        height  = float  (input (" Height: "))
        area = (( 1/2 * height) * (sideone + sidetwo)) * 100
        print ()
        print (" Area of Trapezium is",area,"Cm")
    elif choice == 2:
        print ()
        print (" PERIMETER OF TRAPEZIUM")
        print ()
        sideone = float (input (" Side 1: "))
        sidetwo = float (input (" Side 2: "))
        sidethree = float (input (" Side 3: "))   
        sidefour = float (input (" Side 4: "))  
        print ()
        perimeter = ( sideone + sidetwo + sidethree + sidefour ) * 100
        
# (8) Cuboid
elif ch == 8:
    print ()
    print ( " 1. Total surface area of Cuboid")
    print ( " 2. Curved surface of Cuboid")
    print ( " 3. Volume of Cuboid")
    print ()
    choice = int ( input (" Enter your choice: "))
    if choice == 1:
        print ()
        print (" TOTAL SURFACE AREA OF CUBOID ")
        print ()
        l = float (input (" Lenght of Cuboid: "))
        b = float (input (" Breath of cuboid: "))
        h = float (input ( "Height of Cuboid: "))
        totalarea = (2 * ( l*b + b*h + h*l ))
        print ()
        print (" Total surface area of cuboid is",totalarea)
    elif choice == 2:
        print ()
        print (" CURVED SURFACE AREA OF CUBOID ")
        print ()
        l = float (input (" Lenght of Cuboid: "))
        b = float (input (" Breath of cuboid: "))
        h = float (input ( "Height of Cuboid: "))
        curvedarea = ( 2 * h * ( l + b))
        print ()
        print (" Curved surface area of cuboid is",curvedarea)
    elif choice == 3: 
        print ()
        print (" VOLUME OF CUBOID ")
        print ()
        l = float (input (" Lenght of Cuboid: "))
        b = float (input (" Breath of cuboid: "))
        h = float (input ( "Height of Cuboid: "))
        volumearea = ( l * b * h ) 
        print ()
        print (" Volume of cuboid is",volumearea)
        
 # (9) Cube
elif ch == 9:
    print ()
    print (" 1. Total surface area of cube")
    print (" 2. Curved surface area of cube")
    print (" 3. Volume of cube")
    print ()
    choice = int ( input (" Enter your choice: "))
    if choice == 1:
        print ()
        print (" TOTAL SURFACE AREA OF CUBE ")
        print ()
        side = float (input (" Side: "))
        totalarea = ( 6 * side * side ) * 100
        print ()
        print (" Total surface of cube is",totalarea,"Cm")
    elif choice == 2: 
        print ()
        print (" CURVED SURFACE AREA OF CUBE ")  
        print ()
        side = float (input (" Side: "))
        curvedarea = ( 4 * side ) * 100
        print ()
        print (" Curved surface area of cube",curvedarea,"Cm")
    elif choice == 3:
        print ()
        print (" VOLUME OF CUBE ")
        side = float (input (" Side: "))
        volume = ( side * side * side ) * 100
        print ()
        print (" Volume of cube is",volume,"Cm")
        
        
 # (10) Cylinder
elif ch == 10:
    print ()
    print (" 1. Total surface area of cylinder ")
    print (" 2. Curved surface area of cylinder ")
    print (" 3. Volume of cylinder ")
    print ()
    choice = int ( input (" Enter your choice: "))
    if choice == 1:
        print ()
        print (" TOTAL SURFACE AREA OF CYLINDER ")
        print ()
        diameter = float (input ( " Diameter of cylinder: "))
        height = float (input ( " Height of cylinder: "))
        radius = diameter / 2
        totalarea = ( 2 * 3.14 * radius * ( height + radius )) * 100
        print ()
        print (" Total surface area of cylinder is",totalarea,"Cm")
    elif choice == 2:
        print ()
        print (" CURVED SURFACE AREA OF CYLINDER ")
        print ()
        diameter = float (input ( " Diameter of cylinder: "))
        height = float (input ( " Height of cylinder: "))
        radius = diameter / 2
        curvedarea = ( 2 * 3.14 * radius * height)  * 100
        print ()
        print ( " Curved surface area of cylinder is",curvedarea,"Cm")
    elif choice == 3:
        print ()
        print (" VOLUME OF CYLINDER ")
        print ()
        diameter = float (input ( " Diameter of cylinder: "))
        height = float (input ( " Height of cylinder: "))
        radius = diameter / 2
        volume = ( 3.14 * radius * radius * height ) * 100
        print ()
        print (" Volume of cylinder is",volume,"Cm")
        
# (11) Sphere
elif ch == 11:
    print ()
    print ( " 1. Total surface area of sphere ")
    print ( " 2. Curved surface area of sphere ")
    print ("  3. Volume of sphere ")
    print ()
    choice = int (input (" Enter your choice"))
    if choice == 1:
        print ()
        print (" TOTAL SURFACE AREA OF SPHERE ")
        print ()
        diameter = float (input ( " Diameter of diameter: "))
        radius = diameter / 2
        totalarea = ( 4 * 3.14 * radius * radius ) * 100
        print ()
        print (" Total surace area of sphere is",totalarea,"Cm")
    elif choice == 2:
        print ()
        print ()
        diameter = float (input ( " Diameter of diameter: "))
        radius = diameter / 2
        curvedarea = ( 2 * 3.14 * radius * radius ) * 100
        print ()
        print (" Curved surace area of sphere is",curvedarea,"Cm")
    elif choice == 3:
        print ()
        print (" VOLUME OF SPHERE ")
        print ()
        diameter = float (input ( " Diameter of diameter: "))
        radius = diameter / 2
        volume = ( 4 /3 ) * ( 3.14 * radius * radius * radius ) * 100
        print ()
        print (" Volume of sphere is",volume,"Cm")   
        
elif ch == 0:
     exit()
    
            
        
        
        
        
        
        
    
        
        
        
    
        
        
      
    
        
                       
                       
                       
                       
                       
                     

