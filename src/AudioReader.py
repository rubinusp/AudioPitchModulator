# 1.Standard Modules
import pprint

# 2. Extension Modules
import ffmpeg

# 3. Local Modules
from Model.RawAudio import RawAudio

class AudioReader:

    def __init__(self):
        super().__init__()

    def read(self, file):
        # format = self.__findFileExtension(file)

        try:
            channels, duration, rate = self.__probeBasicInfo(file)
            audio = RawAudio(channels, duration, rate)

            stream = self.__fromAudioToPCM(file)
            audio.set_stream(stream)
            pprint.pprint(audio)

        except Exception as e:
            raise IOError("Unsupported format")

    # def __findFileExtension(self, file):
    #
    #     doc_index = file.rfind(".")
    #     return file[doc_index:]

    def __fromAudioToPCM(self, file):
        out, _ = (
            ffmpeg
            .input(file)
            # Outputs the audio according to signed PCM 16-bit little-endian standard
            .output('-', format='s16le', acodec='pcm_s16le', ac=1)
            .overwrite_output()
            .run(capture_stdout=True)
        )
        return out

    def __probeBasicInfo(self, file):
        probe = ffmpeg.probe(file)
        stream = probe['streams'][0]
        return stream['channels'], stream['duration'], stream['sample_rate']