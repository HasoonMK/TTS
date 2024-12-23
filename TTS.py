from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text, lang="en", output_file="output.mp3"):
    """
    Converts text to speech and saves it as an audio file.

    Args:
        text (str): Text to convert to speech.
        lang (str): Language code (e.g., "en" for English, "es" for Spanish).
        output_file (str): Output audio file name.

    Returns:
        None
    """
    try:
        # Generate speech
        print("Converting text to speech...")
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save to file
        tts.save(output_file)
        print(f"Audio saved as '{output_file}'")

        # Play the audio
        playsound(output_file)
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Input text
    text = input("Enter the text to convert to speech: ")

    # Perform text-to-speech conversion
    text_to_speech(text)

if __name__ == "__main__":
    main()
