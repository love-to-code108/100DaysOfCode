# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
arrowLetters = "H" #the arrow on the top and the bottom
legLetters = "" #a sing leg segment for the 'H'
middleLetters = "" #for the middle segment line
legSpace = "" #the space between the two legs
selectedWidth = int(s) #the selected width
middleHeight = int((selectedWidth + 1) / 2) #for the height of the middle segment line
for i in range(0,selectedWidth):
    #each line grwos by 2 more 'H'-s, one on each side
    print(arrowLetters.center((2 * selectedWidth) - 1,' ')) 
    arrowLetters = arrowLetters + "HH"
    legLetters = legLetters + "H"
    legSpace = legSpace + " "
arrowLetters = arrowLetters[:-2] #for the overflow
fullLeg = legLetters + legSpace + legSpace + legSpace + legLetters
middleLetters = legLetters + legLetters + legLetters + legLetters + legLetters
arrowNotch = int((len(arrowLetters) - selectedWidth) / 2)
lineWidth = (5 * selectedWidth) + arrowNotch
for i in range(0, selectedWidth + 1):
    print(fullLeg.rjust(lineWidth, ' '))
for i in range(0, middleHeight):
    print(middleLetters.rjust(lineWidth, ' '))
for i in range(0, selectedWidth + 1):
    print(fullLeg.rjust(lineWidth, ' '))
for i in range(0, selectedWidth):
    print(arrowLetters.rjust((lineWidth + arrowNotch - i),' '))
    arrowLetters = arrowLetters[:-2]