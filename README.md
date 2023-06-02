# Chatbot
Dette er en chatbot jeg har laget med python.
Den leter etter ord du sier og svarer med en setning.

Det eneste du trenger er python, også en kode som jeg har laget så skal det funke.

Du kan også lage en ordentlig chatbot med openai, detter er hvordan:
Openai key:
-	Gå til openai api
-	Gå til ditt personlig ikon i høyere hjørne
-	Klikk på den
-	Gå til view api-key
-	Create new secret key

Python:
-	pip install openai

import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
