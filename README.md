# Mock Interview Bot
# Mock Interview Bot

Welcome to **Mock Interview Bot**! 
🎤🤖 This project is designed to help you practice for interviews in a fun and interactive way. 
It simulates a mock interview environment by asking you random questions from a dataset, recording your responses (both video and audio), and providing feedback on your answers.

---

## Features
- 🎙️ **Audio and Video Recording**: Records your video and audio responses during the mock interview.
- 💬 **Interactive Questioning**: Asks questions randomly selected from a predefined dataset.
- 🔑 **Keyword Matching**: Evaluates your answers by matching keywords to measure accuracy.
- 📊 **Visual Feedback**: Generates bar and pie charts to display performance metrics.
- 🖼️ **User-Friendly GUI**: Built with Tkinter for an intuitive and interactive interface.

---
---

## How It Works
1. The bot selects random questions from the dataset (`Interview Question Dataset - Sheet1.csv`).
2. You answer the question while the bot records your audio and video.
3. The bot processes your audio response, compares it to expected keywords, and provides feedback on your answer.
4. At the end of the session, the bot displays graphs showing your performance:
   - **Bar Chart**: Keywords matched for each question.
   - **Pie Chart**: Overall performance distribution.

---
---

## Requirements
Ensure you have the following installed on your system:
- Python 3.7 or later
- `pip` (Python package installer)

Required Python packages:
- `pyttsx3`
- `speech_recognition`
- `tkinter` (built-in with Python)
- `random` (built-in with Python)
- `matplotlib`
- `csv` (built-in with Python)
- `threading` (built-in with Python)
- `sounddevice`
- `soundfile`
- `opencv-python`
- `requests`

---

## Setup
1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/mock-interview-bot.git
   cd mock-interview-bot
   ```
2. **Install the required packages:**
   ```bash
   pip install pyttsx3 speechrecognition matplotlib sounddevice soundfile opencv-python requests
   ```

3. **Run the program:**
   ```bash
   python Interview\ Bot.py
   ```

   ---

## Usage
1. Run the `Interview Bot.py` script:
   ```bash
   python Interview\ Bot.py
   ```
2. Click the **Ready** button to start your mock interview session.
3. Answer the questions displayed on the screen.
4. After completing all questions, click **Result** to view your performance graphs.

---

## Future Enhancements
- 🌐 **Multilingual Support**: Add support for questions and answers in multiple languages.
- 🔄 **Dynamic Dataset**: Allow users to upload their custom question datasets.
- 📋 **Detailed Feedback**: Provide suggestions on how to improve answers.
- 📱 **Mobile App**: Create a mobile-friendly version for greater accessibility.

---

We hope you enjoy using the Mock Interview Bot! 💻✨ Feel free to contribute or suggest improvements.

**Happy Practicing!** 🚀
