from transformers import pipeline

def load_model():
    classifier = pipeline(
        "text-classification",
        model="mrm8488/bert-tiny-finetuned-sms-spam-detection"
    )
    return classifier