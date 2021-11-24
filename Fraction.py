import math

class Fract:
    def __init__(self,up,down):
        self.u = up
        self.d = down
    
    def show(self):
        print(self.u , '/' , self.d)
    
    def simp(self , other):
        sim = math.gcd(other.u , other.d)
        other.u = other.u // sim
        other.d = other.d // sim
        return other

    def sum(self , other):
        return self.simp(Fract(self.u * other.d + self.d * other.u , self.d * other.d))

    def sub(self , other):
        return self.simp(Fract(self.u * other.d - self.d * other.u , self.d * other.d))

    def mul(self , other):
        return self.simp(Fract(self.u * other.u , self.d * other.d))

    def div(self , other):
        return self.simp(Fract(self.u * other.d , self.d * other.u))


a_up = int(input('Enter first up : '))
a_down = int(input('Enter first down : '))
x = Fract(a_up , a_down)

b_up = int(input('Enter second up : '))
b_down = int(input('Enter second down : '))
y = Fract(b_up , b_down)

print('INPUT first & second :')
x.show()
y.show()

print('RESULT + & - & * & / :')
plus = x.sum(y)
plus.show()

mines = x.sub(y)
mines.show()

mult = x.mul(y)
mult.show()

divide = x.div(y)
divide.show()
