# Text-to-Speech (TTS) Project

This project converts text input into speech using Python. It leverages libraries like `gTTS`, `pyttsx3`, and `pygame` for text-to-speech conversion and audio playback.

## Features
- Converts any input text to speech.
- Saves the generated audio to a file.
- Supports audio playback within the program.

---

## Prerequisites
- Python 3.8 to 3.11 (Python 3.12+ is not supported by some dependencies).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment
A virtual environment helps isolate your project's dependencies from your system-wide Python packages.

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements
Install the dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run the Project
After installing the requirements, run the script:
```bash
python TTS.py
```

---

## Project Files
- **`TTS.py`**: The main script for text-to-speech conversion.
- **`requirements.txt`**: Lists all project dependencies.
- **`README.md`**: Documentation for the project.

---

## How It Works
1. The script prompts the user to input text.
2. It converts the text to speech using the supported library (`gTTS`).
3. The generated speech is saved as an audio file (e.g., `output.mp3`).
4. The script plays the audio file using `playsound`.

---

## Dependencies
- **gTTS**: Converts text to speech using Google Text-to-Speech API.
- **playsound**: Plays sound files.

These dependencies are listed in the `requirements.txt` file for easy installation.

---

## Example Usage
1. Run the script:
    ```bash
    python TTS.py
    ```
2. Enter the text you want to convert to speech when prompted.
3. The audio file will be saved and played back.

---

## Notes
- Ensure your Python version is compatible with the listed dependencies.
- If you encounter any issues during installation, refer to the documentation or contact the project maintainer.

---

## Contributing
Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

---

## License
This project is licensed under the MIT License.
