#!/usr/bin/python
import cgi, cgitb
import datetime
cgitb.enable()
form = cgi.FieldStorage()
y = form.getvalue('year')
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
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
    date_of_easter_num = datetime.date(year=y,month=n,day=p)
    return str(date_of_easter_num)

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
    z = datetime.date(month=n)
    x = int(str(p)[1])
    if x == 1:
        sup = "st"
    elif x == 2:
        sup = "nd"
    elif x == 3:
        sup = "rd"
    else:
        sup = "th"

    date_of_easter_str = str(p) + sup + ' of ' + str(month[(z-1)]) + ' ' + str(y))



if y.isalpha() == True:
    y = int(y)
else:
    print("<h2> This is not a valid year.</h2>")



if option == 'numeric':
    date_of_easter = Easter_Numeric(y)
elif option == 'string':
    date_of_easter = Easter_String(y)
else:
    date_of_easter = Easter_String(y) + Easter_Numeric(y)



print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head><title> Python Script</title></head>')
print('<body>')
print('<p>')
print('Easter in the year')
print(y)
print('will fall on')
print(date_of_easter)
print('.')
print('</p>')
print('</body>')
print('</html>')
