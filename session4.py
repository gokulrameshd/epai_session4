import random
from decimal import Decimal
import math


def banker_round(n,p = 1):
    if n > 0 :
        if abs(n*(10*p) )- abs(n*(10*p)//1) >= 0.5:
            if ((n*(10*p)//1)+1)% 2 == 0:##
                return(((n*(10*p)//1)+1)/10*p)
            else:
                return((n*(10*p)//1)/(10*p))
        else:
            return(abs(n*(10*p)//1)/10*p)
    elif n == 0:
        return 0
    else:
        if abs(abs(n)*(10*p) )- abs(n*(10*p)//1) >= 0.5:
            if ((abs(n)*(10*p)//1)-1)% 2 == 0:##
                return ((-1)*(((abs(n)*(10*p)//1)-1)/10*p))
            else:
                return ((-1)*((abs(n)*(10*p)//1)/(10*p)))
        else:
            return((-1)*(abs(abs(n)*(10*p)//1)/10*p))

class Qualean():
    def __init__(self,n):
        self.n = n
        if self.n in [-1 , 0, 1]:
            pass
        else:
            raise ValueError("n should be one these following values -1 , 0, 1 ")
        self.q_n = self.n * random.uniform(-1,1)
        self.q = Decimal(self.q_n)
        self.qn = (banker_round(self.q,p = 1))
        
    def __str__(self):
    #         return format(self.qn , 'f15')
        return f'{self.qn}'

    def __add__(self, value):
    #         self.a = self.qn + value
        try: 
            return self.qn + value
        except:
            return self.qn + value.qn
    #         print( self.qn + value.qn)

    def __and__(self, value):
        try:
            return self.qn & value.qn
        except:
            return bool(self.qn )

    def __or__(self, value):
        try:
            return self.qn | value.qn
        except:
            return bool(self.qn)

    def __repr__(self):
        return(f'{self.qn}')

    def __gt__(self,value):
        return self.qn > value.qn

    def __ge__(self,value):
        return self.qn >= value.qn

    def __le__(self,value):
        return self.qn <= value.qn

    def __lt__(self,value):
        return self.qn < value.qn

    def __eq__(self,value):
        try:
            return self.qn == value.qn
        except:
            return self.qn == value

    def __mul__(self ,value):
        try: 
            return self.qn * value
        except:
            return self.qn * value.qn

    def __sqrt__(self):
        return (float(self.qn))**(1/2)


    def __float__(self):
        return float(self.q)

    def __invertsign__(self):
        return -(self.qn)

    def __bool__(self):
        return self.qn > 0
