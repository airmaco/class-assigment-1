a = int(input("what is the temperature"))

def hot():
    print ("hot")

def chilly():
    print ("chilly")

def warm():
    print ("warm")



if a > 60 and a < 90 :
    warm()
elif a >= 90:
    hot()
else:
    chilly()

