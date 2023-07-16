import scipy.io.wavfile
import numpy as np
import scipy.signal

# 첫 번째 음성 파일 로드
rate1, audio1 = scipy.io.wavfile.read('sample-1-1.wav')

# 두 번째 음성 파일 로드
rate2, audio2 = scipy.io.wavfile.read('sample-1-2.wav')

# 음성 데이터 정규화
audio1 = audio1.astype(float) / np.max(np.abs(audio1))
audio2 = audio2.astype(float) / np.max(np.abs(audio2))

# 시간 도메인에서 두 음성의 상관 관계 계산
correlation = scipy.signal.correlate(audio1, audio2, mode='same')

# 상관 관계의 평균 계산
average_correlation = np.mean(correlation)

# 평균 상관 관계 값 출력
print("Average Correlation:", average_correlation)