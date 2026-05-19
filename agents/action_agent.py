class ActionAgent:
    def take_action(self, label, score, reasons):
        if label == "Phishing" or len(reasons) >= 2:
            return "🚨 Block Email + Send Alert"
        return "✅ Allow Email"