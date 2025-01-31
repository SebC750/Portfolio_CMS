import pyttsx3

def main():
    engine = pyttsx3.init()
    engine.say("I will speak this text")
    engine.runAndWait()
    print("Hello world.")
    
if __name__ == "__main__":
    main()