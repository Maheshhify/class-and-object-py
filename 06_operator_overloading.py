class point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def sum(self,p):
        return point((self.x + p.x),(self.y + p.y))
    
    def print_point(self):
        print(f"x is {self.x} and y is {self.y}") 
        
    def __add__(self,p):
        return point((self.x + p.x),(self.y + p.y))
p1 = point(3,1)
p2 = point(5,5)

# p = p1.sum(p2) #Returns new point which is sum of p1 and p2
p = p1 + p2
p.print_point()

