def findthis(x,char):
    new_list= []
    for i in range(0, len(x)):

        if x[i].find(char) != -1:
            new_list.append(x[i])

    print new_list

new_list = ['hello','world','my','name','is','Anna']
char = 'o'
findthis(new_list, char)
