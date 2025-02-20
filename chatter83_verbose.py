"""
Chatter83 - Verbose Version
This is an educational version of the Chatter83 chatbot with:
- Full variable names for clarity
- Comments explaining each section
- Debugging mode enabled by default

This version is **not** optimized for the TI-83 Premium CE but is meant for learning how the chatbot works and will run on your computer.
"""

# Debug Mode (set to False to disable verbose output)
# This will print additional information about the chatbot's internal calculations
DEBUG = True

print("Loading chatbot data...")

# Import necessary data files
import w  # Word list (dictionary)
import sdata  # Score data (word importance + synonyms)
import kp1  # Knowledge base chunk 1
import kp2  # Knowledge base chunk 2
import kp3  # Knowledge base chunk 3
import kp4  # Knowledge base chunk 4

# Load word list
word_list = w.w

# Load knowledge base (questions mapped to answers)
knowledge_base = {}
knowledge_base.update(kp1.k)
knowledge_base.update(kp2.k)
knowledge_base.update(kp3.k)
knowledge_base.update(kp4.k)

# Load word scores (importance + synonyms)
score_data = sdata.s

print("Data loaded successfully.")

# Dictionary to map words to their corresponding index
dictionary = {}
for index, word in enumerate(word_list):
    dictionary[word] = index

print("Dictionary mapping complete. Total words:", len(word_list))

# Function to get word score and synonyms
def get_word_data(word_index):
    return score_data.get(word_index, {"s": 1, "a": []})

# Function to convert user input into a set of word IDs
def process_user_input(user_input):
    word_ids = set()
    for word in user_input.lower().split():
        if word in dictionary:
            word_id = dictionary[word]
            word_ids.add(word_id)
            # Include synonyms
            for synonym in get_word_data(word_id)["a"]:
                word_ids.add(synonym)
    return word_ids

# Function to find the best-matching question in the knowledge base
def find_best_match(user_input):
    user_word_ids = process_user_input(user_input)
    best_match = None
    highest_score = 0.0

    for stored_question, answer_ids in knowledge_base.items():
        total_weight = 0
        overlap_weight = 0

        for word_id in stored_question:
            word_score = get_word_data(word_id)["s"]
            total_weight += word_score
            if word_id in user_word_ids:
                overlap_weight += word_score

        normalized_score = overlap_weight / total_weight if total_weight else 0

        if DEBUG:
            print("Question:", stored_question, "Score:", normalized_score)

        if normalized_score > highest_score:
            highest_score = normalized_score
            best_match = stored_question

    return best_match

# Function to reconstruct the answer from word IDs
def reconstruct_answer(answer_ids):
    tokens = [word_list[i] for i in answer_ids]
    response = ""
    capitalize_next = True

    for token in tokens:
        if token in [".", "?", "!"]:
            response = response.rstrip() + token + " "
            capitalize_next = True
        else:
            if capitalize_next:
                token = token.capitalize()
                capitalize_next = False
            response += token + " "

    return response.strip()

print("Chatbot is ready! Type 'exit' to quit.")

# Main chatbot loop
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    
    if user_input.lower() == "verbose":
        DEBUG = not DEBUG
        print("Bot: Verbose mode toggled.")
        continue
    
    best_question = find_best_match(user_input)
    if best_question is not None:
        print("Bot:", reconstruct_answer(knowledge_base[best_question]))
    else:
        print("Bot: I don't know the answer yet!")
