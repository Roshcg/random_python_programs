fhandler = open( 'Dictionary.txt' )
fh = fhandler.read()

mydict = {}
print(fh)
fread = fh.split('\n')
print('hi')
print(fread)
for i in fread:
    if ':' in i:
        i = i.split(':')
        if i[0][:-1] not in mydict:
            mydict[i[0][:-1]] = i[1][1:]

print(mydict)
print()

while(1):
    op = input( '1. search the dictionary\n2. add the word to the dictionary\n3.delete the word in dictionary\n4. quit\n')
    if op == '1':
        w = input('enter the word to be searched in the dictionary :')

        if w in mydict:
            print(w , ':' , mydict[w])
        else:
            print('word is not present :(')

    if op == '2':
        word = input('enter the word :')
        meaning = input('enter the meaning:')
        mydict[word] = meaning

    if op == '3':
        word = input('enter the word to be deleted :')
        if word in mydict:
            del mydict[word]
        else:
            print('the word you are trying to dlete is not present in the dictionary :(')

    if op == '4':
        break
    print()
fwrite = open('Dictionary.txt','w')

for k, v in mydict.items():
    str = k +' : '+ v
    if str in fh:
        fwrite.write(str+'\n')
    if str not in fh:
        fwrite.write(str+'.\n')
