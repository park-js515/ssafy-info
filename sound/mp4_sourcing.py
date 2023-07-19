from moviepy.editor import VideoFileClip

# 동영상 파일 경로
video_path = './video.mp4'

# 비디오 클립 생성
video_clip = VideoFileClip(video_path)

# MP4 파일로 저장
output_path = './now.mp4'
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
