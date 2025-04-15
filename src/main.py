def calculate(entrada) -> float:
    if '/' in entrada:
        partes = entrada.split('/')
        resultado = float(partes[0]) / float(partes[1])
