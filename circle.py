#A program to compute the diameter, circumference and area of a circle
pi = 3.14

radius = input("Radius = ")

diameter = 2*int(radius)

circumference = pi*int(diameter) #pi = 3.14

area = pi*int(radius)*int(radius)

print(f"Diameter = {diameter}\nCircumference = {circumference}\nArea = {area}")

