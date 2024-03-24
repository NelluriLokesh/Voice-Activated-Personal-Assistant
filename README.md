# Voice-Activated-Personal-Assistant
Python Voice Assistant for Seamless Task Automation


**Voice Assistant with Audio Transcription and Automation**

This Python project implements a voice-controlled assistant capable of transcribing speech into text, performing various tasks based on the transcribed commands, and utilizing different technologies and libraries for its functionalities.

This Python project is a comprehensive voice-controlled assistant designed to enhance user productivity and accessibility through speech interaction. Leveraging a combination of advanced libraries and technologies, the assistant empowers users to perform a variety of tasks seamlessly using voice commands.

**Technologies and Libraries Used:**

1. **PyAudio:** PyAudio is a Python library that provides bindings for PortAudio, a cross-platform audio I/O library. It is used for audio input and output handling, including recording and playback.

2. **SpeechRecognition:** SpeechRecognition is a library that provides easy-to-use APIs for performing speech recognition in Python. It enables the assistant to transcribe speech to text, facilitating seamless interaction between the user and the assistant.

3. **pyttsx3:** pyttsx3 is a text-to-speech conversion library in Python. It is utilized for converting text into audible speech, allowing the assistant to communicate audibly with the user.

4. **webbrowser:** The webbrowser module provides a high-level interface to allow displaying web-based documents to users. It is used for opening web browser windows, facilitating web searches or accessing specific websites based on user commands.

5. **subprocess:** The subprocess module enables the creation of new processes, allowing Python scripts to run system commands and interact with the system shell. It is employed for executing system commands and opening applications as per user requests.

6. **os:** The os module in Python provides a way of interacting with the operating system. It is used for various system-level tasks, including file operations, environment variables, and process management.

7. **time:** The time module provides various time-related functions in Python. It is employed for tasks such as setting timers, handling delays, and displaying timestamps.

8. **psutil:** psutil is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors). It is utilized in the assistant for managing running processes, such as checking if a specific application is already running.

9. **wave:** The wave module provides a convenient interface to work with WAV audio files in Python. It facilitates audio recording and playback operations, allowing the assistant to record audio inputs from the user.

10. **keyboard:** The keyboard module enables detection of keyboard events in Python. It is utilized for detecting key presses, allowing functionalities such as stopping audio recording or timers based on user input.

11. **pygame:** pygame is a cross-platform set of Python modules designed for writing video games. In this project, it is used for audio playback, enabling the assistant to play alarm sounds when needed.

12. **datetime:** The datetime module provides classes for manipulating dates and times in Python. It is employed for tasks such as setting alarms, displaying current time, and calculating time differences.

13. **re:** The re module in Python provides support for regular expressions. It is utilized for text processing and pattern matching, enabling the assistant to extract relevant information from transcribed text.

14. **random:** The random module provides functions for generating random numbers in Python. It is used for generating random passwords with embedded names based on user input.

15. **Voice-Controlled Assistant** This project implements a voice-controlled assistant in Python, capable of transcribing speech into text and performing various tasks based on user commands. It utilizes several libraries and technologies for audio processing, speech recognition, automation, and integration with mapping services.

**And Many More** in my project


   

**Functionality Overview:**

1. **Voice Input and Output Handling:**
   - PyAudio is used to capture voice input through the microphone and playback audio responses.
   - Text-to-speech conversion is achieved using pyttsx3, allowing the assistant to communicate with the user audibly.

2. **Speech Recognition and Transcription:**
   - The SpeechRecognition library is utilized for transcribing spoken commands into text.
   - The assistant recognizes user commands and performs corresponding actions based on the transcribed text.

3. **Automation and Task Execution:**
   - The assistant can open web browsers, perform web searches, open applications, and manage running processes using subprocess and webbrowser libraries.
   - It can execute system commands, such as setting alarms, recording audio, setting timers, and solving math problems.

4. **Additional Functionalities:**
   - The assistant provides features such as setting alarms with customizable times, recording audio with specified durations, and generating random passwords.

**Usage:**
- Run the Python script and allow microphone access for voice input.
- Speak commands clearly, and the assistant will transcribe them into text and execute corresponding actions.
- Use predefined commands to interact with the assistant, such as opening applications, setting alarms, or performing web searches.
- Explore the code to understand the implementation details and customize functionalities as needed.

**Note:**
- Ensure all required libraries are installed using pip (`pip install <library>`).
- Modify file paths and configurations according to your system setup.
- This README provides an overview of the project; refer to the code comments for detailed explanations of each functionality and implementation step.


