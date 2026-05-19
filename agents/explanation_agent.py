class ExplanationAgent:
    def explain(self, email):
        email = email.lower()
        reasons = []

        if "click" in email:
            reasons.append("🔗 Suspicious link detected")
        if "urgent" in email:
            reasons.append("⚠️ Creates urgency")
        if "verify" in email:
            reasons.append("🔐 Requests verification")
        if "password" in email:
            reasons.append("🔑 Sensitive data request")

        return reasons if reasons else ["No strong phishing indicators"]