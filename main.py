#Functional Programming
def subtract (x,y):
  return x - y
  print (subtract(10,4))

def divide (x,y):
  return x / y
  print (divide(10,4))

def do_math (action, x, y):
  return action (x,y)
print (do_math (subtract, 10, 4))
print (do_math (divide, 10, 4))


#OOP Programming
class do_math:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def subtract (self):
        return self.val1 - self.val2
    
    def divide (self):
        return self.val1 / self.val2
    
math_instance = do_math (10, 4)
print (math_instance.subtract())
print (math_instance.divide())