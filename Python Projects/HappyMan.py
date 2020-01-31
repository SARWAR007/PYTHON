if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = "EVAPORATE"
	guessed = "_" * len(word) 
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
	letter = input("guess letter: ")
	while True:
		if letter.upper() in lstGuessed:
			letter = ''
			print("Already guessed!!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '#'
			print(word)
			
		else:
			print(''.join(guessed))
			if letter is not '':
				letter = input("guess letter: ")

		if '_' not in guessed:
			print("You won!!")
			break
		    
        
