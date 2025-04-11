import customtkinter as ctk
import eng_to_ipa as ipa
import pyttsx3

# Appearance configuration
ctk.set_appearance_mode('dark')

# Text-to-speech engine initialization
engine = pyttsx3.init()

# Configure English voice and adjust speed
def configure_english_voice():
    for voice in engine.getProperty('voices'):
        if 'en' in voice.languages or 'English' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 120)  # Adjust speech rate (default is usually around 200)

configure_english_voice()

# Main functionality
def convert_to_ipa():
    input_text = text_input.get()
    ipa_text = ipa.convert(input_text)
    original_text_label.configure(text=input_text, text_color='white')
    ipa_result_label.configure(text=ipa_text, text_color='green')
    text_input.delete(0, 'end')

def listen_to_pronunciation():
    text_to_speak = original_text_label.cget("text")
    if text_to_speak:
        engine.say(text_to_speak)
        engine.runAndWait()

# Main window
app = ctk.CTk()
app.title('Text to IPA Converter')
app.geometry('600x250')

# Labels and input
text_label = ctk.CTkLabel(app, text='Text to convert:')
text_label.pack(pady=5)

text_input = ctk.CTkEntry(app, placeholder_text='Enter your text here', width=500)
text_input.pack(pady=10)

# Buttons
convert_button = ctk.CTkButton(app, text='Convert to IPA', command=convert_to_ipa)
convert_button.pack(pady=10)

listen_button = ctk.CTkButton(app, text='Listen to Pronunciation', command=listen_to_pronunciation)
listen_button.pack(pady=10)

# Output labels
original_text_label = ctk.CTkLabel(app, text='')
original_text_label.pack(pady=0)

ipa_result_label = ctk.CTkLabel(app, text='')
ipa_result_label.pack(pady=0)

# Run the application
app.mainloop()
