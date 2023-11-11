from tkinter import *
from tkinter import ttk
from translate import Translator
from unidecode import unidecode

Screen = Tk()
Screen.geometry('550x250')
Screen.resizable(0, 0)
Screen['bg'] = 'teal'
Screen.title("Translator")

# Set default font
font_style = ("Helvetica", 12)

LanguageChoiceInput = StringVar()
LanguageChoiceTranslate = StringVar()

LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Spanish', 'Greek', 'Arabic'}

# Set default values
LanguageChoiceInput.set('English')
LanguageChoiceTranslate.set('Greek')

def transliterate_text(text):
    return unidecode(text)

def Translate():
    source_language = LanguageChoiceInput.get()
    target_language = LanguageChoiceTranslate.get()

    translator = Translator(from_lang=source_language, to_lang=target_language)
    text_to_translate = TextVar.get()
    translated_text = translator.translate(text_to_translate)

    # Transliterate the translated text
    transliterated_text = transliterate_text(translated_text)

    # Display the transliterated text
    OutputVar.set(transliterated_text)

# Choice for input language
LanguageChoiceInputMenu = OptionMenu(Screen, LanguageChoiceInput, *LanguageChoices)
Label(Screen, text="Choose a Language", bg='teal', fg='black', font=font_style).grid(row=0, column=1)
LanguageChoiceInputMenu.config(bg='teal', fg='black', font=font_style)  # Set background color and font
LanguageChoiceInputMenu.grid(row=1, column=1)

# Choice in which the language is to be translated
NewLanguageMenu = OptionMenu(Screen, LanguageChoiceTranslate, *LanguageChoices)
Label(Screen, text="Translated Text", bg='teal', fg='black', font=font_style).grid(row=0, column=2)
NewLanguageMenu.config(bg='teal', fg='black', font=font_style)  # Set background color and font
NewLanguageMenu.grid(row=1, column=2)

Label(Screen, text="Enter Text", bg='teal', fg='black', font=font_style).grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar, bg='teal', fg='black', font=font_style)  # Set background color and font
TextBox.grid(row=2, column=1)

Label(Screen, text="Output Text", bg='teal', fg='black', font=font_style).grid(row=2, column=2)
OutputVar = StringVar()
TextBox = Entry(Screen, textvariable=OutputVar, bg='teal', fg='black', font=font_style).grid(row=2, column=3)

# Button for calling function with a blue background
B = Button(Screen, text="Translate", command=Translate, bg='teal', fg='black', font=font_style)
B.grid(row=3, column=1, columnspan=3)

Screen.mainloop()
