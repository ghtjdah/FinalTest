# 1번 문제
from itertools import count


def textfilter1(text):
    index=0
    newtext=''
    while(index != len(text)):
        if(text[index]=='<'):
            while(text[index]!='>'):
                newtext +=''
                index += 1
            else:
                newtext += ''
                index += 1
        else:
            newtext += text[index]
            index += 1
    else:
        return newtext


def textfilter2(text):
    fronti,backi = 0,0
    newtext = text
    while(True):
        if(newtext.find('<')==-1):
            break
        fronti = newtext.find('<')
        backi = newtext.find('>') + 1
        newtext = newtext.replace(newtext[fronti:backi],'')


    return newtext


#___main___
text=''' <html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
<hyml>'''


#print(textfilter1(text))
print(textfilter2(text))

