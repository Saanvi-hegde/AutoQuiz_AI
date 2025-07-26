from fastapi import FastAPI, UploadFile, File
from app import pdf_utils, summarizer, question_generator, flashcard_generator

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Generative AI Educational Tool"}

@app.post("/analyze-pdf/")
async def analyze_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = pdf_utils.extract_text_from_pdf_bytes(content)
    summary = summarizer.get_summary(text)
    questions = question_generator.generate_questions(text)
    flashcards = flashcard_generator.generate_flashcards(text)
    return {
        "summary": summary,
        "questions": questions,
        "flashcards": flashcards
    }
