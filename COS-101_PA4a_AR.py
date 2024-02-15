# A function that returns the circumference of a circle with the given radius. 
# The circumference is given as 2*pi*radius. Sample runs would be as follows.

# print(circumference(4))
## 25.132741228718345

# print(circumference(7))
## 43.982297150257104

# Require the math module
import math

# Set a class
class CircumferenceCalc:
    
    # define my circumference function
    def circumference(radius):
        
        # take an overload 'radius' and return the function by multiplying it out
        return 2 * math.pi * radius

    # Prompt the user at the console, ensure it's a float and set this as the radius variable
    radius = float(input("Please enter a radius to calculate the circumference: "))

    # print out the method from your user input as the radius overload
    print(circumference(radius))

        