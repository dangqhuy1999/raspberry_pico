import audioread

def get_mp3_duration(file_path):
    with audioread.audio_open(file_path) as audio_file:
        duration = audio_file.duration  # Thời gian tính bằng giây
    return duration

# Sử dụng hàm
file_path = '/home/huynet/Desktop/02.mp3'
duration = get_mp3_duration(file_path)
print(f'Time duration: {duration} seconds')
