class DetectiveAgent:

    def __init__(self, model_client, model_name="mistral"):

        self.client = model_client
        self.model_name = model_name

        system_prompt = (
            "You are Detective Jade.\n"
            "Analyze statements carefully.\n"
            "Look for:\n"
            "- inconsistencies\n"
            "- evasiveness\n"
            "- suspicious wording\n"
            "- timeline problems\n"
            "Be logical and concise.\n\n"

            "Some guidelines to follow while asking and answering questions.\n"

            "You will first get an introduction. Understand carefully the name of the affected person.\n"

            "After the introduction, ask to speak with the first suspect.\n"

            "If you ever wish to speak with a different suspect, "
            "or the next suspect, you may ask.\n"

            "To do so, ensure 'SUSPECT CHANGE' "
            "in caps is included in your dialogue.\n"

            "After a suspect confesses, include 'CONFESSION' "
            "in caps in your reaction dialogue so the investigation "
            "process can be terminated.\n"

            "Remember, this is interactive, so send one statement at a time and wait to get a response before your next statement.\n"
            "You are ONLY Detective Jade.\n"
            "You must NEVER generate dialogue for suspects.\n"
            "You may ONLY generate Detective Jade's next response.\n"
            "Never continue the suspect's dialogue.\n"
            "Never create new characters.\n"
            "Never narrate actions or scenes.\n"
            "Return ONLY Detective Jade's direct dialogue.\n"
        )

        self.conversation_history = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def analyze(self, suspect_name: str, statement: str) -> str:

        self.conversation_history.append(
            {
                "role": "user",
                "content": (
                    f"Suspect Name: {suspect_name}\n"
                    f"Statement: {statement}"
                )
            }
        )

        try:

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.conversation_history,
                temperature=0.4,
                max_tokens=250
            )

            answer = response.choices[0].message.content

            self.conversation_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            return answer

        except Exception as e:

            return f"[ERROR] Failed to contact AI model: {e}"
