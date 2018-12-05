#!/usr/bin/python3
import cgi, cgitb
import datetime
cgitb.enable()
form = cgi.FieldStorage()
y = int(form.getvalue('year'))

option = form.getvalue('Format')


def Easter_Numeric(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    date_of_easter_num = str(p) + '/' + '0' + str(n) + '/' + str(y)
    print(date_of_easter_num)

def Easter_String(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    if n == 3:
        n = 'March'
    else:
        n = 'April'
    x = int(str(p)[1])
    if x == 1:
        sup = 'st'
    elif x == 2:
        sup = 'nd'
    elif x == 3:
        sup = 'rd'
    else:
        sup = 'th'

    print(str(p) + '<sup>' + sup + '</sup>' + ' of ' + str(n) + ' ' + str(y))

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <meta charset="utf-8">')
print('<title> Python Script</title>')
print('<meta name="Easter" content="width = device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('</head>')
print('<body>')
print('<nav>')
print('<ul><li style="float:left">Easter Calculator!</li>')
print('<li><a href="../index.html">Home</a></li></ul>')
print('</nav>')
print('<p>')
if option == 'numeric':
    Easter_Numeric(y)
elif option == 'string':
    Easter_String(y)
else:
    Easter_Numeric(y)
    print('<br>')
    Easter_String(y)
print('</p>')
print('</body>')
print('</html>')
