class AudioActivityMonitor:
    """
    Offline Voice Activity and Discussion Level Monitor.
    """
    def __init__(self):
        self.active_frames = 0
        self.total_frames = 0

    def process_audio_chunk(self, is_speech: bool):
        self.total_frames += 1
        if is_speech:
            self.active_frames += 1

    def get_participation_ratio(self):
        if self.total_frames == 0:
            return 0.0
        return round((self.active_frames / self.total_frames) * 100, 2)
