import time
from app.core.logging import get_logger
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)  #* configurando o logger para usar o nome do módulo atual, útil para saber de onde as mensagens de log estão vindo

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) #! configurando a chave da API do Gemini a partir das variáveis de ambiente, garantindo que a chave não fique hardcoded no código

def generate_smart_description(title: str, resource_type: str):
    start_time = time.time()
    
    system_prompt = (
        "Você é um Assistente Pedagógico especializado em organização "
        "de materiais educacionais. "
        "Responda exclusivamente em JSON válido com o seguinte formato:\n"
        "{\n"
        '   "description:" "Descrição detalhada e pedagógica do material",\n'
        '   "tags": ["tag1", "tag2", "tag3"]\n'
        "}\n"
        "Forneça exatamente 3 tags relevantes.\n"
        "As tags devem:\n"
        "- Conter no máximo 3 palavras\n"
        "- Ser escritas em minúsculo\n"
        "- Não conter espaços removidos (ex: 'matemática    básica')\n"
        "- Não usar hífens ou junções de palavras\n"
        "- Ser o mais específicas possível, evitando termos genéricos (ex: 'ciências' é muito genérico, 'ciências biológicas' é melhor)\n"
        "- Evitar repetições de tags para títulos semelhantes\n"
    )
    
    user_prompt = (
        f"Título: {title}\n"
        f"Tipo: {resource_type}\n"
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = system_prompt + "\n\n" + user_prompt,
        config={
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "object",
            "properties": {
                "description": {"type": "string"},
                "tags": {
                    "type": "array",
                    "items": {"type": "string"}
                    }
            },
            "required": ["description", "tags"]
        }
        }
    )
    
    usage = response.usage_metadata

    total_tokens = usage.total_token_count
    
    latency = round(time.time() - start_time, 2)
    
    logger.info(
    f'AI Request | '
    f'Title="{title}" | '
    f'TokenUsage={total_tokens} | '
    f'Latency={latency}s'
    )
    
    import json
    
    #! o método parsed do genai já tenta converter a resposta para um objeto Python, mas como a resposta pode não ser um JSON válido, é importante tratar isso com um try-except para evitar que o sistema quebre caso a IA retorne algo inesperado
    try:
        parsed = response.parsed
    except Exception:
        raise ValueError("AI didn't return valid JSON")
    
    return parsed