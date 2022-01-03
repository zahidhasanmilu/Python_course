def funarg(normal,*args,**kwargs):
    print(n)
    for item in args:
        print(item)

    print("\n Now i Want to introduce with som important persons")
   
    for key,value in kwargs.items():
        print(f"{key} is a {value}")



n = "You are a student"
ar = ["Zahid","Hasan","Milu"]

kw = {
    "Zahid":"Student",
    "Hasan":"Job Holder",
    "Milu":"Programmer"
}

funarg(n,*ar,**kw)