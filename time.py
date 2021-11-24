class Time:
    def __init__(self , hour=0 , minute=0 , second=0):
        self.h = hour
        self.m = minute
        self.s = second

        self.correct()

    def show(self):
        print("[", self.h ,":", self.m ,":", self.s , "]")

    def correct(self):
        while self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.s < 0:
            self.s += 60
            self.m -= 1
        

        while self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.m < 0:
            self.m += 60
            self.h -= 1

    def sum(self , other):
        return Time(self.h + other.h , self.m + other.m , self.s + other.s)

    def sub(self , other):
        return Time(self.h - other.h , self.m - other.m , self.s - other.s)

    def time_to_sec(self):
       res = self.h*3600 + self.m*60 + self.s
       print(res , "ثانیه")
       return res


print('Times are (T1 _ T2 _ T3 _ second) : ')

t1_h = int(input('Enter hour time : '))
t1_m = int(input('Enter minute time : '))
t1_s = int(input('Enter second time : '))

t1 = Time(t1_h,t1_m,t1_s)
t1.show()


t2_h = int(input('Enter hour time : '))
t2_m = int(input('Enter minute time : '))
t2_s = int(input('Enter second time : '))

t2 = Time(t2_h,t2_m,t2_s)
t2.show()


t3_h = int(input('Enter hour time : '))
t3_m = int(input('Enter minute time : '))
t3_s = int(input('Enter second time : '))

t3 = Time(t3_h,t3_m,t3_s)
t3.show()


time_second = int(input('Enter second : '))

time = Time(0,0,time_second)


print('RESULT is (T1+T2 _ T2+T3 / T2-T1 _ T3-T2 / second(input)->time _ time(T3)->second) :')

a = t1.sum(t2)
a.show()

b = t2.sum(t3)
b.show()

print('/')

c = t2.sub(t1)
c.show()

d = t3.sub(t2)
d.show()

print('/')

time.show()

t3.time_to_sec()
