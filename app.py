perguntas = ("Qual o livro mais lido do mundo depois da Bíblia?",
             "Quanto tempo a luz do Sol demora para chegar na Terra?",
             "Em que período da pré-história o fogo foi descoberto?",
             "Qual o país da Ásia que fala português?",
             "Júpiter e Plutão são correlatos romanos de quais deuses gregos?")

opcoes = (("A. O Senhor dos Anéis","B.  Dom Quixote","C. O Pequeno Príncipe","D. Ela, a Feiticeira","E. Harry Potter"),
          ("A. 12 minutos","B. 1 dia","C. 12 horas","D. 8 minutos","E. 12 segundos"),
          ("A. Neolítico","B. Paleolítico","C. Idade dos Metais","D. Período da Pedra Polida","E. Idade Média"),
          ("A. Índia","B. Filipinas","C. Moçambique","D. Macau","E. Portugal"),
          ("A. Ares e Hermes","B. Cronos e Apolo","C. Zeus e Hades","D. Dionísio e Deméter","E. Zeus e Ares"))

respostas =("B","D","B","D","C")

palpites = []
pontuacao = 0
numero_perguntas = 0

for pergunta in perguntas:
    print('-'*40)
    print(pergunta)
    for opcao in opcoes[numero_perguntas]:
        print('-'*40)
        print(opcao)

    palpite = input("Pressione(A,B,C,D,E):").upper()
    palpites.append(palpite)
    if palpite == respostas[numero_perguntas]:
        pontuacao+=1
        print("ACERTOU!")
    else:
        print("Você errou!")
        print(f"{respostas[numero_perguntas]} é a resposta certa")


    numero_perguntas +=1

# descobrir as respostas e palpites dados:
print("-"*30)
print("        RESULTADO       ")
print('-'*30)

print("resposta: ", end="")
for resposta in respostas:
    print(resposta, end =' ')
print()

print("palpites: ", end = "")
for palpite in palpites:
    print(palpite, end =' ')
print()

# resultado em porcentagem:
pontuacao = int(pontuacao / len(perguntas) * 100)
print(f"A sua pontução é de: {pontuacao}%")
