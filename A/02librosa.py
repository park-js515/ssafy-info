import librosa
# from sklearn.metrics.pairwise import cosine_distances
import matplotlib.pyplot as plt

# 두 개의 음원 파일 로드
audio1, sr1 = librosa.load('sample-1-1.wav')
audio2, sr2 = librosa.load('녹음.wav')

# plt.figure(figsize=(14, 5))
plt.figure()
librosa.display.waveshow(y=audio1, sr=sr1, label='1', alpha=0.5)
librosa.display.waveshow(y=audio2, sr=sr2, label='2', alpha=0.5)
plt.legend()
plt.show()

