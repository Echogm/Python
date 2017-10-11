def scorethis(x):
    for i in range(0,x):
        import random
        random_num = random.randint(0,101)
        # l = 100 * random_num
        if random_num >90:
            print "Score:",random_num,"Your grade is A"
        elif random_num >80:
            print "Score:",random_num,"Your grade is B"
        elif random_num >70:
            print "Score:",random_num,"Your grade is C"
        elif random_num < 70:
            print "Score:",random_num,"Your grade is D"

    return

scorethis(10)
