import pyttsx3

#Converts the given text to speech using pyttsx3 library and plays it out loud
def text_to_speech_pyttsx3(text):

    # Initialize the TTS engine using pyttsx3
    engine = pyttsx3.init()
    # Set the speed of the speech (how fast the speech is read out)
    engine.setProperty('rate', 150)  # Speed of speech words per minute (optional)
    # Set the volume of the speech (between 0.0 and 1.0)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0, optional)
    
    # To change the voice (male or female):
    voices = engine.getProperty('voices')
    # Set the voice for speech. Here, we are setting the voice to the first available voice.
    engine.setProperty('voice', voices[1].id)  # 0 is male, 1 is female

     # The engine reads the text aloud. The 'say' function tells the engine to speak the provided text
    engine.say(text)

    # Wait for the speech to complete before continuing the execution of the program.
    # This function ensures the program doesn't terminate until the speech is finished.
    engine.runAndWait()

def read_text_file(file_path):
    # Open the text file and read the content
    with open(file_path, 'r') as file:
        text = file.read()
    return text


file_path = r'C:/Users/asus/Desktop/New folder (6)/output.txt'  
text = read_text_file(file_path)
text_to_speech_pyttsx3(text)
