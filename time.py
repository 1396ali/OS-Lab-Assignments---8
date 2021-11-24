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
t1 = Time(17,60,60)
t1.show()

t2 = Time(0,59,60)
t2.show()

t3 = Time(18,2,60)
t3.show()

time = Time(0,0,3600)

print('RESULT is (T1+T2 _ T2+T3 / T3-T1 _ T1-T2 / second->time _ time->second) :')

a = t1.sum(t2)
a.show()

b = t2.sum(t3)
b.show()

print('/')

c = t3.sub(t1)
c.show()

d = t1.sub(t2)
d.show()

print('/')

time.show()

t2.time_to_sec()