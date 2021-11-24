class Complex:
    def __init__(self,real,imaginary):
        self.r = real
        self.i = imaginary
    
    def show(self):
        print(self.r ,'+ (' , self.i ,'i )')

        
    def sum(self , other):
        return Complex(self.r + other.r , self.i + other.i)
    
    def sub(self , other):
        return Complex(self.r - other.r , self.i - other.i)

    def mul(self , other):
        return Complex(self.r * other.r - self.i * other.i , self.r * other.i + self.i * other.r)

    def div(self , other):
        return Complex((self.r * other.r + self.i * other.i)/(other.r*other.r + other.i*other.i) , (self.i * other.r - self.r * other.i)/(other.r*other.r + other.i*other.i))


a_real = int(input('Enter first real : '))
a_imaginary = int(input('Enter first imaginary : '))
x = Complex(a_real , a_imaginary)

print()

b_real = int(input('Enter second real : '))
b_imaginary = int(input('Enter second imaginary : '))
y = Complex(b_real , b_imaginary)


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
