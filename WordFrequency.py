infile = open('sometext.txt','r')
mydict = {}

sometext = infile.read().split(' ')

for word in sometext:
    if word in mydict:
        mydict[word] += 1
    else:
        mydict[word] = 1


for k,v in mydict.items():
    print(f'{k}: {v}')


    