import cmath

print("Welcome to the Quadratic Equation Solver ")

print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a +bj")
print("Where a is the real portion and bj if the imaginary portion.")


#user input to set how many equations to be solved
user_num = int(input("\nHow many equations would you like to solve today: "))
num_eq = list(range(1, user_num+1))

#for loop runs for as many times as specified by user input
for num in num_eq:
  print("\nSolving equation #" + str(num))
  a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
  b = float(input("Please enter your value of b (coefficient of x): "))
  c = float(input("Please enter your value of c (coefficient): "))
  
  # calculates results of equation
  d = (b**2) - (4*a*c)
  x1 = (-b-cmath.sqrt(d))/(2*a)
  x2 = (-b+cmath.sqrt(d))/(2*a)
  
  print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:" )
  print("\n\t\tx1 = (" + str(x1) + ")")
  print("\n\t\tx2 = (" + str(x2) + ")")

print("\nThanks for using the Quadratic Equation Solver.")




