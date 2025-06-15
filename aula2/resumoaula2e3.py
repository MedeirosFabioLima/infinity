# Dicionário de tradução simples (inglês para português)
traducao = {
    "an": "um",
    "hello": "olá",
    "how": "como",
    "are": "está",
    "you": "você",
    "i": "eu",
    "am": "estou",
    "fine": "bem",
    "thanks": "obrigado",
    "good": "bom",
    "morning": "manhã",
    "night": "noite",
    "beautiful": "bonito",
    "Thing":" Coisa",
     "Place":" Lugar",
    "Time":"Tempo",
    "Day":"Dia",
    "Night": "Noite",
    "Week":" Semana",
    "Month":" Mês",
    "Year":"Ano",
    "World": "Mundo",
    "House": "Casa",
    "Car":"Carro",
    "Food":"Comida",
    "Water":"Água",
    "Money":"Dinheiro",
    "Job":"Trabalho",
    "School":"Escola",
    "Work":"Trabalho",
    "Family":"Família",
    "Friend":"Amigo",
    "Love":"Amor",
    "Hate":"Odeio",
    "Happy":"Feliz",
    "Sad":"Triste",
    "Angry":"Raivoso",
    "Excited":"Empolgado",
    "Bored":"Aborrecido",
    "Tired":"Fadiga",
    "Sleepy":"Sonolento",
    "mine" : "meu",
    "is": "é",
    "are": "são",
    "have": "tenho",
    "has": "tem",
    "had": "tinha",
    "will": "vai",
    "would": "iria",
    "can": "pode",
    "could": "poderia",
    "may": "pode",
    "might": "poderia",
    "shall": "vai",
    "should": "deveria",
    "must": "deve",
    "ought": "deveria",
    "shall not": "não vai",
    "should not": "não deve",
    "must not": "não deve",
    "can not": "não pode",
    "could not": "não pode",
    "may not": "não pode",
    "might not": "não pode",
    "will not": "não vai",
    "would not": "não iria",
    "have not": "não tem",
    "has not": "não tem",
    "had not": "não tinha",
    "is not": "não é",
    "are not": "não são",
    "have been": "foi",
    "has been": "foi",
    "had been": "foi",
    "is being": "está sendo",
    "are being": "estão sendo",
    "have been being": "estava sendo",
    "has been being": "estava sendo",
    "had been being": "estava sendo",
    "was": "foi",
    "were": "foram",
    "was being": "estava sendo",
    "were being": "estavam sendo",
    "has been": "foi",
    "good":"bom",
    "bad":"ruim",
    "big":"grande",
    "small":"pequeno",
    "happy":"feliz",
    "to work": "trabalhar"
    }
    


   
# Solicita ao usuário uma frase em inglês
frase = input("Digite uma frase em inglês: ")

# Divide a frase em palavras
palavras = frase.lower().split()

# Traduz palavra por palavra
traduzida = []
for palavra in palavras:
    if palavra in traducao:
        traduzida.append(traducao[palavra])
    else:
        traduzida.append(f"[{palavra}]")  # palavra não encontrada

# Exibe a frase traduzida
print("Tradução aproximada:")
print(" ".join(traduzida)+"?")
