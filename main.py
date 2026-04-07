import pyttsx3

def speak_text(text):
    """Offline Text-to-Speech for visually impaired users."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 140) # Slow speed for clear hearing
    print("\n[Privacy Mode ON] Reading Medical Data Locally...")
    print(f"Text: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    sample_medical_report = "Your MRI scan is clear. The VPMP shunt pressure is stable. Please remember to take your Vata-balancing medication."
    speak_text(sample_report)
