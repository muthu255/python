class Circle:
    def __init__(value,rad):#init method
        value.rad=rad
    def area(inte):
        return (22/7)*inte.rad*inte.rad
    def perimeter(value):
        return 2*(22/7)*(value.rad)
    def __str__(value):
        return 'Circle: radius={0}'.format(value.rad)
    def __rep__(value):
        return 'Circle({0}.rad)'.format(value.rad)
    def __eq__(value,other):
        if isinstance(other,Circle):
            return value.rad == other.rad
        else:
            return False
    def __lt__(value,other):
        return value.rad <= other.rad
    



r1=Circle(7)

print('Area of r1->',int(r1.area()))
print('Preimeter of r1->',int(r1.perimeter()))
print('Radius of r1->',r1.rad)
print(r1)

r2=Circle(5)

print('Area of r2->',int(r2.area()))
print('Preimeter of r2->',int(r2.perimeter()))
print('Radius of r1->',r2.rad)
print(r2)
print(r1 == 7)
print(r1 < r2)
