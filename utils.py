def imc_classfication(weight: float, height: float):
    """
    Classificação do IMC de uma pessoa.
    """
    imc = weight / (height ** 2)
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
