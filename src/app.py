def somar(a: int, b: int) -> int:
    """Retorna a soma de dois números inteiros."""
    if not isinstance(a, int) or not isinstance(b, int):
        # Esta é uma regra simples para forçar um erro se o tipo estiver errado
        raise TypeError("Ambos os argumentos devem ser inteiros.")
    return a + b

def multiplicar(a: int, b: int) -> int:
    """Retorna a multiplicação de dois números inteiros."""
    return a * b