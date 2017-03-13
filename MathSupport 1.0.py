import math

def quadratic():
    print ('====================================================')
    print ('QuadraticFormula = (-b +- sqroot(b^2 - 4ac))/2a) \n')
    print ('Values are retrieved from Quadratic Equation (ax^2 + bx +c = 0) \n')
            
    a = int(input('Enter a value for a \n --> '))
    b = int(input('Enter a value for b\n --> '))
    c = int(input('Enter a value for c\n --> '))
            
    try:
        outcome1 = ((-b + math.sqrt((b**2) - (4 *a *c)))/(2*a))
        outcome2 = ((-b - math.sqrt((b**2) - (4 *a *c)))/(2*a))
        print ('---------------------------------------------------')
        print ('Your two outcomes are:')
        print (outcome1, outcome2)
                
    except ValueError:
        print ('Oops! That is either an invalid input or it contains an imaginary number')  
        
def areaofshape():    
    temp_list = ['1. Square', '2. Rectangle', '3. Circle', '4. Triangle', '5. Trapezoid', '6. Parallelogram', '0. Quit']
    print ('====================================================')
    print ('Please choose a shape')
    print ('\n'.join(temp_list))
    
    print ('---------------------------------------------------')
        
    selected_input_shapes = int(input('Enter a number now\n --> '))        
    
    if (selected_input_shapes == 1):                                        # Square
        print ('====================================================')
        print ('Area of Square = Length x Length \n')
        print ('What is the length?')
        
        x = int(input('Enter a value\n --> '))
        outcome = x * x
        print (outcome)
                
    if (selected_input_shapes == 2):                                        # Rectangle
        print ('====================================================')
        print ('Area of Rectangle = Width x Length \n')
        print ('What is the length?')
        x = int(input('Enter a value\n --> '))
        print ('What is the width?')
        y = int(input('Enter a value\n --> '))            
        outcome = x * y
        print (outcome)
        
    if (selected_input_shapes == 3):                                        # Circle
        print ('====================================================')
        print ('Area of Circle = Pi x radius power of 2 \n')
        print ('What is the radius?')
                    
        x = float(input('Enter a value\n --> '))
        outcome = (math.pi * math.pow(x, 2))
        print (outcome)   
                    
    if (selected_input_shapes == 4):                                        # Triangle
        print ('====================================================')
        print ('Area of Triangle = 1/2 x b x h \n')
        print ('What is the value for base?')
        b = float(input('Enter a value\n --> '))
        print ('What is the value for height?')
        h = float(input('Enter a value\n --> '))            
        outcome = ((1/2) * b * h)
        print (outcome)                           
             
    if (selected_input_shapes == 5):                                        # Trapezoid
        print ('====================================================')
        print ('Area of Trapezoid = (1/2) x h (b1 + b2)\n')
        print ('What is the value for top base?')
        b1 = float(input('Enter a value\n --> '))
        print ('What is the value for bottom base?')
        b2 = float(input('Enter a value\n --> '))  
        print ('What is the value for height?')
        h = float(input('Enter a value\n --> '))
        outcome = ( (1/2) * h * (b1 + b2))
        print (outcome) 
        
    if (selected_input_shapes == 6):                                        # Parallelogram
        print ('====================================================')
        print ('Area of Parallelogram = b x h \n')
        print ('What is the value for base?')
        b = float(input('Enter a value\n --> '))
        print ('What is the value for height?')
        h = float(input('Enter a value\n --> '))            
        outcome = (b * h)
        print (outcome)                       
                    
    if (selected_input_shapes == 0):                                        # Quit
        print ('Thank you for using MathSupport 1.0 Prototype')
        return 0
    
def math_program():
     
    option_list = ['1. Quadratic Formula', '2. Area of Shapes', '0. Quit']
    count_list = 0
    count_max = (len(option_list)-1)
   
    
    print ('\nThank you for using MathSupport 1.0 Prototype \nPlease select one of the following options from ', count_list, ' to ', count_max)
    print ('====================================================')
    print ('\n'.join(option_list))
    
    print ('---------------------------------------------------')
    
    selected_input = int(input('Enter a number now\n --> '))    
    
    # Quadratic Formula
    if (selected_input == 1):
        quadratic()

    # Area of Shapes
    if (selected_input == 2):
        areaofshape()
        
    # Quit
    if (selected_input == 0):                                                  
        print ('Thank you for using MathSupport 1.0 Prototype')
        return 0    
    
    

    

def main():
    math_program()
    
main()
input('Press ENTER to exit')
