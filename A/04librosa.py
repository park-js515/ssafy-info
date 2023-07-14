import librosa
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

# 첫 번째 음성 파일 로드 및 MFCC 추출
audio1, sr1 = librosa.load('sample-1-1.wav') # 오디오 데이터(ndarray), 샘플링 속도(seconds)
mfcc1 = librosa.feature.mfcc(y=audio1, sr=sr1)
# ex. mfcc1.shape = (20, 44) => 20개의 프레임, 44개의 특성

# 두 번째 음성 파일 로드 및 MFCC 추출
audio2, sr2 = librosa.load('sample-1-2.wav')
mfcc2 = librosa.feature.mfcc(y=audio2, sr=sr2)

# RMS 계산
rms1 = librosa.feature.rms(y=audio1)
rms2 = librosa.feature.rms(y=audio2)

# MFCC 비교 (Mel-frequency Cepstral Coefficients)
mfcc_similarity = 1 - cdist(mfcc1.T, mfcc2.T, metric='cosine')

# RMS 비교 (Root Mean Square)
rms_similarity = np.mean(rms1) - np.mean(rms2)

# print(mfcc1.shape)
print("MFCC Similarity:", mfcc_similarity)
print("RMS Similarity:", rms_similarity)


# plt.figure()
# librosa.display.waveshow(y=audio1, sr=sr1, label='1', alpha=0.5)
# librosa.display.waveshow(y=audio2, sr=sr2, label='2', alpha=0.5)
# plt.legend()
# plt.show()