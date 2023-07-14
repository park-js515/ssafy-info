import librosa

y, sr = librosa.load('./녹음.wav')

similarity = librosa.segment.cross_similarity(y, sr)
print(similarity)