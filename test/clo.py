# coding=utf-8

def dec(func):
    print('call dec')
    def in_dec(*arg):
        print('in_dec arg=', arg)
        if len(arg) == 0:
            return 0
        for i in arg:
            if not isinstance(i, int):
                return 0
        return func(*arg)
    return in_dec

@dec
def mysum(*arg):
    print 'in_mysum'
    return sum(arg)
mysum(1,2,3)
# mysum = dec(mysum)
# print(mysum(1,2,3,4,5))
            