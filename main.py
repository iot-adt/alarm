import pyaudio
import wave

# 현재 디렉토리의 example.wav 파일 실행
wav_file = "example.wav"  # 같은 디렉토리에 있는 파일 이름만 지정

# 파일 열기
wf = wave.open(wav_file, 'rb')

# PyAudio 스트림 생성
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# 파일 데이터를 읽어서 스트림에 출력
data = wf.readframes(1024)
while data:
    stream.write(data)
    data = wf.readframes(1024)

# 스트림 종료
stream.stop_stream()
stream.close()
p.terminate()
wf.close()
