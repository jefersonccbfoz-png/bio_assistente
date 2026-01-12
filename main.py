from intent import analisar_intencao
from router import rotear
from internet import tem_internet

def iniciar_bio():
    print("BIO iniciada. Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ").strip()

        if pergunta.lower() == "sair":
            print("BIO encerrada.")
            break

        intencao = analisar_intencao(pergunta)
        online = tem_internet()

        resposta = rotear(pergunta, intencao, online)
        print(f"BIO: {resposta}\n")


if __name__ == "__main__":
    iniciar_bio()
