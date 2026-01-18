class SmartPiChat:
    """
    Offline chatbot logic.
    Add custom patterns in `self.responses`.
    """
    def __init__(self):
        self.responses = {
            "hello": "Hello! I am SmartPi, your AI assistant.",
            "how are you": "I am just a Pi, but I'm running well!",
            "what is your name": "I am SmartPi, your AI assistant.",
            "bye": "Goodbye! Have a nice day.",
        }

    def respond(self, text: str) -> str:
        """Return a response to the user text."""
        text = text.lower()
        for key, reply in self.responses.items():
            if key in text:
                return reply
        return "Sorry, I don't understand that yet."
