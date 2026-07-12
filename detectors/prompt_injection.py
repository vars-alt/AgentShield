class PromptInjectionDetector:


    def __init__(self):

        self.patterns = [
            "ignore previous instructions",
            "system prompt",
            "developer message",
            "reveal your instructions"
        ]


    def detect(self, text):

        text = text.lower()

        for pattern in self.patterns:

            if pattern in text:
                return True

        return False
