def analisar_intencao(texto: str) -> str:
    texto = texto.lower()

    if any(p in texto for p in ["cura", "tratar", "doença"]):
        return "PROIBIDA"

    if any(p in texto for p in ["preço", "valor"]):
        return "PRECO"

    if any(p in texto for p in ["como usar", "modo de uso"]):
        return "USO"

    if any(p in texto for p in ["bíblia", "salmo", "versículo"]):
        return "BIBLIA"

    if any(p in texto for p in ["hoje", "agora", "notícia"]):
        return "ATUAL"

    return "GERAL"
