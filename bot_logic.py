import random

responses = {
    "greetings": ["Hi there!", "Hello!", "Hey, how can I support you today?"],
    "stress": ["Take 3 deep breaths. Hold. Release. You’ve got this!"],
    "tired": ["You deserve rest. How about a short break or nap?"],
    "bored": ["Wanna hear a fun fact or do a breathing exercise?"],
    "panic": ["Try 5-4-3-2-1 grounding: 5 things you see, 4 you feel, 3 you hear..."],
    "happy": ["That's great! What made you happy today?"],
    "sad": ["I'm here for you. Want to hear a positive quote?"],
    "quote": [
        "You are doing the best you can, and that’s enough.",
        "Difficult roads often lead to beautiful destinations.",
        "You’re not a burden, you’re human."
    ],
    "motivate": [
        "Small progress is still progress.",
        "Every day is a fresh start.",
        "Believe in your magic!"
    ]
}

def get_bot_response(msg):
    msg = msg.lower()

    if "happy" in msg: return random.choice(responses["happy"])
    if "sad" in msg or "depress" in msg: return random.choice(responses["sad"])
    if "panic" in msg or "attack" in msg: return random.choice(responses["panic"])
    if "tired" in msg or "sleep" in msg: return responses["tired"][0]
    if "stress" in msg: return random.choice(responses["stress"])
    if "quote" in msg or "motivate" in msg: return random.choice(responses["quote"])
    if "bored" in msg: return random.choice(responses["bored"])
    if "hi" in msg or "hello" in msg: return random.choice(responses["greetings"])

    return "I'm here to listen. You can talk to me about anything you're feeling."
