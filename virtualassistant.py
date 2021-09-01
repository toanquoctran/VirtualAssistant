import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic, timeout = 3, phrase_time_limit = 3)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Toan Tran"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "wife" in you:
        robot_brain = ""
    elif "parents" in you:
        robot_brain = ""
    elif "brothers" in you:
        robot_brain = ""
    elif "do I love her" in you:
        robot_brain = "Yes you love her very much, and she loves you back"
    elif "from" in you:
        robot_brain = ""
    elif "bye" in you:
        robot_brain = "Bye Toan Tran"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm good. How are you?"

    print("Robot: " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()