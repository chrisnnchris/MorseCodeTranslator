englishToMorseDict = {
	'a': "*-",
	'b': "-***",
	'c': "-*-*",
	'd': "-**",
	'e': "*",
	'f': "**-*",
	'g': "--*",
	'h': "****",
	'i': "**",
	'j': "*---",
	'k': "-*-",
	'l': "*-**",
	'm': "--",
	'n': "-*",
	'o': "---",
	'p': "*--*",
	'q': "--*-",
	'r': "*-*",
	's': "***",
	't': "-",
	'u': "**-",
	'v': "***-",
	'w': "*--",
	'x': "-**-",
	'y': "-*--",
	'z': "--**",
	'1': "*----",
	'2': "**---",
	'3': "***--",
	'4': "****-",
	'5': "*****",
	'6': "-****",
	'7': "--***",
	'8': "---**",
	'9': "----*",
	'0': "-----"
}
def englishToMorse(stringInput):
	translateString = "";
	print("This is the stringInput: " + stringInput)
	for x in range(0, len(stringInput)):
		print(stringInput[x])
		print("translated")
		print(englishToMorseDict[stringInput[x].lower()])
		translateString+=englishToMorseDict[stringInput[x].lower()] + " "
	return translateString
test = "hello";
translated = englishToMorse(test)
print(translated)