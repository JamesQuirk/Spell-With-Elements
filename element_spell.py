import pandas as pd

elements_df = pd.read_csv('elements.csv')
symbols = elements_df['Symbol'].str.lower().values
MAX_WINDOW = elements_df['Symbol'].map(len).max()	# Essentially longest element symbol available.


def respell(word,el_spelling):
	'''
	Recursively respell 'word' with element symbols and build up 'el_spelling'
	'''
	print(word,'->',el_spelling)
	
	# Shelfing the values passed to this node allows for back-tracking.
	shelf_out = el_spelling
	shelf_word = word

	for win_size in range(1,MAX_WINDOW+1):
		sub_str = word[:win_size]
		if sub_str in symbols:
			el_spelling += sub_str.upper() if win_size == 1 else (sub_str[0].upper() + sub_str[1:])
			word = word[win_size:]
			word, el_spelling = respell(word,el_spelling)
			if word != '':
				# Back-track! <- solution not reached on this route.
				word = shelf_word
				el_spelling = shelf_out
			else:
				break
	return word, el_spelling

def spell_with_elements(word):
	print('Evaluating:',word)
	word = word.lower()
	possible = True
	el_spelling = ''	# Init output

	word, el_spelling = respell(word,el_spelling)

	possible = word == ''	# Deemed possible if entirety of 'word' can be respelled.

	return possible, el_spelling

# Test
for word in ['LION',
	'ELEMENTS',
	'PERIODIC',
	'FOOTBALL',
	'EUROS',
	'CONGRATULATIONS',
	'Nonrepresentationalisms',
	'Floccinaucinihilipilification',
	'supercalifragilistic']:
	print(word,spell_with_elements(word))