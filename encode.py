import sys

if len(sys.argv) < 2:
    sys.stderr.write('Usage: python encode.py <message>\n')
    sys.exit(1)

def getAsciiForCharacter(char):
    return ord(char)


def convertToBinary(code):
    word = ""
    for x in range(0,8):
        c = code % 2
        code = code / 2
        word = str(c) + word
    return word

output = ""
print "Encoding message: %s" % sys.argv[1]
for char in sys.argv[1]:
    n = getAsciiForCharacter(char)
    output += convertToBinary(n) + " "
open('data.txt', 'w').write(output)
