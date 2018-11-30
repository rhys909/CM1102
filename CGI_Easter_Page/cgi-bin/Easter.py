#
import cgi, cgitb
import datetime
form = cgi.FieldStorage()
y = form.getvalue('year')
if y.isalpha() == True:
    y = int(y)
    return y
else:
    print("<p> This is not a valid year.</p>")

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
    print(datetime.date(year=y,month=n,day=p))

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
    x = datetime.date(year=y,month=n,day=p)
    print(datetime.strptime(x, %d %B %Y))

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<HTML>')
