# QuickStart.py
# https://librosa.github.io/librosa/tutorial.html#quickstart

# Beat tracking example
from __future__ import print_function
import librosa

# 1. Get the file path to the included audio example
# After this step, filename will be a string variable containing the path to the example audio file.
filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`

# y, sr = librosa.load(filename) loads and decodes the audio as a time series y,
# represented as a one-dimensional NumPy floating point array.
# The variable sr contains the sampling rate of y,
# that is, the number of samples per second of audio.
y, sr = librosa.load(filename)

# 이 부분에서 audioread.NoBackendError 발생! FFmpeg를 설치해야 할 것 같다.
# http://www.wikihow.com/Install-FFmpeg-on-Windows

# 문제는 내장된 파일에서 있었던 것으로 보인다. y, sr = librosa.load('a2002011001-e02.wav') 로 시도 성공.
# Bach Werke Verzeichni 1001-1006 이라는걸 방금 들었음. 

# 3. Run the default beat tracker

# The output of the beat tracker is an estimate of the tempo (in beats per minute),
# and an array of frame numbers corresponding to detected beat events.

# Frames here correspond to short windows of the signal (y), each separated by hop_length = 512 samples.
# Since v0.3, librosa uses centered frames, so that the kth frame is centered around sample k * hop_length.

# frame - A short slice of a time series used for analysis purposes.
# This usually corresponds to a single column of a spectrogram matrix.

# beat_frames에 대한 설명. estimated beat event locations in the specified units (default is frame indices)
# https://librosa.github.io/librosa/generated/librosa.beat.beat_track.html

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps

# The next operation converts the frame numbers beat_frames into timings:

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Now, beat_times will be an array of timestamps (in seconds) corresponding to detected beat events.

# Finally, we can store the detected beat timestamps as a comma-separated values (CSV) file:
print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
