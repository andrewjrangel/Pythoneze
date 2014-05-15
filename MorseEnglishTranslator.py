englishToMorse= {"a" : ".-",
				"b" : "-...", 
				"c" : "-.-.",
				"d" : "-..",
				"e" : ".",
				"f" : "..-.",
				"g" : "--.",
				"h" : "....",
				"i" : "..",
				"j" : ".---",
				"k" : "-.-",
				"l" : ".-..",
				"m" : "--",
				"n" : "-.",
				"o" : "---",
				"p" : ".--.",
				"q" : "--.-",
				"r" : ".-.",
				"s" : "...",
				"t" : "-",
				"u" : "..-",
				"v" : "...-",
				"w" : ".--",
				"x" : "-..-",
				"y" : "-.--",
				"z" : "--..",
				" " : " ",
				"1" : ".----", 
				"2" : "..---", 
				"3" : "...--", 
				"4" : "....-", 
				"5" : ".....", 
				"6" : "-....", 
				"7" : "--...", 
				"8" : "---..", 
				"9" : "----.", 
				"0" : "-----", 
				"," : "--..--", 
				"." : ".-.-.-", 
				"?" : "..--..", 
				"/" : "-..-.", 
				"-" : "-....-"}

inputString = raw_input("What would you like translated to Morse Code?: ")
inputString = inputString.lower()

inputList = []
outputList = []
dictToList = []

for x in range(0, len(inputString)):
	inputList.append(inputString[x])
	
#print inputList

for key, value in englishToMorse.iteritems():
	dictToList.append(key)

#print dictToList

tempSet = set(dictToList).intersection(inputList)
tempList = list(tempSet)
inputSet = set(inputList).intersection(inputList)

inputLength = len(inputSet)
compareLenght = len(tempList)

if	len(inputSet) == len(tempList):
	for x in range(0, len(inputList) ):
		key = inputList[x]
		outputList.append(englishToMorse[key])
		
	print " ".join(outputList)
else:
	print "FAIL!"






