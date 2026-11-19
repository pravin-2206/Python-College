try:
    print(x)
except NameError:
    print("X is not defined")
except:
    print("Something else")
    