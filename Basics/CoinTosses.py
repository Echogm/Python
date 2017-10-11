import random
def tossthis(num):
    temp1 = 0
    temp2 = 0
    for i in range(1, num):
        tossing = random.randint(1,3)
        if tossing == 1:
            temp1 += 1
            print "Attempt #{}: Throwing a coin... It's a head got {} head(s) so far and {} tail(s) so far.".format(i,temp1,temp2)
        elif tossing == 2:
            temp2 += 1
            print "Attempt #{}: Throwing a coin... It's a tail got {} tail(s) so far and {} head(s) so far.".format(i,temp2,temp1)
    return

tossthis(5001)
