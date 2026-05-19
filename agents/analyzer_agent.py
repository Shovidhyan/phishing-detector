def analyze(self, email):
    short_email = email[:512]
    result = self.classifier(short_email, truncation=True)[0]

    label = result['label']
    score = float(result['score'])

    # 🔥 Rule-based override (CRITICAL FIX)
    email_lower = email.lower()

    risk_flags = 0

    if "http" in email_lower:
        risk_flags += 1
    if "urgent" in email_lower:
        risk_flags += 1
    if "verify" in email_lower:
        risk_flags += 1
    if "account" in email_lower:
        risk_flags += 1
    if "bank" in email_lower:
        risk_flags += 1

    # Override if strong phishing signals
    if risk_flags >= 2:
        label = "spam"
        score = max(score, 0.85)

    return "Phishing" if label == "spam" else "Legitimate", score