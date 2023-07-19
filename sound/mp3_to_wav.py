from pydub import AudioSegment
from scipy.io import wavfile

# MP3 파일 로드
mp3_path = '아라_쏠.mp3'
audio = AudioSegment.from_mp3(mp3_path)

# WAV 파일로 변환 후 저장
wav_path = '아라_쏠.wav'
audio.export(wav_path, format="wav")