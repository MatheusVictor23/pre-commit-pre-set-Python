Guia de Implementação: Pre-Commit com Pytest-Testmon. Este documento detalha como configurar o pre-commit para executar apenas os testes relevantes para os arquivos em git staged, utilizando a ferramenta pytest-testmon.
## Pré-requisitos: 
1. Certifique-se de que as ferramentas necessárias estão instaladas: 
   ```
    pip install pre-commit pytest pytest-testmon
   ```
2. Configuração do **pytest.ini** ou demais arquivos de configuração do pytest: pytest.tom, pyproject.toml, tox.ini, etc.
   ```
    [pytest]
    minversion = 6.0
    addopts = 
        -ra 
        -v

    testpaths =
        tests

    python_files = test_*.py *_test.py

   ```

## Configuração pre-commit:
1. Adicione o arquivo .pre-commit-config.yaml na raiz do projeto:
   ```
    repos:
    - repo: local
    hooks:
      - id: pytest-testmon
        name: pytest-testmon
        entry: pytest --testmon
        language: python
        pass_filenames: false
        files: \.(py)$ 
        stages: [pre-commit]
        additional_dependencies:
            - pytest
            - pytest-testmon
        python_version: python3.10
   ```


2. Inicialização do pre-commit.Instale o hook no seu repositório Git:
    ```
    pre-commit install
    ```

## !! Importante:
Para a demonstração é necessário "treinar" o testmon, execute o comando:
```pytest``` para realizar a cobertura de todos os teste do projeto, o testmon irá mappear os testes e usar como guia para execut os testes apenas nos arquivos modificados e com teste associado.


## Demonstração de Casos de Commit:
O projeto possui 3 arquivos para exemplo, que são: 

#### app.py
Contém as funções de soma e multiplicação. Os testes serão baseados nessas funções.

#### test_app.py
Contém 4 casos de teste associados ao arquivo app.py

####  Index.py
Este arquivo não tem nenhuma função de teste, apenas um print. Ele deve ser usado para simular a modificação em um arquivo sem teste associado.

### Testes
Faça alguma modificação em algum desses arquivos e dê commit. O testmon irá executar apenas os testes associados aos arquivos em stagged. 

#### Saídas Possíveis:
1. PASSED
2. FAILED
3. no tests ran (sem testes a executar)
4. SKIPPED (Arquivos sem .py)