from pydub import AudioSegment
from io import BytesIO
import speech_recognition as sr

def transpose_audio_for_text(audio_file):
    recognizer = sr.Recognizer()
    
    try:
        audio_segment = AudioSegment.from_file(audio_file, format="wav")
        wav_audio = BytesIO()
        audio_segment.export(wav_audio, format="wav")
        wav_audio.seek(0)

        with sr.AudioFile(wav_audio) as source:
            audio_data = recognizer.record(source)
    
        transcription = recognizer.recognize_google(audio_data, language="pt-BR")
        return transcription
    
    except sr.UnknownValueError:
        return 'Não foi possível entender o áudio.'
    except sr.RequestError as e:
        return f'Erro no serviço de reconhecimento de voz: {e}'
        
