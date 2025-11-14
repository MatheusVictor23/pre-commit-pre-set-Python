import pytest
from src.app import somar, multiplicar

# 1. Teste Básico (Caso de Sucesso)
def test_somar_numeros_positivos():
    """Verifica se a soma de 3 e asd5 é 8. """
    resultado = somar(3, 5)
    # A afirmação (assert) é o coração do teste
    assert resultado == 8

# 2. Teste de Borda (Caso Limite)
def test_somar_com_numero_negativo():
    """Verifica se a soma lida corretamente com números neg ativos."""
    resultado = somar(10, -4)
    assert resultado == 6

# 3. Teste de Multiplicação
def test_multiplicar_por_zero():
    """Verifica se a multiplicação por zero funciona."""
    resultado = multiplicar(50, 0)
    assert resultado == 0

# 4. Teste de Exceção (Caso de Falha Esperada)
def test_somar_com_tipo_incorreto():
    """Verifica se a função levanta um TypeError quando passamos uma string."""
    with pytest.raises(TypeError):
        # Esperamos que a função 'somar' levante um TypeError neste ponto
        somar(2, "tres")