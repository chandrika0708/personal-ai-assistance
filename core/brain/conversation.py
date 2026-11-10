"""
JARVIS AI 2.0
Conversational Intelligence Engine
"""

from datetime import datetime


class ConversationEngine:

    def __init__(self):
        self.assistant_name = "JARVIS"
        self.conversation_history = []

    def generate_response(self, user_message):

        message = user_message.lower().strip()

        if not message:
            return "Please enter a message."

        if message in ["hello", "hi", "hey"]:
            response = "Hello! I am JARVIS AI 2.0. How can I assist you?"

        elif "your name" in message:
            response = "I am JARVIS, your AI desktop assistant."

        elif "how are you" in message:
            response = "All systems are running. I am ready to assist you."

        elif "time" in message:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            response = f"The current time is {current_time}."

        elif "what can you do" in message:
            response = (
                "I am being developed with conversational AI, "
                "voice intelligence, memory, computer vision, "
                "research intelligence and an AI Video Studio."
            )

        else:
            response = (
                "I received your message. My advanced AI "
                "intelligence is still under development."
            )

        self.conversation_history.append({
            "user": user_message,
            "assistant": response
        })

        return response