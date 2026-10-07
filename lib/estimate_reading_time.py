def estimate_reading_time(text: str) -> float:
    if not isinstance(text, str):
        raise Exception("This needs to be a string!")
    
    word_count = len(text.split())
    return word_count / 200