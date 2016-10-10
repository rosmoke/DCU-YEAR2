
def get_plural(word):
	consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z","w","y"]
	if word.lower().endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("s") or word.endswith("z"):
		word = word + "es"
		return(word)
	if len(word) > 1:
		if word[-2].lower() in consonant and word.lower().endswith("y"):
			word = word[:-1] + "ies"
			return(word)
		if word.lower().endswith("fe"):
			word = word[:-2] + "ves"
			return(word)
		elif word.lower().endswith("f"):
			word = word[:-1] + "ves"
			return(word)
		elif word.lower().endswith("o"):
			word = word + "es"
			return(word)
		else:
			word = word + "s"
			return(word)
	if word.lower().endswith("f"):
		word = word[:-1] + "ves"
		return(word)
	elif word.lower().endswith("o"):
		word = word + "es"
		return(word)
	return(word)