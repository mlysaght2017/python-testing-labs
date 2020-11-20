class Calculate(object):
    def add(self,x,y):
        if type(x) == int and type(y) == int:
            return x+y
        else:
            raise TypeError("Invalid Type")
        
if __name__ =='__main__':
    calc = Calculate()
    result = calc.add("Hello","World")
    print(result)