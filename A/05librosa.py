import librosa
import numpy as np
from scipy.spatial.distance import cdist

# 첫 번째 음성 파일 로드 및 MFCC 추출
audio1, sr1 = librosa.load('sample-1-1.wav')
mfcc1 = librosa.feature.mfcc(y=audio1, sr=sr1)

# 두 번째 음성 파일 로드 및 MFCC 추출
audio2, sr2 = librosa.load('sample-1-2.wav')
mfcc2 = librosa.feature.mfcc(y=audio2, sr=sr2)

# MFCC 비교 (Mel-frequency Cepstral Coefficients)
mfcc_similarity = 1 - cdist(mfcc1.T, mfcc2.T, metric='cosine')

# 대각 요소 밑의 값들로 유사도 통계량 계산
statistics = {
    'mean': np.mean(mfcc_similarity[np.triu_indices_from(mfcc_similarity, k=1)]),
    'min': np.min(mfcc_similarity[np.triu_indices_from(mfcc_similarity, k=1)]),
    'max': np.max(mfcc_similarity[np.triu_indices_from(mfcc_similarity, k=1)]),
    'median': np.median(mfcc_similarity[np.triu_indices_from(mfcc_similarity, k=1)]),
}

print("MFCC Similarity Statistics:")
for stat, value in statistics.items():
    print(f"{stat}: {value}")
