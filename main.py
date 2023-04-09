import wave
import pyaudio


input_file = "input_file.mp3"
output_file = "output_file.wav"

with pyaudio.PyAudio() as py_audio:
    with py_audio.open(input_file, format=py_audio.get_format_from_width(2), channels=2, rate=44100) as stream:
        data = stream.read()

with wave.open(output_file, "wb") as wav_audio:
    wav_audio.setnchannels(2)
    wav_audio.setsampwidth(2)
    wav_audio.setframerate(44100)
    wav_audio.writeframes(data)
