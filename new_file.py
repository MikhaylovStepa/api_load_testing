import time
import json

a = {"asdf":1234, 'asdffdfd':'sddfdf'}
print(json.dumps(a))
b = json.dumps(a)

def name():
    print('name')

def my_dec(func):
    def wrap():
        print('Hallo')
        func()
        print('Buy')
    return wrap


def last_dec(func):
    def wrap():
        func()
        print('See you soon')
    return wrap

@my_dec
def name():
    print('Steve')

print()



@last_dec
@my_dec
def last():
    print('Steve')
last()


def dec_agrs(func):
    def wrap(a1, a2):
        print('hello')
        func(a1,a2)
        return 'dec hello', func(a1,a2)
    return wrap

@dec_agrs
def new_f(a, b):
    print(a)
    print(b)
    #time.sleep(3.45)
    return a

a = new_f('asdf funct','qwer')
print(new_f('asdf','qwer'))

#time.sleep(3.45)
print()
print(type(3.45))