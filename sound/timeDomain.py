import librosa
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cosine


def compare_audio_time_domain(audio_file1, audio_file2):
    # 오디오 파일 로드
    y1, sr1 = librosa.load(audio_file1, sr=16000)  # 16000 이 인간 목소리에 적합하다고 함
    y2, sr2 = librosa.load(audio_file2, sr=16000)

    # 두 오디오 파일의 길이를 맞춰줍니다. -> 오류 발생 방지
    min_length = min(len(y1), len(y2))
    y1 = y1[:min_length]
    y2 = y2[:min_length]

    # 스케일링을 위해 2D 배열로 변환
    y1 = y1.reshape(-1, 1)
    y2 = y2.reshape(-1, 1)

    # MinMaxScaler를 이용하여 스케일링
    scaler = MinMaxScaler()
    y1_scaled = scaler.fit_transform(y1)
    y2_scaled = scaler.fit_transform(y2)

    # 스케일링된 신호를 다시 1D 배열로 변환
    y1_scaled = y1_scaled.flatten()
    y2_scaled = y2_scaled.flatten()

    # 시간 도메인에서의 신호를 비교
    diff = y1_scaled - y2_scaled

    # 차이값들의 절대값의 평균과 제곱합의 평균 계산
    mae = np.mean(np.abs(diff))
    cosine_similarity = 1 - cosine(y1_scaled, y2_scaled)
    # squared_mean_diff = np.mean(diff ** 2)

    # 시간 도메인에서 두 오디오 신호 겹쳐서 시각화
    # plt.figure(figsize=(12, 6))
    # plt.plot(np.arange(len(y1)) / sr1, y1, label='Audio 1')
    # plt.plot(np.arange(len(y2)) / sr2, y2, label='Audio 2', alpha=0.7)
    # plt.title("Audio Comparison in Time Domain")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Amplitude")
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

    return mae, cosine_similarity

# print(compare_audio_time_domain("./nar/심규선_원본.mp3", "./nar/심규선_높낮이1up.mp3"))
