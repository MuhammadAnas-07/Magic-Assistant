import speech_recognition as sr  # Library for speech recognition
import pyttsx3  # Library for text-to-speech conversion
import webbrowser  # Library for opening web pages
import pyjokes  # Library to fetch jokes
import re  # Library for regular expressions
import datetime  # Library to fetch date and time

# Function to capture and recognize speech
def sptext():
    recognizer = sr.Recognizer()  # Initialize recognizer object
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")  # Inform the user that it's listening
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture audio
        try:
            print("Recognizing...")  # Start recognition process
            data = recognizer.recognize_google(audio)  # Use Google's speech recognition
            print(data)  # Print recognized text
            return data  # Return recognized speech text
        except sr.UnknownValueError:  # Handle if the speech is unintelligible
            response = ("Sorry, I can't Understand. What are you saying!")
            print(f"{response}{speechtx(response) or ''}")  # Provide feedback through speech synthesis

# Function for text-to-speech conversion
def speechtx(x):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    voices = engine.getProperty("voices")  # Get available voices
    engine.setProperty("voice", voices[1].id)  # Set the voice to female (index 1)
    engine.setProperty("rate", 150)  # Set the speech rate to 150 words per minute
    engine.say(x)  # Convert the text to speech
    engine.runAndWait()  # Ensure the speech is processed before proceeding

# Function to fetch jokes from pyjokes library
def py_jokes(x):
    jokes = pyjokes.get_joke("en", x)  # Get a joke in English of the specified category
    return jokes  # Return the fetched joke

# Function to open a web page in a new browser tab
def py_web(x):
    web = webbrowser.open_new_tab(x)  # Open the specified URL in a new browser tab
    return web

# Function that returns a list of websites to be opened
def web_list(urls):
    urls = ["google", "facebook", "youtube", "gmail", "instagram"]  # List of websites
    return urls  # Return the list

# Main program logic
if __name__ == "__main__":
    while True:  # Continuous loop for voice commands
        try:
            user_name = "Anas"  # User's name is stored
            data1 = sptext().lower()  # Convert recognized speech to lowercase for uniform comparison
            
            # Respond if the user asks for the name
            if "your name" in data1:
                name = "My name is Magic"  # Set the assistant's name
                speechtx(name)  # Say the assistant's name

            # Respond to a greeting
            elif "hello" in data1:
                greeting = f"Hi, {user_name}\nHow are you?"  # Create a personalized greeting
                speechtx(greeting)  # Speak the greeting

            # Respond if the user asks how old the assistant is
            elif "old are you" in data1:
                response = "I don't have an age like humans do, but I was created by you"  # Response for age-related queries
                print(f"{response}{speechtx(response) or ''}")  # Print and speak the response

            # If the user requests a joke
            elif re.search(r"tell .* joke", data1):  # Use regex to match any phrase containing "tell" and "joke"
                if "chuck" in data1:  # Check if the user requests a Chuck Norris joke
                    response = py_jokes("chuck")  # Fetch a Chuck Norris joke
                elif "neutral" in data1:  # Check if the user requests a neutral joke
                    response = py_jokes("neutral")  # Fetch a neutral joke
                else:
                    response = py_jokes("all")  # Fetch any joke if no specific type is requested
                print(f"{response}{speechtx(response) or ''}")  # Print and speak the joke

            # If the user asks for the current time
            elif "time" in data1:
                response = datetime.datetime.now().strftime("%I%M%p")  # Get current time in 12-hour format without colons
                formatted_time = f"{response[:2]}:{response[2:4]} {response[4:]}"  # Insert colon and preserve AM/PM
                print(f"{formatted_time} {speechtx(response) or ''}")  # Print and speak the formatted time

            # If the user requests to open a website
            elif "open" in data1:
                urls = web_list(urls='')  # Get the list of websites
                for i in urls:
                    if i.lower() in data1.lower():  # Case-insensitive check if website is mentioned
                        print(f"Opening {i.title()}...")  # Inform the user which site is being opened
                        py_web(f"https://www.{i}.com/")  # Open the website
                        break  # Exit loop after opening the website
                else:
                    print(f"What would you like to open? {speechtx('what would you like to open?') or ''}")  # If no site matches

            # Exit the loop if the user says "exit"
            elif "exit" in data1:
                print(f"Thank you {speechtx('thank you') or ''}")  # Thank the user before exiting
                break  # Break out of the loop and end the program

        except AttributeError as es:
            print(f"Error: {es}")  # Catch any attribute errors and display them
