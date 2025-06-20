import gradio as gr
from groq import Groq
import os

# Configuração do cliente Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Busca a chave da variável de ambiente
client = Groq(api_key=GROQ_API_KEY)

# Função para consultar o modelo no Groq
def consultar_groq(pergunta):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Exemplo de modelo, ajuste conforme necessário
            messages=[{"role": "user", "content": pergunta}]
        )
        resposta = response.choices[0].message.content
        return resposta
    except Exception as e:
        return f"Erro ao consultar o modelo: {e}"

# Interface Gradio
demo = gr.Interface(
    fn=consultar_groq,
    inputs=gr.Textbox(label="Pergunta para o modelo Groq"),
    outputs=gr.Textbox(label="Resposta do modelo"),
    title="Consulta ao Modelo Groq",
    description="Digite uma pergunta e consulte um modelo hospedado no Groq."
)

demo.launch()
