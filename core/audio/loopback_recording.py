import soundcard as sc
import soundfile as sf
import os 

OUTPUT_FILE_NAME = "core/static/audio/out.wav"
SAMPLE_RATE = 48000              # [Hz]

def audio_recorder(record_sec):
    with sc.get_microphone(
            id=str(sc.default_speaker().name),
            include_loopback=True
        ).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*record_sec)

        # change "data=data[:, 0]" to "data=data",
        # if you would like to write audio as multiple-channels.
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
