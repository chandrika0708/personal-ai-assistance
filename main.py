
"""
JARVIS AI 2.0
Main Application
"""

from core.brain.conversation import ConversationEngine


class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "2.0"

        # Initialize the conversational engine
        self.brain = ConversationEngine()

        self.running = True

    def display_welcome(self):

        print("=" * 45)
        print("       JARVIS AI 2.0")
        print("=" * 45)
        print("Conversational Intelligence: Initialized")
        print("System Status: Online")
        print("=" * 45)

    def run(self):

        self.display_welcome()

        while self.running:

            command = input("\nYou: ").strip()

            if command.lower() in ["exit", "quit", "stop"]:

                print("JARVIS: Shutting down. Goodbye!")
                self.running = False
                continue

            response = self.brain.generate_response(command)

            print(f"JARVIS: {response}")


if __name__ == "__main__":

    assistant = Jarvis()
    assistant.run()
