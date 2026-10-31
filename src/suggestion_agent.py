class TeachingAssistantAgent:
    """
    Generates dynamic, context-aware teaching adjustments for instructors.
    """
    @staticmethod
    def generate_suggestions(engagement_score: float, participation_ratio: float):
        suggestions = []
        if engagement_score < 50.0:
            suggestions.append("Attention dip detected: Pause and introduce a 2-minute interactive poll or Q&A.")
            suggestions.append("Check session pacing; content density may currently be too high.")
        elif 50.0 <= engagement_score < 75.0:
            suggestions.append("Engagement is moderate: Encourage peer discussion or open-floor feedback.")
        else:
            suggestions.append("Classroom attention is optimal: Continue with planned lesson delivery.")

        if participation_ratio < 15.0:
            suggestions.append("Low verbal interaction detected: Ask directed, open-ended questions.")
        
        return suggestions
