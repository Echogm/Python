x = [4, 6, 1, 3, 5, 7, 25]
def starthis(x):
    stars = "*"
    for i in range (0,len(x)):
        print x[i] * stars

    return
starthis(x)
print " "
z = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_part2(container):
    stars = "*"
    for i in container:
        if type(i) == int:
            print i * stars
        elif type(i) == str:
            print i[0].lower() * len(i)
    return
draw_part2(z)
