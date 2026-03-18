import speech_recognition as sr
import pyttsx3
import keyboard
import time
import threading
# Right now the custom commands are tailored to work with League of Legends, 
# but they can be easily modified to work with any game or application by changing 
# the key presses and commands as needed.

recognizer = sr.Recognizer()

def speak(text):
    def _speak_thread():
        tts = pyttsx3.init()
        tts.say(text)
        tts.runAndWait()
    thread = threading.Thread(target=_speak_thread, daemon=True)
    thread.start()

def my_function():
    print("Waiting for 'p' to start...")
    keyboard.wait('p')
    if keyboard.is_pressed('p'):
        print("Program started. Press 'p' again to stop.")
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio)
                command = command.lower()
                print(f"You said: {command}")

                if "hello" in command:
                    speak("Hello! How can I assist you today?")
                    
                if "forward" in command:
                    print("Moving forward...")
                    keyboard.press('w')  # Simulate pressing the 'W' key to move forward
                    time.sleep(1)  # Simulate a short press
                    keyboard.release('w')  # Release the 'W' key
                    speak(command)
                    
                    
                if "backward" in command:
                    print("Moving backward...")
                    keyboard.press('s')  # Simulate pressing the 'S' key to move backward
                    time.sleep(1)  # Simulate a short press
                    keyboard.release('s')  # Release the 'S' key
                    speak(command)
                    
                    
                if "left" in command:
                    print("Moving left...")
                    keyboard.press('a')  # Simulate pressing the 'A' key to move left
                    time.sleep(1)  # Simulate a short press
                    keyboard.release('a')  # Release the 'A' key
                    speak(command)
                    
                    
                if "flash" in command:
                    print("Flashing...")
                    keyboard.press('d')  # Simulate pressing the 'D' key to move right  
                    time.sleep(1)  # Simulate a short press
                    keyboard.release('d')  # Release the 'D' key
                    speak(command)
                    
                if "jump" in command:
                    print("Jumping...")
                    keyboard.press('space')  # Simulate pressing the 'Space' key to jump
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('space')  # Release the 'Space' key
                    speak(command)
                    
                if "double jump" in command:
                    print("Double jumping...")
                    keyboard.press('space')  # Simulate pressing the 'Space' key to jump
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('space')  # Release the 'Space' key
                    keyboard.press('space')  # Simulate pressing the 'Space' key to jump
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('space')  # Release the 'Space' key
                    speak(command)
                
                if "charge" in command:
                    print("Pressing Q")
                    keyboard.press('q')  # Simulate pressing the 'Q' k
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('q')  # Release the 'Q' key
                    speak(command)
                    
                if "block" in command:
                    print("Pressing W")
                    keyboard.press('w')  # Simulate pressing the 'W' key
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('w')  # Release the 'W' key
                    speak(command)
                    
                if "spin" in command:
                    print("Pressing E")
                    keyboard.press('e')  # Simulate pressing the 'E' key
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('e')  # Release the 'E' key
                    speak(command)
                    
                if "ult" in command:
                    print("Pressing R")
                    keyboard.press('r')  # Simulate pressing the 'R' key
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('r')  # Release the 'R' key
                    speak(command)
                    
                if "flash" in command:
                    print("Pressing f")
                    keyboard.press('f')  # Simulate pressing the 'F' key
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('f')  # Release the 'F' key
                    speak(command)
                    
                if "be toxic" in command:
                    print("Being toxic")
                    keyboard.press_and_release('t')  # Simulate pressing the 'T' key
                    keyboard.press_and_release('y, o, u, s, u, c, k')  # Simulate pressing the 'Y', 'O', 'U', 'S', 'U', 'C', 'K' keys
                    keyboard.press('enter')  # Simulate pressing the 'Enter' key
                    time.sleep(0.5)  # Simulate a short press
                    keyboard.release('enter')  # Release the 'Enter' key
                    speak(command)
                    

                if "exit" in command or keyboard.is_pressed('p'):
                    print("Exiting program.")
                    speak("Goodbye!")
                    break

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as req_err:
                print(f"Could not request results; {req_err}") 
                
if __name__ == "__main__":
    my_function()