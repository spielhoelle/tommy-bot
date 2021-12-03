sting = """
Oh schoen von dir zu hoeren 🙂 Ich muss auch ab und zu an dich denken - es wird aber  weniger.
My computer crashed
Holi, basically now we could start
If you have nothing to do right now
Aber ich will dort hingehen
yes
We should meet in Berlin and talk about in person
You are great!
Just woke up in Bogot
Yes
now
basically
later will be a bit hard
1.5 hours
then a meeting what i maybe can shift
but then i dont know, I need to leave the airbnb
Oki cool
Come when you feel ready, sorry
Geh
🙈
Im in the red dress ..
On you laying on the floor
I go there now
And it finishes at 11
But I’m kinda weak, feels like a small fever
Maybe from the vaccination :(
Yeah
Maybe
Yeah, saving the world with orange wine would be a really transcendent goal
So you have plans? I think I stay here 
"""

lines = sting.split("\n")
print(lines[1])
print(lines[2])


from googletrans import Translator, constants
from pprint import pprint
translator = Translator()
translations = translator.translate(lines, dest='en')
result = []
for translation in translations:
	print(translation.text)
	result.append(translation.text)


translation_result_text="\n\r".join(result)
target_filename = "./data/translated_messages.txt"
print("Creating file:", target_filename)
text_file = open(target_filename, "w")
text_file.write(translation_result_text)
text_file.close()
