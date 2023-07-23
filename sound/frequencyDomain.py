import librosa
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from scipy.spatial.distance import cosine


def compare_audio_frequency_domain(audio_file1, audio_file2):
    # 오디오 파일 로드
    y1, sr1 = librosa.load(audio_file1, sr=16000)  # 16000 이 인간 목소리에 적합하다고 함
    y2, sr2 = librosa.load(audio_file2, sr=16000)

    # 두 오디오 파일의 길이를 맞춰줍니다. -> 오류 발생 방지
    min_length = min(len(y1), len(y2))
    y1 = y1[:min_length]
    y2 = y2[:min_length]

    # MP3 파일을 읽어서 MFCC 특성 추출
    def extract_mfcc(y, sr):
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        return mfcc

    # MFCC 특성 추출
    mfcc1 = extract_mfcc(y1, sr1)
    mfcc2 = extract_mfcc(y2, sr2)

    scaler = MinMaxScaler()
    mfcc1_normalized = scaler.fit_transform(mfcc1.T).T
    mfcc2_normalized = scaler.transform(mfcc2.T).T
    mfcc1_flattened = mfcc1_normalized.flatten()
    mfcc2_flattened = mfcc2_normalized.flatten()

    # MSE를 사용하여 주파수 도메인 유사도 측정
    # mse = np.mean((mfcc1_flattened - mfcc2_flattened)**2)
    mae = mae = np.mean(np.abs(mfcc1_flattened - mfcc2_flattened))
    cosine_similarity = 1 - cosine(mfcc1_flattened, mfcc2_flattened)
    return mae, cosine_similarity


# mae, cosine_similarity = compare_audio_frequnecy_domain("./nar/신우_속도1up.mp3", "./nar/신우_속도1down.mp3")
# print(f"mae: {mae}\ncosine_similarity: {cosine_similarity}")
