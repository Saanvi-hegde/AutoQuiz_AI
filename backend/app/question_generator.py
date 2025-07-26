from transformers import pipeline

qg = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

def generate_questions(text: str):
    output = qg(text[:512])
    return [output[0]['generated_text']]
