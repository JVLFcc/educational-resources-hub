import logging

#! configurando o logging para toda a aplicação, definindo o nível de log como INFO, e um formato que inclui timestamp, nível do log, nome do logger e a mensagem
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | [%(levelname)s] %(name)s | %(message)s",
)

def get_logger(name: str):
    return logging.getLogger(name)