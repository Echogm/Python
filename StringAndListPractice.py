# Find And Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace ("day", "moth",1)

# Min And Max
xi = [2,54,-2,7,12,98]
print xi
print min (xi)
print max (xi)

# First And Last
y = ["hello",2,54,-2,7,12,98,"world"]
print y
last = len(y) -1
newList = [y[0],y[last]]
print newList

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
flist = x[:len(x)/2]
slist = x[len(x)/2:]
slist.insert(0,flist)
print slist
