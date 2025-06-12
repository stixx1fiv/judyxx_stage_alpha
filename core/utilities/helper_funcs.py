import random
import time

def embed_and_score_events(content):
    """
    Placeholder embedding and scoring function.

    - Embedding: Returns a dummy vector (list of floats).
    - Score: Simple heuristic based on content length & keywords.
    """
    # Dummy embedding: vector of 128 zeros (pretend embedding dim)
    embedding = [0.0] * 128

    # Simple scoring heuristic
    keywords = ["urgent", "important", "remember", "alert", "note"]
    score = 0

    # Boost score if keywords present
    content_lower = content.lower()
    for kw in keywords:
        if kw in content_lower:
            score += 5

    # Score length bonus: longer messages = more important
    score += min(len(content) / 50, 10)  # cap length bonus at 10

    # Add random fuzz for realism
    score += random.uniform(0, 1)

    # Clamp score between 0 and 20
    score = max(0, min(score, 20))

    # Fake some processing delay for realism
    time.sleep(0.05)

    return embedding, score
