import librosa

# 음성 파일 로딩
audio_path1 = './sample-1-1.wav'
audio_path2 = './sample-1-2.wav'
audio1, sr1 = librosa.load(audio_path1, sr=None)
audio2, sr2 = librosa .load(audio_path2, sr=None)

# 특징 추출
features1 = librosa.feature.mfcc(y=audio1, sr=sr1)
features2 = librosa.feature.mfcc(y=audio2, sr=sr2)

# 유사도 비교
similarity = librosa.feature.delta(features1) - librosa.feature.delta(features2)
print(similarity.shape)
similarity = sum(sum(abs(similarity)))

print(f"Similarity: {similarity}")
