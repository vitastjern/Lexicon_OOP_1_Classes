# examples on decorators

'''
s = "Our global variable"

def func():

    print(locals())

func()

print(globals().keys())
'''

'''def hello(name = "Anna"):
    #return print("Hello " + name)
    print ("The hello() function has been executed")

    def greet():
        return "\t This is inside the greet() function"

    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

'''
'''greet = hello   # so you can assign methods!  Cool!  
                # Needs to be without parenthesises, then it doesn't get executed and can be passed around!
greet()

del hello  # removed hello, but still got greet... (error if hello() is uncommented)

#hello()
greet()'''
'''

hello()'''

def new_decorator(func):

    def wrap_func():
        print("Code would be herre, before executing the func")
        func()
        print("Code here will execute after func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator")

func_needs_decorator()

'''func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()'''
