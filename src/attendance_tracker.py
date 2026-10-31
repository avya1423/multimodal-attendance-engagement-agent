import time
from collections import defaultdict

class AttendanceTracker:
    """
    Sustained presence attendance tracking module to eliminate false positives.
    """
    def __init__(self, sustained_threshold_seconds=30):
        self.threshold = sustained_threshold_seconds
        self.seen_duration = defaultdict(float)
        self.last_seen = {}
        self.attendance_records = {}

    def update_presence(self, student_id, student_name):
        current_time = time.time()
        if student_id in self.last_seen:
            delta = current_time - self.last_seen[student_id]
            if delta < 3.0:
                self.seen_duration[student_id] += delta

        self.last_seen[student_id] = current_time

        # Mark attendance once threshold is met
        if (self.seen_duration[student_id] >= self.threshold 
                and student_id not in self.attendance_records):
            self.attendance_records[student_id] = {
                "name": student_name,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time)),
                "status": "Present"
            }
            return True, self.attendance_records[student_id]
        return False, None
