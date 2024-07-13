import pyaudio
from googletrans import Translator
from datetime import datetime  
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from forex_python.converter import CurrencyRates
import string
import os
import time
import pyautogui
import psutil
import wave
import keyboard
import pygame
import datetime
import json  
import pytz
import re
import random
import folium
from geopy.geocoders import Nominatim
import nltk
from nltk.corpus import wordnet
from datetime import date, timedelta
import holidays
from pydub import AudioSegment
from pydub.playback import play
from bs4 import BeautifulSoup
from textblob import TextBlob
import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw
import requests
import polyline
import pyjokes

import soundfile as sf
import noisereduce as nr
import os

from Game_Scripty import *
from paths import *
import playsound







FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open PyAudio stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER)

engine = pyttsx3.init()

# Set properties for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 




def voice_into_text():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=FRAMES_PER_BUFFER)
    seconds = 4
    frames = []
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
    
    # Stop and close PyAudio stream
    stream.stop_stream()
    stream.close()

    # Convert raw audio data to AudioData
    audio_data = b"".join(frames)
    audio_data_instance = sr.AudioData(audio_data, sample_rate=RATE, sample_width=2)

    recognizer = sr.Recognizer()

    try:
        # Transcribe in English
        text_en = recognizer.recognize_google(audio_data_instance, language="en-US")
        print("Transcribed text (English):", text_en)
        return text_en
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        engine.say("Sorry, I couldn't understand what you said.")
        engine.runAndWait()
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def music_player_wav(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the playback speed
    pygame.mixer.quit()
    pygame.quit()

def write_to_notepad(title, content):
    # Open Notepad
    subprocess.Popen(["notepad.exe"]).wait()
    time.sleep(1)  # Wait for Notepad to open

    # Simulate typing the title
    pyautogui.write(title + '\n')

    # Simulate typing the content
    pyautogui.write(content,interval=0.02)




def open_application_by_name(app_name, application_path=None):
        try:
            if application_path == None:
                subprocess.Popen(['start', '', app_name], shell=True)
                print(f"Opening")
                    
        except Exception as e:
            
            print(f"Error: {e}")

def is_application_running(app_name):
    for proc in psutil.process_iter(['name']):
        
        if app_name.lower() in proc.info['name'].lower():
            
            return True
    return False

def close_application_by_name(app_name):
    try:
        subprocess.run(['taskkill', '/f', '/im', app_name], check=True)
        engine.say(f"Closed {app_name} successfully")
        engine.runAndWait()
    except subprocess.CalledProcessError:
        engine.say(f"Failed to close {app_name}")
        engine.runAndWait()
        
    

def record_audio():


    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    engine = pyttsx3.init()

    
    engine.say('Directory path to save the record ')
    engine.runAndWait()
    save_record_audio_path = input("Enter the directory path to save the recorded audio: ")

    
    engine.say("The file name ")
    engine.runAndWait()
    save_record_audio_name_as = input("Enter the name of the audio file to save: ")
    
    
    engine.say('Extension of the file ')
    engine.runAndWait()
    extension = input("Enter the file extension (e.g., wav, mp3, etc.): ")
    

    if not extension.startswith('.'):
        extension = '.' + extension

    file_path = os.path.join(save_record_audio_path, save_record_audio_name_as + extension)

    os.makedirs(save_record_audio_path, exist_ok=True)  # Ensure the directory exists
    print("* Recording... Press Ctrl+S to stop.")

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        # Check if Ctrl+S is pressed to stop recording
        if keyboard.is_pressed('ctrl+s'):
            break

    engine = pyttsx3.init()
    engine.say("* Recording stopped.")
    engine.runAndWait()
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error: {0}".format(e))



def play_audio():
    # Load the audio file
    engine.say("file path")
    engine.runAndWait()
    filename = input("Enter the file path ")
    
    audio = AudioSegment.from_file(filename)

    # Play the audio
    play(audio)
    


def alarm_and_transcribe(text):
    
    def set_alarm(alarm_time):
        pygame.init()
        pygame.mixer.init()



        stop_alarm = False

        # Define a callback function to stop the alarm when Ctrl+S is pressed
        def stop_alarm_callback(event):
            nonlocal stop_alarm
            if event.name == 's' and keyboard.ctrl_pressed:
                stop_alarm = True

        keyboard.on_press(stop_alarm_callback)

        while True:
            if stop_alarm:
                print("alarm stopped.")
                break

            current_time = datetime.datetime.now()
            if current_time >= alarm_time:
                print("Alarm! It's time to wake up!")
                for i in range(3):
                    engine.say('Alarm stopped')
                    engine.runAndWait()
                break

    
            else:
                time_left = alarm_time - current_time
                print(f"Time left until alarm: {time_left}")
                time.sleep(1)  # Check every sec

    # Extract hours and minutes using regular expression
    numbers = re.findall(r'\d+', text)
    hours = int(numbers[0])
    minutes = int(numbers[1])
    
    print("Hours:", hours)
    print("Minutes:", minutes)

    # Speak out the transcribed text
    engine.say("You said: " + text)
    engine.runAndWait()

    # Set the alarm time
    alarm_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)

    # Call the function to set alarm
    set_alarm(alarm_time)



    
def timers(text):

    input_str = text.lower()

    # Use regular expressions to find the time duration in the input string
    time_pattern = r"(\d+)\s*(minute|min|minutes|second|sec|seconds)"
    matches = re.findall(time_pattern, input_str)

    mins = 0
    secs = 0

    # Iterate over the matches and accumulate the time duration
    for match in matches:
        value, unit = match
        if 'min' in unit:
            mins += int(value)
        elif 'sec' in unit:
            secs += int(value)

    # Calculate total seconds
    total_seconds = mins * 60 + secs
    
    # Start the timer
    engine.say("Timer started for {} minutes and {} seconds.".format(mins, secs))
    engine.runAndWait()
    for remaining_time in range(total_seconds, 0, -1):
        if remaining_time <= 3:
            
            engine.say("{}".format(remaining_time))
            engine.runAndWait()
            print("{} seconds remaining...".format(remaining_time))

        else:
            print("{} seconds remaining...".format(remaining_time))
            time.sleep(1)
    
    for i in range(3):
        engine.say("Timer Stopped")
        engine.runAndWait()


def record_audio_transcribe_and_speak():

    while True:
        FORMAT = pyaudio.paInt16  # Format of the audio
        CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
        RATE = 44100              # Sample rate (samples per second)
        CHUNK = 1024              # Number of frames per buffer
        RECORD_SECONDS = 5        # Duration of the recording
        
        p = pyaudio.PyAudio()

        # Open PyAudio stream for recording
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        print("Recording...")

        frames = []

        # Record audio in chunks and append to frames
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Recording finished.")

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Transcribing recorded audio to text...")

        # Convert audio frames to audio data
        audio_data = b''.join(frames)

        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Recognize the speech
        try:
            audio = sr.AudioData(audio_data, RATE, 2)  # Create AudioData object
            text = recognizer.recognize_google(audio, language='en-US')
            print("Transcription:", text)
            
            
            # Text-to-speech conversion in English
            engine = pyttsx3.init()
            engine.say(text)   # Speak transcribed text in English
            engine.runAndWait()
            

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        if 'exit' in text:
            engine.say("exiting the translator")
            engine.runAndWait()
            break


    
def record_audio_transcribe_and_execute():
    FORMAT = pyaudio.paInt16  # Format of the audio
    CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100              # Sample rate (samples per second)
    CHUNK = 1024           # Number of frames per buffer
    RECORD_SECONDS = 4        # Duration of the recording
    
    print("solving math problems")
    
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set properties for a female voice

    def solve_math_problem(operation, num1, num2):
        result = None
        if operation == "addition":
            result = num1 + num2
        elif operation == "subtraction":
            result = num1 - num2
        elif operation == "multiplication":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        remainder = num1 % num2  # Calculate remainder for division
        return result, remainder

    def speak_result(operation, num1, num2):
        try:
            print(f"Solving {operation} of {num1} and {num2}...")
            result, remainder = solve_math_problem(operation, num1, num2)
            if operation == "division":
                engine.say(f"The result of {operation} of {num1} and {num2} is {result} with remainder {remainder}")
            else:
                engine.say(f"The result of {operation} of {num1} and {num2} is {result}")
            engine.runAndWait()
        except Exception as e:
            print("Error:", e)

    p = pyaudio.PyAudio()  # Initialize PyAudio

    while True:  # Loop continuously until "stop" command is received
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)  # Open PyAudio stream for recording
        print("lets solve math problems....")

        frames = []  # List to store audio frames

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)  

        stream.stop_stream()  # Stop and close the stream
        stream.close()

        audio_data = b''.join(frames)  # Convert audio frames to audio data

        recognizer = sr.Recognizer()  # Initialize recognizer

        try:
            audio = sr.AudioData(audio_data, RATE, 2)  # Create AudioData object
            text = recognizer.recognize_google(audio, language='en-US')  # Recognize the speech
            print("Transcription:", text)

            command = text.lower()  # Process the transcribed text

            if 'stop' in command:  # Check if the command is "stop"
                engine.say("i'm stopping solving math problems")
                engine.runAndWait()
                break

            if any(op in command for op in ["addition", "subtraction", "multiplication", "division"]):
                operation = next(op for op in ["addition", "subtraction", "multiplication", "division"] if op in command)
                numbers = [int(num) for num in command.split() if num.isdigit()]
                if len(numbers) == 2:
                    num1, num2 = numbers
                    speak_result(operation, num1, num2)
                else:
                    print("Invalid command")
            else:
                print("Command not recognized")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    
def random_password(text):
    
    
    
    print("Transcription:", text)
    
    # Extract name from the transcribed text
    name = text.split("by using name ")[-1]
    
    # Generate random password with embedded name
    numbers = '1234567890'
    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!\";#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    # Initialize password with first character as a letter
    password = random.choice(string.ascii_letters)
    
    # Include at least one character from each category
    password += random.choice(numbers)
    password += random.choice(lowercase_characters)
    password += random.choice(uppercase_characters)
    password += random.choice(symbols)
    
    # Add remaining characters with embedded name
    for _ in range(random.randint(1, 3)):
        password += random.choice(string.ascii_letters + numbers + symbols)
    password += name
    for _ in range(random.randint(1, 3)):
        password += random.choice(string.ascii_letters + numbers + symbols)
        
    # Shuffle the characters
    random_password_with_embedded_name = ''.join(random.sample(password, len(password)))

    print(f"Random Password by using Name:{name}", random_password_with_embedded_name)
    
    # Save password to a file
    
    os.makedirs(save_password_path, exist_ok=True)
    password_file_path = os.path.join(save_password_path, "generated_password.txt")
    mode = 'a' if os.path.exists(password_file_path) else 'w'  # Append if file exists, otherwise write
    with open(password_file_path, mode) as file:
        if os.stat(password_file_path).st_size != 0:
            file.write("\n")
        file.write(json.dumps({name: random_password_with_embedded_name}))
    print("Password saved to:", password_file_path)
    
    
    # Text-to-speech conversion
    engine = pyttsx3.init()
    engine.say(f"Random Password by using Name {name} : {random_password_with_embedded_name} ")
    engine.runAndWait()

    
def display_route_on_map(text):
    
    # Function to geocode an address and return its coordinates
    def geocode_address(address):
        geolocator = Nominatim(user_agent="navigation_app")
        location = geolocator.geocode(address)
        return location.latitude, location.longitude

    # Extract starting and destination locations
    start_location = text.split("from ")[-1].split(" to ")[0]
    destination_location = text.split("to ")[-1].split()[0]

    # Check if both start and destination locations are extracted successfully
    if start_location and destination_location:
        engine.say(f"Starting Location:{start_location}")
        engine.runAndWait()
        engine.say(f"Destination Location:{destination_location}" )
        engine.runAndWait()
    else:
        print("Failed to extract starting and/or destination locations. Please check the input text format.")

    # Geocode the addresses
    point1 = geocode_address(start_location)
    point2 = geocode_address(destination_location)

    if point1 and point2:
        # Create a folium map
        map_center = [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
        mymap = folium.Map(location=map_center, zoom_start=10)

        # Add markers for the addresses
        folium.Marker(point1, popup="Location A").add_to(mymap)
        folium.Marker(point2, popup="Location B").add_to(mymap)

        # Retrieve the route between the addresses
        url = f"https://router.project-osrm.org/route/v1/driving/{point1[1]},{point1[0]};{point2[1]},{point2[0]}"
        response = requests.get(url)
        route_data = response.json()

        # Extract the route geometry
        route_geometry = route_data['routes'][0]['geometry']

        # Decode the polyline string into coordinates
        decoded_route = polyline.decode(route_geometry)

        # Add the route to the map
        folium.PolyLine(locations=decoded_route, color="blue").add_to(mymap)

        # Extract total distance in kilometers
        total_distance = route_data['routes'][0]['distance'] / 1000  # Convert meters to kilometers

        # Add total distance as a marker at the top left of the map with increased font size
        top_lat = max(point1[0], point2[0]) + 0.02  # Slightly above the highest latitude of the route
        left_lon = min(point1[1], point2[1]) - 0.02  # Slightly to the left of the leftmost point of the route
        folium.Marker(
            [top_lat, left_lon],
            icon=folium.DivIcon(html=f"<div style='font-weight: bold; font-size: 20px;'>Total Distance: {total_distance:.2f} km</div>")
        ).add_to(mymap)
        
        engine.say(f"the total distance from {start_location} to {destination_location} is {total_distance} km")
        engine.runAndWait()
        
        # Save the map as an HTML file in the specified folder
        engine.say("here is the map")
        engine.runAndWait()
        
        map_file_path = os.path.join(save_Map_Route_map, "route_map2.html")
        mymap.save(map_file_path)

        # Display the HTML content in the notebook
        os.system(f'"{map_file_path}"')
    
def Show_the_map():
    
    os.system(f'"{map_route_path}"')
    
    
def Currancy(text):
    c = CurrencyRates()
    
    # Split the text to extract currencies
    parts = text.split(" ")

    # Check if the second part is 'into', if so, the amount should be in the first part
    if "into" in parts:
        if parts[1] == 'into':
            amount = float(parts[0])  # Convert amount to float
            from_currency = parts[2].upper()
            to_currency = parts[-1].upper()
        else:
            amount = float(parts[1])  # Convert amount to float
            from_currency = parts[2].upper()
            to_currency = parts[-1].upper()
        converted_amount = c.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        engine.say(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        engine.runAndWait()
    else:
        engine.say("I can not understand you")
        engine.runAndWait()
    
    

def get_random_joke():
    joke = pyjokes.get_joke()
    # Split the joke based on punctuation marks
    parts = joke.split('?')  # Split at question marks
    if len(parts) < 2:
        parts = joke.split('.')  # Split at periods if question mark is not found
    if len(parts) < 2:
        parts = joke.split('!')  # Split at exclamation marks if period is not found
    if len(parts) < 2:
        return None, None  # Return None for both question and answer if unable to split
    
    # The first part is the question, and the remaining parts are the answer
    question = parts[0].strip() + '?'  # Add the question mark back
    answer = '.'.join(parts[1:]).strip()  # Join the remaining parts for the answer
    
    print(question)
    engine.say(question)
    engine.runAndWait()
    time.sleep(2)
    print(answer)
    engine.say(answer)
    engine.runAndWait()
    
def get_random_fact():
    
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()['text']
    print(fact)
    engine.say(fact)
    engine.runAndWait()
    
def get_word_definition(word):
    
    word = word.split()[-1]
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        print(f"Definition of{word} is {definition}")
        engine.say(f"Definition of{word} is {definition}")
        engine.runAndWait()
    else:
        print(f"No definitions found for the word {word}")
        
        engine.say(f"No definitions found for the word {word}")
        engine.runAndWait()
        
        

def next_holiday():
    indian_holidays = holidays.India()

    # Start from tomorrow
    tomorrow = date.today() + timedelta(days=1)

    # Find the next holiday
    next_holiday = None
    for d in (tomorrow + timedelta(n) for n in range((date(tomorrow.year, 12, 31) - tomorrow).days + 1)):
        if d in indian_holidays:
            next_holiday = (d, indian_holidays.get(d))
            break

    if next_holiday:
        days_until_holiday = (next_holiday[0] - tomorrow).days
        print("Next holiday:", next_holiday[0], "-", next_holiday[1])
        engine.say(f"The next Holiday is {next_holiday[1]} on {next_holiday[0]}")
        engine.runAndWait()
        
        if days_until_holiday == 0:
            print("Countdown:", days_until_holiday, "days remaining")
            print(f"that means tomorrow is an holiday! happy {next_holiday[1],next_holiday[0]}")
            engine.say(f"that means tomorrow is an holiday! happy {next_holiday[1]}")
            engine.runAndWait()
        elif days_until_holiday == 1:
            print("Countdown:", days_until_holiday, "day remaining")
            engine.say(f"{days_until_holiday} day remaining")
            engine.runAndWait()
        else:
            print("Countdown:", days_until_holiday, "days remaining")
            engine.say(f"{days_until_holiday} days remaining")
            engine.runAndWait()
    else:
        print("No upcoming holidays.")



def News_Summaries(query):
    
    if query:
        query = query.split('about')[1]
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={News_Summaries_api_key}"
        response = requests.get(url)
        data = response.json()
        if 'articles' in data and data['articles']:
            article = data['articles'][0]
            title = article['title']
            summary = article['description']
            
            print(title)
            engine.say(title)
            engine.runAndWait()
            
            time.sleep(1)
            
            print(summary)
            engine.say(summary)
            engine.runAndWait()
        else:
        
            engine.say("No articles found.")
            engine.runAndWait()
    else:
        engine.say("Sorry Can't understand")
        engine.say()
        
 

def word_association_game():
    
    engine.say("Welcome to the Word Association Game!")
    engine.say("I'll say a word, and you respond with the first word that comes to your mind.")
    
    
    print("And.. if you want to stop the game press Ctrl + s!!")
    engine.say("if you want to stop the game press Ctrl + s!!")
    engine.runAndWait()
    engine.say("Let's get started!\n")
    engine.runAndWait()

    while True:
        # Select a random word from the dictionary
        word = random.choice(list(word_associations.keys()))

        # Display the word and prompt the user for their response
        print(f"Word: {word}")
        engine.say(f"The word is {word}")
        engine.runAndWait()

        # Record voice
        print("speak : ")
        text_en = voice_into_text()
        print("Your response:", text_en)

        
        # Check if the response matches any associated words
        if text_en.lower() in word_associations[word]:
            print('Correct!')
            engine.say("Correct!")
            engine.runAndWait()

            
            engine.runAndWait()
            
        elif "stop" == text_en:
            print("exiting the game")
            engine.say("exiting the game")
            engine.runAndWait()
            break
        
        else:
            print("Incorrect !")
            engine.say("Incorrect ! ")
            print("The associated words are:", ", ".join(word_associations[word]))
            engine.say(f"The associated words are : {word_associations[word]}")
            engine.runAndWait()
            continue


def guess_and_play_sound():
    
    print("Welcome to Guess the Sound Game!")
    engine.say("Welcome to Guess the Sound Game!")
    engine.runAndWait()
    
    print("Listen to the sound and try to guess what it is.")
    engine.say("Listen to the sound and try to guess what it is.")
    engine.runAndWait()
    
    
    while True:
        # Select a random sound file
        sound_name = random.choice(list(sound_files.keys()))
        description = sound_files[sound_name]
        
        # Get the file path for the selected sound
        guess_the_sound = get_sound_filepath(sound_name)


        # # Function to play the audio file
        music_player_wav(guess_the_sound)
        
        print('speak...')
        guess = voice_into_text()
        print("you said : ",guess)

        # Check if the guess is correct
        if guess == description.lower():
            engine.say("Correct! You guessed it right.")
            engine.runAndWait()
        
        elif "stop" in guess:
            print("exiting the game")
            engine.say("exiting the game")
            engine.runAndWait()
            break
        
        else:
            engine.say(f"Sorry, the correct answer was {description}.")
            engine.runAndWait()


def rock_paper_scissor():
    
    webbrowser.open('file://' + rock_paper_scissor)


def word_scramble_game():
    """Run the Word Scramble Game."""
    print("Welcome to the Word Scramble Game!")
    engine.say("Welcome to the Word Scramble Game!")
    engine.runAndWait()
    print("Try to unscramble the letters to form a correct word.")
    engine.say("Try to unscramble the letters to form a correct word.")
    engine.runAndWait()
    while True:
        # Choose a word and scramble it
        target_word = random.choice(word_list)
        print(target_word)
        scrambled_letters = random.sample(target_word, len(target_word))
        scrambled_word = ''.join(scrambled_letters)

        print(f"\nScrambled word: {scrambled_word}")

        # Ask for user input
        guess = input("Enter your guess (or type 'quit' to exit): ").lower()

        # Check if the user wants to quit
        if guess == 'quit':
            print("Thanks for playing!")
            break

        # Check if the guess is correct
        if guess == target_word:
            print("Congratulations! You guessed the correct word!")
            engine.say("right")
            engine.runAndWait()
            
        else:
            print(f"Sorry, that's incorrect. The correct word is: {target_word}")
            engine.say(f"wrong.. the correct one is {target_word}")
            engine.runAndWait()


def memory_game():
    """Run the Memory Game."""
    
    print("Welcome to the Memory Game!")

    engine.say("Welcome to the Memory Game!")
    engine.runAndWait()

    print("A sequence of colors will be say, and you need to repeat it back.")

    engine.say("A sequence of colors will be displayed, and you need to repeat it back.")
    engine.runAndWait()

    sequence_length = 1
    while True:
        # Generate a random sequence
        sequence = [random.choice(color_list) for _ in range(sequence_length)]

        # Display the sequence to the user
        print(f"Round {sequence_length}:")
        for color in sequence:
            engine.say(color)
            engine.runAndWait()
            time.sleep(1)  # Pause for 1 second between colors
        print()  # Move to the next line after displaying the sequence

        # Get the user's input for the repeated sequence
        print("Repeat the sequence by typing the colors separated by spaces:")
        user_input = input().strip().split()

        # Check if the user's input matches the sequence
        if sequence == user_input:
            print("Congratulations! You repeated the sequence correctly.")
            engine.say('Right')
            engine.runAndWait()
            # Increase sequence length for the next round (up to 10)
            sequence_length = min(sequence_length + 1, 10)

        else:
            print("Sorry, your sequence did not match. Game Over.")
            engine.say("Sorry, your sequence did not match. Game Over.")
            engine.runAndWait()
            break

def get_recommendations(text_en):
    
    """Get recommended educational content based on user interests."""
 
    # Setup user profile
    interests = text_en.split("of ")[1]
    
    recommendations = []
    for interest in interests:
        if interest in educational_content:
            recommendations.extend(educational_content[interest])

    # Display recommended content to the user
    if recommendations:
        for idx, content in enumerate(recommendations, start=1):
            print(f"{idx}. {content}")
    else:
        print("No recommendations available for your interests.")


def DrawingApp():
    def on_button_press(event):
        app.start_x = event.x
        app.start_y = event.y

    def on_move_press(event):
        x, y = event.x, event.y
        if app.start_x and app.start_y:
            app.canvas.create_line(app.start_x, app.start_y, x, y, fill=app.draw_color, width=2)
            app.draw.line([app.start_x, app.start_y, x, y], fill=app.draw_color, width=2)
        app.start_x = x
        app.start_y = y

    def on_button_release(event):
        app.start_x = None
        app.start_y = None

    def choose_color():
        color = colorchooser.askcolor()[1]
        if color:
            app.draw_color = color

    def clear_canvas():
        app.canvas.delete("all")
        app.draw.rectangle((0, 0, app.canvas.winfo_width(), app.canvas.winfo_height()), fill="white")

    def save_as_png():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            image = app.image.crop((0, 0, app.canvas.winfo_width(), app.canvas.winfo_height()))
            image.save(file_path, "png")

    root = tk.Tk()
    root.title("Drawing App")

    app = tk.Frame(root)
    app.canvas = tk.Canvas(app, width=600, height=400, bg="white")
    app.canvas.pack()

    app.image = Image.new("RGB", (600, 400), "white")
    app.draw = ImageDraw.Draw(app.image)

    app.start_x = None
    app.start_y = None
    app.draw_color = "black"

    app.canvas.bind("<Button-1>", on_button_press)
    app.canvas.bind("<B1-Motion>", on_move_press)
    app.canvas.bind("<ButtonRelease-1>", on_button_release)

    toolbar = tk.Frame(root)
    toolbar.pack(pady=5)

    color_button = tk.Button(toolbar, text="Color", command=choose_color)
    color_button.pack(side=tk.LEFT)

    clear_button = tk.Button(toolbar, text="Clear", command=clear_canvas)
    clear_button.pack(side=tk.LEFT)

    save_button = tk.Button(toolbar, text="Save", command=save_as_png)
    save_button.pack(side=tk.LEFT)

    app.pack()
    root.mainloop()


def Emotion_detection():
    while True:    
        print('speak')
        engine.say("speak a sentance : ")
        engine.runAndWait()
        
        text_en = voice_into_text()
        
        
        
        blob = TextBlob(text_en)
        sentiment = blob.sentiment.polarity

        # Respond based on emotion
        if sentiment > 0.5:
            response = "positive emotion"
        elif sentiment < -0.5:
            response = "negative emotion"
        
            
        elif 'stop' in text_en:
            print("exiting")
            engine.say('exiting the emotion detecter!!')
            engine.runAndWait()
            break
        
        else:
            response = "This is not an emotion"

        # Speak the response
        engine.say(response)
        engine.runAndWait()
        


def Background_noise():
    input_filepath = input("Enter the file path to remove background noise: ")
    # Load the audio file
    audio_data, sample_rate = sf.read(input_filepath)

    # Select a portion of the audio file for noise estimation (optional)
    noise_data = audio_data[:sample_rate * 5]  # Use the first 5 seconds for noise estimation

    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=audio_data, sr=sample_rate, stationary=True)

    # Specify the output directory path
    output_dir = "C:\\Users\\ABC\\Desktop\\Mini Projects\\SpeakSmart\\Audio_BackGround_removers"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(input_filepath))[0]

    # Specify the output file path
    output_filepath = os.path.join(output_dir, f"{file_name}_BackGround_remov.wav")

    # Save the denoised audio to the specified output path
    sf.write(output_filepath, reduced_noise, sample_rate)

    print("Denoised audio saved successfully at:", output_filepath)


def run_mart():
    # Define the path to mart.py

    try:
        # Run mart.py using subprocess
        subprocess.run(['python', mart_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running mart.py: {e}")
        
        
def get_weather_forecast(user_input):
    
    # Prompt the user for location input
    
    city = user_input.split("of")[-1].strip()


    # Display the weather forecast

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={get_weather_Api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        forecast = f"Weather forecast for {city}:\n"
        forecast += f"Description: {weather_description}\n"
        forecast += f"Temperature: {temperature}°C\n"
        forecast += f"Humidity: {humidity}%\n"
        forecast += f"Wind Speed: {wind_speed} meters per second \n"
        print(forecast)
        engine.say(forecast)
        engine.runAndWait()
    else:
        return "Failed to fetch weather forecast."
    
    
    


def fetch_full_content(topic):
    topic = topic.split("about ")[-1]
    
    topic = topic.replace(' ', '_')
    # Wikipedia URL for the given topic
    url = f"https://en.wikipedia.org/wiki/{topic}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser') 

        # Find the main content of the page
        content = soup.find(id='mw-content-text')

        # Find all paragraphs in the content
        paragraphs = content.find_all('p')

        # Concatenate all paragraphs into a single string
        full_content = ''
        for paragraph in paragraphs[:2]:
            full_content += paragraph.text + '\n'

        # Write the full content to a text file
        write_to_notepad(topic, full_content)
    else:
        print("Failed to retrieve full content from Wikipedia.")
        
        

def get_recipe_suggestions(ingredients_input):
    
    ingredients_input = ingredients_input.split("using ")[1].strip().split(',')
    
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    
    params = {
        'apiKey': spoonacular_api_key,
        'ingredients': ','.join(ingredients_input),
        'number': 5,
        'ranking': 1
    }
    
    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            recipes = response.json()
            if recipes:
                print("\nHere are some recipe suggestions based on your ingredients:\n")
                print(f"the example Recipes using {ingredients_input} are")
                engine.say(f"the example Recipes using {ingredients_input} are")
                engine.runAndWait()
                for recipe in recipes:
                    print(recipe['title'])
                    engine.say(recipe['title'])
                    engine.runAndWait()
                print()
            else:
                print("No recipes found. Please try again.")
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)



def personal_notes_manager():
    class PersonalNotes:
        def __init__(self, file_path):
            self.notes = {}
            self.file_path = file_path

            # Load notes from file if it exists
            try:
                with open(self.file_path, "r") as file:
                    self.notes = json.load(file)
            except FileNotFoundError:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        def create_note(self, title, content):
            self.notes[title] = content
            self.save_notes()

        def retrieve_note(self, title):
            return self.notes.get(title, "Note not found.")

        def display_notes(self):
            if self.notes:
                print("Your notes:")
                for i, (title, content) in enumerate(self.notes.items(), 1):
                    print(f"note {i} - {title}")
            else:
                print("You have no notes yet.")

        def save_notes(self):
            with open(self.file_path, "w") as file:
                json.dump(self.notes, file)

    notes_file_path = r"C:\Users\ABC\Desktop\Mini Projects\SpeakSmart\Notes\notes.json"
    notes_manager = PersonalNotes(notes_file_path)

    while True:
        print("\nWhat would you like to do?")
        print("1. Create a note")
        print("2. Retrieve a note")
        print("3. Display all notes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the note: ")
            content = input("Enter the content of the note: ")
            notes_manager.create_note(title, content)
            print("Note created successfully.")

        elif choice == "2":
            title = input("Enter the title of the note you want to retrieve: ")
            note = notes_manager.retrieve_note(title)
            print(note)

        elif choice == "3":
            notes_manager.display_notes()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")
            
            
            
from datetime import datetime
def get_current_time_in_country(country):
    try:
        if country in cities:
            timezone = cities[country]
            current_time = datetime.now(pytz.timezone(timezone)).strftime('%H:%M')
            print(f"The current time in {country} ({list(cities.keys())[list(cities.values()).index(timezone)]}) is {current_time}.")
            engine.say(f"The current time in {country} ({[list(cities.values()).index(timezone)]}) is {current_time}.")
            engine.runAndWait()
        else:
            print("Country not found in the list.")
    except Exception as e:
        print(f"An error occurred: {e}")
    