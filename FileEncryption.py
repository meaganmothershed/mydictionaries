info_security = open('info_security.txt','r')

file_encryption = info_security.read()

encrypted = open('encrypted.txt','w')

codes = {'A':'1','a':'2',
        'B':'3','b':'4',
        'C':'5','c':'6',
        'D':'7','d':'8',
        'E':'9','e':'0',
        'F':'!','f':'@',
        'G':'#','g':'$',
        'H':'%','h':'^',
        'I':'&','i':'*',
        'J':'(','j':')',
        'K':'-','k':'_',
        'L':'=','l':'+',
        'M':'`','m':'~',
        'N':'[','n':'{',
        'O':']','o':'}',
        'P':'<','p':',',
        'Q':'>','q':'.',
        'R':'a','r':'b',
        'S':'c','s':'d',
        'T':'e','t':'f',
        'U':'g','u':'h',
        'V':'i','v':'j',
        'W':'k','w':'l',
        'X':'m','x':'n',
        'Y':'o','y':'p',
        'Z':'q','z':'r',
        ' ':' ','.':'?',
        ':':';'}

for word in file_encryption:
    for symbol in word:
        encrypted.write(f'{codes[symbol]}')

encrypted.close()