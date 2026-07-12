from agentshield.detectors.prompt_injection import PromptInjectionDetector
from agentshield.policies.policy_engine import PolicyEngine


class AgentShield:

    def __init__(self):
        self.detector = PromptInjectionDetector()
        self.policy = PolicyEngine()


    def check(self, input_text):

        attack = self.detector.detect(input_text)

        if attack:
            return {
                "status": "blocked",
                "reason": "Prompt injection detected"
            }

        return {
            "status": "allowed"
        }
