import random
import emojis

l1, l2 = ['a', 'e', 'i', 'o', 'u'], list()
for element in range(5):
	l2.append(l1[element].upper())
vowels = l1 + l2

def owo_convertor(text):
    """ Its your OwO Convertor """
	# replacing 'L', 'i', 'R' and 'r' with 'W' and 'w' respectively
    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')
	# deal with ending
    text = end(text, '!', '! {}'.format(random.choice(emojis.ending)))
    text = end(text, '?', '? owo')
    text = end(text, '.', '. {}'.format(random.choice(emojis.ending)))
    for element in vowels:
        if 'n{}'.format(element) in text:
            text = text.replace('n{}'.format(element), 'ny{}'.format(element))
        if 'N{}'.format(element) in text:
            text = text.replace('N{}'.format(element), 'N{}{}'.format('Y' if element.isupper() else 'y', element))
    return text

def end(s, old, new):
    l = s.rsplit(old, 1)
    return new.join(l)

if __name__=="__main__":
	text = input("Enter Your Text : ")
	owo_translation = owo_convertor(text)
	print("Your Translation : ", owo_translation)