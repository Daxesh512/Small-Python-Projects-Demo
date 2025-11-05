#make sure to run the below pip install before running code.
#pip install pyspellchecker

from spellchecker import SpellChecker
corrector  = SpellChecker()

text = input("Enter Text:")

#for letter in text:
if text not in corrector:
    print("Original letter =", text)
    correct_letter = corrector.correction(text)
    print("Correct letter =", correct_letter)