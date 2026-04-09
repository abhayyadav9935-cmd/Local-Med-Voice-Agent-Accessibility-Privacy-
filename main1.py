import pyttsx3
import os

def read_medical_file(file_path):
    if not os.path.exists(file_path):
        print(f"[Error] File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        report_text = file.read()

    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)

    print("\n[Privacy Mode ON] Reading Medical Data Locally...")
    print("-" * 50)
    print(report_text)
    print("-" * 50)

    engine.say(report_text)
    engine.runAndWait()
    print("\n[Done] Report reading complete. 100% Offline.")

if __name__ == "__main__":
    dummy_file = "sample_report.txt"
    with open(dummy_file, "w") as f:
        f.write("Patient Name: Abhay. Condition: Stable. VPMP Shunt is functioning normally.")
    read_medical_file(dummy_file)
