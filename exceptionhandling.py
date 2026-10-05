# Exception handling
try:
    ival1=int(input("enter the value:"))
    ival2=ival1+50
    print("division is:", ival1/0)
    print(ival2)    
except ValueError as e:
    print("supplied value is not valid:", e)
except TypeError as e:
    print("wrong type:",e)
except ZeroDivisionError as e:
    print("zero division is not possible:",e)
except FileNotFoundError as e:
    print("the requested file is not available:",e)
finally:
    print("execution completed !")