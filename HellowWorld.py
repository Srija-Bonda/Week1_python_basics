print("Hello World!")
#this is a comment
if 5>2:
    print("5 is greater than 2.") # this aswell
    x= 5
    y= 2
    print(type(x))
    Fruits = [ "Apple", "Banana", "Carrot" ]
    a,b,c= Fruits
    print(a+b+c)
    p=2
    q=3
    print(p+q)
    
    r= "yes"
    def myfunc():
        print("The answer is " + r)
        
    myfunc()
    print(r)
    
    i=1
    j=2.8
    k=5j
    #int to float conversion
    f=float(i)
    print(f)
    #float to int conversion
    g=int(j)
    print(g)
    #int to complex conversion
    h=complex(i)
    print(h)
    #to print the type of the assigned variable
    print(type(f))
    print(type(g))
    print(type(h))
    #to print a random number of the given range
    import random
    print(random.randrange(-1,10))
    
    #multiline string
    abc= """hi,
this is srija"""
    print(abc)