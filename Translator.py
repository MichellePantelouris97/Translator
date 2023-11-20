from tkinter import *
from tkinter import ttk
from translate import Translator
from unidecode import unidecode

def transliterate_text(text):
    return unidecode(text)

def translate_text():
    source_language = LanguageChoiceInput.get()
    target_language = LanguageChoiceTranslate.get()

    translator = Translator(from_lang=source_language, to_lang=target_language)
    text_to_translate = TextVar.get()
    translated_text = translator.translate(text_to_translate)

    # Transliterate the translated text
    transliterated_text = transliterate_text(translated_text)

    # Display the transliterated text
    OutputVar.set(transliterated_text)

def toggle_fullscreen(root):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

Screen = Tk()
Screen.geometry('600x300')
Screen.resizable(0, 0)
Screen['bg'] = '#f4f4f4'  # Light background color
Screen.title("Sophisticated Translator")

# Remove icon from title bar
Screen.iconbitmap('')  # Pass an empty string to remove the icon

# Set default font
font_style = ("Helvetica", 12)

# Frames for organization
frame_input = ttk.LabelFrame(Screen, text="Input", padding=(10, 5), labelanchor="n", borderwidth=5)
frame_output = ttk.LabelFrame(Screen, text="Output", padding=(10, 5), labelanchor="n", borderwidth=5)
frame_languages = ttk.LabelFrame(Screen, text="Language Selection", padding=(10, 5), labelanchor="n", borderwidth=5)

frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame_output.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
frame_languages.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Supported languages
LanguageChoices = ['Hindi', 'English', 'French', 'German', 'Spanish', 'Greek', 'Arabic', 'Japanese', 'Korean']

LanguageChoiceInput = StringVar()
LanguageChoiceTranslate = StringVar()

# Set default values
LanguageChoiceInput.set('English')
LanguageChoiceTranslate.set('Greek')

# Choice for input language
ttk.Label(frame_languages, text="Choose Source Language:", background='#f4f4f4', font=font_style).grid(row=0, column=0, pady=5, sticky="w")
LanguageChoiceInputMenu = ttk.Combobox(frame_languages, textvariable=LanguageChoiceInput, values=LanguageChoices, state="readonly")
LanguageChoiceInputMenu.grid(row=0, column=1, pady=5, sticky="w")

# Choice for target language
ttk.Label(frame_languages, text="Choose Target Language:", background='#f4f4f4', font=font_style).grid(row=0, column=2, pady=5, sticky="w")
LanguageChoiceTranslateMenu = ttk.Combobox(frame_languages, textvariable=LanguageChoiceTranslate, values=LanguageChoices, state="readonly")
LanguageChoiceTranslateMenu.grid(row=0, column=3, pady=5, sticky="w")

# Text input
Label(frame_input, text="Enter Text:", background='#f4f4f4', font=font_style).grid(row=0, column=0, pady=5, sticky="w")
TextVar = StringVar()
TextBox = Entry(frame_input, textvariable=TextVar, bg='#ffffff', fg='#333333', font=font_style)
TextBox.grid(row=1, column=0, pady=5, sticky="nsew")

# Output display
ttk.Label(frame_output, text="Translated Text:", background='#f4f4f4', font=font_style).grid(row=0, column=0, pady=5, sticky="w")
OutputVar = StringVar()
OutputBox = Entry(frame_output, textvariable=OutputVar, bg='#ffffff', fg='#333333', font=font_style)
OutputBox.grid(row=1, column=0, pady=5, sticky="nsew")

# Translate button
B = Button(Screen, text="Translate", command=translate_text, bg='#ffffff', fg='#333333', font=font_style)
B.grid(row=2, column=0, columnspan=2, pady=10)

# Button for toggling fullscreen
ToggleFullscreenButton = Button(Screen, text="Toggle Fullscreen", command=lambda: toggle_fullscreen(Screen), bg='#ffffff', fg='#333333', font=font_style)
ToggleFullscreenButton.grid(row=3, column=0, columnspan=2, pady=10)

# Configure column and row weights
for i in range(2):
    Screen.columnconfigure(i, weight=1)
    Screen.rowconfigure(i, weight=1)

frame_languages.columnconfigure(1, weight=1)
frame_languages.columnconfigure(3, weight=1)

# Run the Tkinter event loop
Screen.mainloop()


