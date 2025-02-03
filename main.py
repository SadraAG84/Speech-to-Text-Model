import speech_recognition as sr  

# Initialize the recognizer object that will be used for speech recognition
r = sr.Recognizer()

def record_text():
    # This function continuously listens to the microphone input and returns the recognized text.
    # The loop ensures that it will retry in case of errors or unrecognized speech.

    while True:
        try:
            # Use the microphone as the source of audio input
            with sr.Microphone() as source2:
                # Adjust for ambient noise to improve recognition accuracy, increasing the duration of adjustment
                r.adjust_for_ambient_noise(source=source2, duration=0.45)  # increased duration for noise adjustment

                # Inform the user to start speaking
                print("Please speak now...")
                
                # Capture the audio from the microphone
                audio2 = r.listen(source=source2)

                # Use Google's speech recognition to convert the audio to text
                MyText = r.recognize_google(audio2)
                
                # Print the recognized text to the console
                print("You said:", MyText)

                # Check if the user said "thank you goodbye" (case-insensitive)
                if "thank you goodbye" in MyText.lower():
                    print("Goodbye!")  # Print a goodbye message
                    return None  # Stop the program by returning None
                
                # Return the recognized text if it's not the exit phrase
                return MyText

        except sr.RequestError as e:
            # Handle the case where the request to the Google API fails (e.g., network issue)
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            # Handle the case where the speech is not understood
            print("Could not understand the audio, please try again.")
        
    return  # Return None if there's an error or it should exit

def output_text(text):
    # This function writes the recognized text to a file called "output.txt"
    # It appends the new text to the file, preserving previous content.

    with open("output.txt", "a") as f:
        # Write the recognized text to the file followed by a newline
        f.write(text)
        f.write("\n")

    return  # End the function

# Main loop: Continuously recognize speech and save it to a file
while True:
    # Call the record_text function to capture speech and return recognized text
    text = record_text()
    
    # If the returned text is None, it means the exit phrase "thank you goodbye" was said
    if text is None:
        break  # Exit the loop and stop the program
    
    # If speech was successfully recognized, write it to a file
    output_text(text)

    # Print the recognized text that was written to the file
    print("Wrote text:", text)
