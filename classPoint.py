class Point:
    #init with properties
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    #method get the sum of squares the properties
    def sqSum(self):
        return (self.x**2+ self.y**2 + self.z**2 )

x=Point()
print(x.sqSum())