try:
    a=10/0
except:
    print("exception raised")
else:
    print("no exception")
finally:
    print("this is final block")
print("outside the try")
