def generate_flashcards(text: str):
    # Dummy implementation — can improve later
    lines = text.split(".")
    flashcards = []
    for line in lines[:5]:
        question = f"What is: {line.strip()}?"
        answer = line.strip()
        flashcards.append({"question": question, "answer": answer})
    return flashcards
