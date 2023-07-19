import librosa
from sklearn.metrics import mean_squared_error

# MP3 파일을 읽어서 MFCC 특성 추출
def extract_mfcc(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return mfcc

# MSE를 사용하여 두 음성 데이터 간의 주파수 도메인 유사도 측정
def compute_mse(mfcc1, mfcc2):
    return mean_squared_error(mfcc1, mfcc2)

# 두 개의 MP3 파일 비교
file1 = '다인_쏠.mp3'
file2 = '다인_쏠.mp3'

# MFCC 특성 추출
mfcc1 = extract_mfcc(file1)
mfcc2 = extract_mfcc(file2)

# MSE를 사용하여 주파수 도메인 유사도 측정
mse = compute_mse(mfcc1, mfcc2)

print("두 음성 데이터 간의 주파수 도메인 유사도(MSE):", mse)
