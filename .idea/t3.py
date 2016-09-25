# i = 0
# numbers = []


def loop_test(i, t, z):
    numbers = []
    while i < t:
        print "At the top i is: %d" % i
        numbers.append(i)
        i += z
        print "Numbers now: ", numbers
        print "At the top i is: %d" % i
    return numbers


def loop_test2(x, y):
    numbers = []
    for i in range(x, y):
        numbers.append(i)
    return numbers


#print "The Numbers: "

#for num in numbers:
#    print num


