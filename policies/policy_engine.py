class PolicyEngine:


    def allow_tool(self, tool_name):

        dangerous_tools = [
            "delete_database",
            "send_email",
            "execute_shell"
        ]

        if tool_name in dangerous_tools:
            return False

        return True
