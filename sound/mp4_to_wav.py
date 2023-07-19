from moviepy.editor import VideoFileClip

# MP4 파일 경로
mp4_path = './y2mate.com - 이경영 닥쳐_360p.mp4'

# 비디오 클립 생성
video_clip = VideoFileClip(mp4_path)

# 오디오 추출 및 WAV 파일로 저장
wav_path = './AA.wav'
video_clip.audio.write_audiofile(wav_path)
