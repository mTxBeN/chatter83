"""
Chatter83 - Training Script
This script automates the entire training process for Chatter83.

It:
- Reads `data.txt` (Q&A pairs)
- Generates word importance scores (`sdata.py`)
- Compresses the data (`kp#.py`)
- Generates all required Python files for the chatbot (`w.py`, `sdata.py`, `kp#.py`)

Usage:
Simply run `train.py` after updating `data.txt` with your Q&A pairs.
"""

import json
import re
import os
import math

# Set paths relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.txt")
SCORE_FILE = os.path.join(BASE_DIR, "score.txt")

# These are the final output files
WORD_LIST_FILE = os.path.join(BASE_DIR, "w.py")
SCORE_DATA_FILE = os.path.join(BASE_DIR, "sdata.py")
KNOWLEDGE_FILES = [os.path.join(BASE_DIR, f"kp{i+1}.py") for i in range(4)]  # Split into 4 files

### 🛠️ Helper Functions
def extract_words(text, keep_punctuation=False):
    """
    Cleans and extracts words from a string.
    If `keep_punctuation` is True, it keeps ".", "?", and "!" as separate tokens.
    """
    text = text.lower()
    if keep_punctuation:
        text = re.sub(r"([^a-z0-9 ])", r" \1 ", text)  # Separate punctuation
    else:
        text = re.sub(r"[^\w\s]", "", text)  # Remove all punctuation
    return text.split()

def load_data():
    """ Reads the Q&A pairs from data.txt. """
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

### 📊 Step 1: Generate Word Scores
def generate_word_scores(knowledge_base):
    """
    Assigns scores to words based on frequency in questions.
    Less common words get higher scores, common words get lower scores.
    """
    word_counts = {}
    for question in knowledge_base.keys():
        for word in extract_words(question):  # Extract words **without punctuation**
            word_counts[word] = word_counts.get(word, 0) + 1

    # Assign scores (higher score for rarer words, rounded for efficiency)
    word_scores = {word: max(1, round(1000 / count)) for word, count in word_counts.items()}

    # Format score dictionary
    score_dict = {
        word: {"s": score, "a": []} for word, score in word_scores.items()
    }

    return score_dict

def save_score_data(score_dict):
    """ Saves the generated scores to `score.txt`. """
    with open(SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(score_dict, file, indent=4)

### 🔗 Step 2: Compress Data
def compress_data(knowledge_base, score_dict):
    """
    Converts words into numeric IDs, generating compressed data for efficient storage.
    Also ensures ".", "?", and "!" are correctly stored.
    """
    question_words = set()
    answer_words = set()
    synonyms = set()

    # Extract unique words from Q&A pairs
    for question, answer in knowledge_base.items():
        for word in extract_words(question):  # **Remove punctuation from questions**
            question_words.add(word)
        for word in extract_words(answer, keep_punctuation=True):  # **Keep punctuation in answers**
            answer_words.add(word)

    # Ensure all words in scores are included
    for word, entry in score_dict.items():
        question_words.add(word)
        for syn in entry.get("a", []):
            synonyms.add(syn)

    # Create full vocabulary
    all_words = sorted(question_words.union(answer_words, synonyms, {".", "?", "!"}))
    word_to_id = {word: index for index, word in enumerate(all_words)}

    # Convert Q&A pairs to ID format
    compressed_knowledge = {
        tuple(word_to_id[word] for word in extract_words(q)): 
        tuple(word_to_id[word] for word in extract_words(a, keep_punctuation=True))  # **Keep punctuation**
        for q, a in knowledge_base.items()
    }

    # Convert scores using numeric word IDs
    compressed_scores = {
        word_to_id[word]: {"s": data["s"], "a": [word_to_id[syn] for syn in data["a"] if syn in word_to_id]}
        for word, data in score_dict.items() if word in word_to_id
    }

    return all_words, compressed_knowledge, compressed_scores

### 💾 Step 3: Save Data in Python Files
def save_python_files(word_list, knowledge_base, score_dict):
    """ Saves the compressed data into Python files for use on the calculator. """

    # Save word list
    with open(WORD_LIST_FILE, "w", encoding="utf-8") as out:
        out.write(f"w = {json.dumps(word_list)}\n")

    # Save word scores
    with open(SCORE_DATA_FILE, "w", encoding="utf-8") as out:
        out.write(f"s = {json.dumps(score_dict)}\n")

    # Split knowledge base into multiple files for calculator compatibility
    knowledge_items = list(knowledge_base.items())
    chunk_size = math.ceil(len(knowledge_items) / len(KNOWLEDGE_FILES))  # Distribute evenly

    for i, file_path in enumerate(KNOWLEDGE_FILES):
        chunk = knowledge_items[i * chunk_size:(i + 1) * chunk_size]
        with open(file_path, "w", encoding="utf-8") as out:
            out.write("k = {\n")
            for q_ids, a_ids in chunk:
                out.write(f"    {q_ids}: {a_ids},\n")
            out.write("}\n")

### 🔥 Main Training Process
def main():
    print("🔄 Loading Q&A data from data.txt...")
    if not os.path.exists(DATA_FILE):
        print(f"❌ Error: {DATA_FILE} not found. Make sure it's in the same folder as train.py!")
        return

    knowledge_base = load_data()

    print("📊 Generating word scores...")
    score_dict = generate_word_scores(knowledge_base)
    save_score_data(score_dict)

    print("🔗 Compressing data for efficient storage...")
    word_list, compressed_knowledge, compressed_scores = compress_data(knowledge_base, score_dict)
    
    print("💾 Saving final chatbot files...")
    save_python_files(word_list, compressed_knowledge, compressed_scores)

    print(f"✅ Training complete! Your chatbot files are ready in: {BASE_DIR}")

if __name__ == "__main__":
    main()