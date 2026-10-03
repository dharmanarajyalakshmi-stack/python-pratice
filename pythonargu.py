# types of arguments
# variable length arguments
def add(a, b):
    return a + b

print("addition of the given numbers:", add(12, 45))

# kwargs
def details(**info):
    print(info)

details(name="raji", age=21)
