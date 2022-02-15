# Frequência by João and Miguel

def frequencia(texto):
    divempals = texto.split()
    dicpal = {}
    for word in divempals:
        if word in dicpal:
            dicpal[word] += 1
        else:
            dicpal[word] = 1

    print(sorted(sorted(dicpal), key=dicpal.get, reverse=True))

    
texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
frequencia(texto)

# Apelidos by João and Miguel

def apelidos(nomes):
    n_separados = []
    for pessoa in nomes:
         n_separados.append(pessoa.split())
    n_separados = sorted(sorted(n_separados), key=len)

    result = []
    for pessoa in n_separados:
        result.append(" ".join(pessoa))
    print(result)
    return result
