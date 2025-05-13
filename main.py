def analisar(numeros):
    if not numeros:
        return "A lista está vazia."

    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = [num for num in numeros if num % 2 == 0]
    qnt_par = len(pares)

    return {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "qnt_par": qnt_par
    }
