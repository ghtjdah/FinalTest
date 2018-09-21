# 1번 문제

def textfilter(text):
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

print(text)
print(textfilter(text))
