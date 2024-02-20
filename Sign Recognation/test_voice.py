import sounddevice as sd
import soundfile as sf

def play_audio(file_path):
    try:
        # Load the audio file
        data, fs = sf.read(file_path, dtype='float32')
        
        # Play the audio
        sd.play(data, fs)
        
        # Wait until playback is finished
        status = sd.wait()
        if status:
            print("An error occurred during playback.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    audio_file = "speed20.wav"  # Change this to your audio file path
    play_audio(audio_file)
