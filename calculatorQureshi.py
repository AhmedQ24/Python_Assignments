def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y
    
x = int(input("Enter the x value "))
y = int(input("Enter the y value "))
    
print x, " * ", y, " is equal to: ", multiply(x, y)
print x, " + ", y, " is equal to: ", add(x, y)
print x, " - ", y, " is equal to: ", subtract(x, y)
print x, " / ", y, " is equal to: ", divide(x, y)
