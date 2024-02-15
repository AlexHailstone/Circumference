# A function that returns the circumference of a circle with the given radius. 
# The circumference is given as 2*pi*radius. Sample runs would be as follows.

# print(circumference(4))
## 25.132741228718345

# print(circumference(7))
## 43.982297150257104


class CircumferenceCalc:
    def circumference(radius):
        return 2 * math.pi * radius

    # Sample runs
    print(circumference(4))  # Expected: 25.132741228718345
    print(circumference(7))  # Expected: 43.982297150257104
        