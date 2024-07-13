

import pyaudio
import speech_recognition as sr
import pyttsx3
import webbrowser

from utilities import *


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



engine.say("....Hi Lokesh?? how can I help you today?")
engine.runAndWait()
print("Start recording...")




while True:
    # Record voice
    seconds = 3
    frames = []

    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    # Stop and close PyAudio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert raw audio data to AudioData
    audio_data = b"".join(frames)
    audio_data_instance = sr.AudioData(audio_data, sample_rate=RATE, sample_width=2)

    # Initialize SpeechRecognition recognizer
    recognizer = sr.Recognizer()

    try:
        # Transcribe in English
        text_en = recognizer.recognize_google(audio_data_instance, language="en-US")
        print("Transcribed text (English):", text_en)

        if "ok done" == text_en.lower():
            engine.say("Thank you... You can call me any time")
            engine.say("Exiting the assistant.")
            engine.runAndWait()
            break

        elif "open Google" in text_en:
            engine.say("Opening Google")
            engine.runAndWait()
            webbrowser.open("https://www.google.com")

        elif "search" in text_en:
            query = text_en.split("search")[-1].strip()
            engine.say(f"Searching for {query}")
            engine.runAndWait()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "quit" == text_en.lower():
            
            engine.say("Quitting the assistant")
            engine.runAndWait()
            break


        elif ("open" or "app") in text_en and "WhatsApp" not in text_en:  # If "open" is in the command
            app_name = text_en.split("open", 1)[-1].split("app", 1)[0].strip()  # Get the application name
            if "mail" in text_en:
                
                open_application_by_name(Mail_app_path)
            else:
                
                open_application_by_name(app_name)
                
        
        elif 'WhatsApp' and ('open' or 'app') in text_en:
              
            open_application_by_name(What_app_path)
            
            
        elif 'close' in text_en:    
            
            app_name = text_en.split("close", 1)[-1]
            if 'notepad' in text_en:
                app_name = 'notepad.exe'
                close_application_by_name(app_name)
            else:
                close_application_by_name(app_name) 
        
        
        elif "solve problems" == text_en:
            
            record_audio_transcribe_and_execute()
            print("Done")
            
            
        elif 'translator' == text_en:
            
            record_audio_transcribe_and_speak()
            print("Done")
            
        elif "what is the time" == text_en:
            from datetime import datetime

            # Get current date and time
            def current_time():
                current_time = datetime.now()

                # Convert time to string format
                time_str = current_time.strftime("%I:%M %p")  # %I for 12-hour format, %p for AM/PM

                # Print the time
                print(f"Current time is: {time_str}")
                
                engine.say(f"Current time is: {time_str}")
                engine.runAndWait()
            current_time()
            print("Done")
        
        elif "record" == text_en:
            
          filename = record_audio()
          
           
          print("Done")
          
        elif "play the recording" in text_en:
            
            play_audio()
            print("Done")
          
        elif 'location' in text_en:
            
            display_route_on_map(text_en)
            print("Done")
            
        elif "show the map" == text_en:
            
            Show_the_map()
            print("Done")
        
            
          
        elif "set alarm" in text_en:
            
            alarm_and_transcribe(text_en)
            print("Done")

        elif 'start timer' in text_en:
            
            timers(text_en)
            print("Done")
            
        elif 'random password' in text_en:
            
            random_password(text_en)
            print("Done")
                
        
                
        elif "change" in text_en:
            
            Currancy(text_en)
            print("Done")
            
        elif "tell" and "me" and 'a' and 'joke' in text_en:
            
            get_random_joke()
            print("Done")
            
        elif "random fact" in text_en:
            
            get_random_fact()
            print("Done")
                    
        elif "definition" in text_en:
            
            get_word_definition(text_en)
            print("Done")
            
        elif "next holiday" in text_en:
            
            next_holiday()
            print("Done")
            
        elif "quick" and 'summary' in text_en:
            
            News_Summaries(text_en)
            print("Done")
            
            
        ##                                                      games
        
        elif "random game" in text_en:

            game_selector = random.choice([word_association_game, guess_and_play_sound,rock_paper_scissor,word_scramble_game])
            
            game_selector()
            
            print("Done")
        
        elif "scramble game" in text_en:

            word_scramble_game()
            print("Done")
            
        elif "word association game" in text_en:
            
            word_association_game()
            print("Done")
        
        elif "guess and play sound" in text_en:
            
            guess_and_play_sound()
            print("Done")
        
        elif "rock paper scissor" in text_en:
            
            rock_paper_scissor()
            print("Done")
            

        elif "memory game" in text_en:

            memory_game()
            print("Done")
        
            
        
        elif "Drawing app" == text_en:
            
            DrawingApp()
            print('Done')  
            
        
        
        elif "tone analysis" in text_en:
            
            Emotion_detection()
            print("Done")    
        
            
        elif "Loki Mart" in text_en:
            print("Welcome to Loki Mart, where your shopping experience begins!")
            engine.say("Welcome to Loki Mart, where your shopping experience begins!")
            engine.runAndWait()
            run_mart()
            print("Done")
        
        elif "weather report" in text_en : 
            get_weather_forecast(text_en)              # example : weather report of "kakinada"
            print("Done")
        
        elif "remove background noise" in text_en:
            
            Background_noise()
            print("Done")
        
        elif "short note about" in text_en:
            
            fetch_full_content(text_en)                 # exampler : short note about "india" 
            print("Done")
        
        elif "recipes" in text_en:                                                     
                                                            # example : "Recipes using "fish""
            get_recipe_suggestions(text_en)
            
            print("Done")
            
        elif "road map of" in text_en:
                                                        # example : road map of "data science"
            get_recommendations(text_en)
            
        elif "personal notes" in text_en:
            
            personal_notes_manager()
            print()

        elif "what is the current time of" in text_en:
            
            user_input = text_en.split("of ")[1]                # example : what is the current time of"
            user_input = user_input.capitalize()
            get_current_time_in_country(user_input)
            
            
        elif text_en:
            
            print("you said : ", text_en)
            
            engine.say(f"you said {text_en}")
            engine.runAndWait()
            print("Done")
            
        


    except sr.UnknownValueError:
        
        print("Im Waiting......")

    # Re-initialize PyAudio stream for next recording
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=FRAMES_PER_BUFFER)
 