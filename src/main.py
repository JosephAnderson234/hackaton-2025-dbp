def calculate(entrada) -> float:
    entrada = entrada.strip()
    if '*' in entrada:
        partes = entrada.split('*')
        if len(partes) == 2:
            num1 = float(partes[0])
            num2 = float(partes[1])
            return num1 * num2
    if '-' in entrada:
        partes = entrada.split('-')
        num1 = float(partes[0])
        num2 = float(partes[1])
        return num1 - num2
    if '/' in entrada:
        partes = entrada.split('/')
        return float(partes[0]) / float(partes[1])
    