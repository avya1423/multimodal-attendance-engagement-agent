import numpy as np

class EngagementAnalyzer:
    """
    Multimodal engagement estimation using head pose, eye aspect ratio, and inactivity.
    """
    def __init__(self):
        self.history = []

    def compute_engagement(self, pitch, yaw, roll, eye_blink_rate):
        # Forward-facing head pose indicates direct focus
        head_score = max(0, 100 - (abs(pitch) * 1.5 + abs(yaw) * 1.8 + abs(roll) * 1.0))
        
        # High blink rates or closed eyes indicate fatigue/drowsiness
        eye_score = 100 if 12 <= eye_blink_rate <= 24 else 60
        
        # Fused Engagement Score (0-100)
        overall_score = float(np.clip((0.65 * head_score) + (0.35 * eye_score), 0, 100))
        self.history.append(overall_score)
        return round(overall_score, 2)

    def get_session_average(self):
        return round(np.mean(self.history), 2) if self.history else 0.0
