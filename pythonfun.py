#python function
def greet():
    print("Hello, Raji!")

greet()
#fucntion without parameters 
def greet(name):
    print("hello", name)
greet("rajii")
greet("venky")
#function with parameters
def add(a,b):
    return a+b
print("addition of the given numbers:", add(12,45))
# lambda function 
a=int(input("enter first value:",))
b=int(input("enter second value:",))
add=lambda a,b: a+b
print("addition of the given numbers :",add(a,b))

