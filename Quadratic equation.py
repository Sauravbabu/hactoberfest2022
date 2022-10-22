import cmath

print("Enter the Value of a: ", end="")

a = int(input())

print("Enter the Value of b: ", end="")

b = int(input())

print("Enter the Value of c: ", end="")

c = int(input())

discriminant = (b**2) - (4*a*c)

solutionOne = (-b-cmath.sqrt(discriminant))/(2*a)

solutionTwo = (-b+cmath.sqrt(discriminant))/(2*a)

print("\nRoot 1 =", solutionOne)

print("Root 2 =", solutionTwo)
