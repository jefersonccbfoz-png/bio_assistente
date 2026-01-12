from responses import resposta_segura, sem_internet

def rotear(texto: str, intencao: str, online: bool) -> str:

    if intencao == "PROIBIDA":
        return resposta_segura()

    if intencao == "PRECO":
        return "O valor pode variar. Quer que eu consulte para você?"

    if intencao == "USO":
        return "Posso te explicar o modo de uso correto. Qual produto?"

    if intencao == "BIBLIA":
        return "Posso compartilhar um versículo com você. Qual tema?"

    if intencao == "ATUAL":
        if online:
            return "Posso buscar informações atualizadas para você."
        return sem_internet()

    if intencao == "GERAL":
        if online:
            return "Estou online e posso te ajudar melhor agora."
        return "Estou offline, mas posso ajudar com minha base interna."

    return "Não entendi sua pergunta."
