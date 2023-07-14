import numpy as np
from sklearn.preprocessing import normalize
from scipy.io import wavfile

# 두 개의 .wav 파일 로드
rate1, data1 = wavfile.read("녹음.wav")
rate2, data2 = wavfile.read("녹음.wav")

# 샘플 값들의 차이 계산
data1 = data1.reshape(-1, 1)
data2 = data2.reshape(-1, 1)
data1Norm = normalize(data1, axis=0).ravel()
data2Norm = normalize(data2, axis=0).ravel()

diff = data1Norm - data2Norm

# # RMSD 계산
normalized_rmsd = np.sqrt(np.mean(diff**2))
print("Normalized RMSD:", normalized_rmsd)