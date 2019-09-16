class RawAudio:

    def __init__(self, ac, ad, ar, stream=None):
        self.ac = ac                # audio channels
        self.ad = ad                # audio duration
        self.ar = ar                # audio rate
        self.stream = stream        # raw audio stream

    def set_ac(self, ac):
        self.ac = ac

    def set_ad(self, ad):
        self.ad = ad

    def set_ar(self, ar):
        self.ar = ar

    def set_stream(self, stream):
        self.stream = stream

    def get_ac(self):
        return self.ac

    def get_ad(self):
        return self.ad

    def get_ar(self):
        return self.ar

    def get_stream(self):
        return self.stream
