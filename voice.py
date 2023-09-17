import speech_recognition as sr
import serial

# initialize the speech recognizer
r = sr.Recognizer()
ser = serial.Serial('COM6', 9600)

# define a function to recognize speech input
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    try:
        # use the Google Speech-to-Text API to transcribe the speech input
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech-to-Text could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech-to-Text service; {0}".format(e))
        return None

# define a function to turn the lights on
def turn_lights_on():
    ser.write('1'.encode()) 
    print("Lights turned on")

# define a function to turn the lights off
def turn_lights_off():
    ser.write('0'.encode()) 
    print("Lights turned off")

# loop to continuously recognize speech input
while True:
    # recognize speech input
    # text = recognize_speech()
    
    # if the wake word "Assistant" is detected, wait for the next command
    # if "Assistant" in text:
    print("What can I do for you?")
    # recognize the next command
    command = recognize_speech()
    # check if the command is to turn the lights on or off
    if "turn the lights on" in command:
        turn_lights_on()
    elif "turn the lights off" in command:
        turn_lights_off()
    else:
        print("I'm sorry, I didn't understand your command.")
