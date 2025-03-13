#Task 4: Factorial using Loops and Recursion 
#1. Implement two functions to calculate the factorial of a given number: 
#1.a. One function using a for loop. 
#1.b. Another function using recursion. 
#2. Ask the user for a number and print its factorial using both methods.

n = int(input("Enter the number: "))
def factorial(n):
    fact = 1
    for i in range(1, n + 1):  # Changed 'num' to 'n'
        fact *= i
    print("Factorial of a number using for loop:", fact)

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

factorial(n)
print("Factorial of a number using recursive method:", factorial_recursive(n))
