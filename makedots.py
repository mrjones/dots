data = open('data.txt').read()

tokens = data.split(" ")

gridsize = 40

y = 0
leftmargin = 4 * gridsize
topmargin = 3 * gridsize
output = "<svg xmlns='http://www.w3.org/2000/svg' version='1.1'>"
for token in tokens:
    x = 0
    for char in token:
        if char != '1' and char != '0':
            continue
        color = "white"
        if char == '1':
            color = "blue"
        output += "<circle cx='%d' cy='%d' r='7' stroke='black' stroke-width='2' fill='%s' />" % ((leftmargin + gridsize * x), (topmargin + gridsize * y), color)
        x += 1
        if token == "00111111":
            output += "<text x='%d' y='%d' font-family='helvetica' font-size='20'>?</text>" % (leftmargin + gridsize * 8.33, topmargin + gridsize * (y + .25))
        else:
            output += "<line stroke='black' stroke-width='2' x1='%d' y1='%d' x2='%d' y2='%d' />" % ( leftmargin + gridsize * 8, topmargin + gridsize * (y + .25), leftmargin + gridsize * 9, topmargin + gridsize * (y + .25) )
    y += 1

output += "</svg>"


open('/var/www/dots.svg', 'w').write(output)
