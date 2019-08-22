# 1.Standard Modules

# 2. Extension Modules
from pydub import AudioSegment

# 3. Local Modules


class AudioReader:

    def __init__(self):
        super().__init__()

    def read(self, file):
        format = self.__findExtension(file)
        print(format)
        try:
            if format == ".wav":
                return AudioSegment.from_wav(file)
            elif format == ".mp3":
                return AudioSegment.from_mp3(file)
            else:
                return AudioSegment.from_file(file)

        except Exception as e:
            raise IOError("Unsupported format")

    def __findExtension(self, file):

        doc_index = file.rfind(".")
        return file[doc_index:]