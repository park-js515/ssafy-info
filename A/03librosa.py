import librosa
import numpy as np

# 음성 파일 로딩
audio_path1 = './sample-1-1.wav'
audio_path2 = './sample-1-2.wav'
audio1, sr1 = librosa.load(audio_path1, sr=None)
audio2, sr2 = librosa.load(audio_path2, sr=None)

# 특징 추출
features1 = librosa.feature.mfcc(y=audio1, sr=sr1)
features2 = librosa.feature.mfcc(y=audio2, sr=sr2)

# 델타 특성 계산
delta1 = librosa.feature.delta(features1)
delta2 = librosa.feature.delta(features2)

# 정규화
delta1_norm = (delta1 - np.min(delta1)) / (np.max(delta1) - np.min(delta1))
delta2_norm = (delta2 - np.min(delta2)) / (np.max(delta2) - np.min(delta2))

# 유사도 비교
similarity = np.abs(delta1_norm - delta2_norm)
similarity = np.sum(similarity)

print(f"Similarity: {similarity}")
