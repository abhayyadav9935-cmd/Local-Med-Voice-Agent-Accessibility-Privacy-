# Local Med-Voice Agent 🏥

> **100% Offline. Zero Data Leaks. Built for Real Patients.**

---

##  The Problem

Visually impaired patients and elderly individuals **cannot read** complex medical reports.  
Existing solutions (Google Assistant, cloud AI) **upload your private medical data** to remote servers — a serious privacy violation.

---

##  The Solution

A completely **offline** Python tool that uses your computer's own Text-to-Speech engine to **read medical documents aloud** — no internet, no cloud, no data leaks.

Your medical data **never leaves your device.**

---

##  Features

- **100% Offline** — works without internet
-  **Privacy-First** — no data sent to any server
-  **Clear Speech** — slow reading speed for easy understanding
-  **Accessibility** — designed for visually impaired users
-  **Medical Use Case** — reads MRI reports, prescriptions, appointments
-  **Lightweight** — runs on low-end devices (even old laptops)

---

##  Installation

**Step 1: Install Python**  
Download from: https://python.org

**Step 2: Install dependency**
```bash
pip install pyttsx3
```

**Step 3: Run the tool**
```bash
python main.py
```

---

##  How to Use

Open `main.py` and replace the sample text with your actual medical report:

```python
sample_medical_report = "Your report text goes here..."
```

Then run:
```bash
python main.py
```

The tool will read it aloud on your speakers or headphones.

---

##  Project Structure

```
local-med-voice-agent/
│
├── main.py              # Main script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

##  Future Scope

- [ ] Add OCR (scan physical reports with camera)
- [ ] Support Hindi & regional Indian languages
- [ ] GUI interface for elderly users
- [ ] Integration with local LLM for report summarization
- [ ] Mobile version (Android offline TTS)

---

## 👤 Author

**Abhay Yadav**  
GitHub: abhayyadav9935-cmd

---

## License

MIT License — Free to use, modify, and distribute.
