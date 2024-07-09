from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the chatbot
edu_bot = ChatBot(
    'EduBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    database_uri='sqlite:///database.sqlite3'
)
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(edu_bot)

# Train the chatbot based on the English corpus
trainer.train(
    'chatterbot.corpus.english'
)
# Custom educational training data
custom_conversations = [
    "What is machine learning?",
    "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data.",
    "What is a chatbot?",
    "A chatbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, instead of providing direct contact with a live human agent."
]

trainer.train(custom_conversations)
def chat_with_bot():
    print("Hello! I am EduBot. How can I help you today?")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("EduBot: Goodbye!")
                break
            response = edu_bot.get_response(user_input)
            print(f"EduBot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
if __name__ == "__main__":
    chat_with_bot()
