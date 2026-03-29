# 注意：2.x 版本直接从 moviepy 导入，不再有 .editor
from moviepy import VideoFileClip 
import os

def extract_audio(video_path, audio_output_path):
    """
    从视频中提取音频 (适配 MoviePy 2.x)
    """
    if not os.path.exists(video_path):
        print(f"错误：找不到视频文件 {video_path}")
        return

    try:
        # 加载视频文件
        video = VideoFileClip(video_path)
        
        # 提取音频
        audio = video.audio
        
        # 保存音频文件
        # codec参数写法不变
        audio.write_audiofile(audio_output_path, codec='mp3')
        
        print(f"成功！音频已保存至: {audio_output_path}")
        
        # 关闭资源
        audio.close()
        video.close()
        
    except Exception as e:
        print(f"发生错误: {e}")


# 使用示例
if __name__ == "__main__":
    # 修改为你的视频文件路径
    # input_video = "./music/self-music_0_0.mp4" 
    # # 修改为你想要保存的音频路径
    # output_audio = "./music/self-music_0_0.mp3"
    input_folder = "./music/"
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(input_folder, filename)
            audio_output_path = os.path.join(input_folder, os.path.splitext(filename)[0] + ".mp3")
            extract_audio(video_path, audio_output_path)
    