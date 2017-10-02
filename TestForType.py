def testForType(obj):
    if type(obj) is int:
        if obj >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    elif type(obj) is str:
        if len(obj) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif type(obj) is list:
        if len(obj) >= 10:
            print "Big list!"
        else:
            print "Short list."
    else:
        print "I have no idea what that is"

testForType(45)
testForType(100)
testForType(455)
testForType(0)
testForType(-23)
testForType("Rubber baby buggy bumpers")
testForType("Experience is simply the name we give our mistakes")
testForType("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
testForType("")
testForType([1,7,4,21])
testForType([3,5,7,34,3,2,113,65,8,89])
testForType([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
testForType([])
testForType(['name','address','phone number','social security number'])