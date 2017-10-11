def comparethis(x,y):
    if x == y:
        print "They are equal."
    else:
        print "They are not equal."
    return comparethis

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

comparethis(list_one,list_two)

list_one1 = [1,2,5,6,5]
list_two1 = [1,2,5,6,5,3]

comparethis(list_one1,list_two1)

list_one2 = [1,2,5,6,5,16]
list_two2 = [1,2,5,6,5]

comparethis(list_one2,list_two2)

list_one3 = ['celery','carrots','bread','milk']
list_two3 = ['celery','carrots','bread','cream']

comparethis(list_one3, list_two3)
