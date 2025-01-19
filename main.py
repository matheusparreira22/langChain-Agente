from langchain.tools import BaseTool
import os
from langchain_openai import ChatOpneAI
pergunta = 'Quais os dados da Ana?'

class DadosDeEstudante(BaseTool):
    name = 'DadosDeEstudante'
    description =    """Esta Ferramenta estrai o histórico e preferencia de um estudante de acordo com seu estado"""

    def run(self, input: str) -> str:
        llm = chatOpenai(model="gpt-4o")
            api_key