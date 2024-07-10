Tipos de dados são as classificações dos dados que uma variável pode armazenar :
    -> Inteiros (int): Números inteiros, positivos ou negativos, sem ponto decimal.
        Exemplo: x = 10, y = -5
    -> Flutuantes (float): Números com ponto decimal, também conhecidos como números de ponto flutuante.
        Exemplo: pi = 3.14, temperature = -15.6
    -> Strings (str): Sequências de caracteres, usadas para armazenar texto.
        Exemplo: name = "Alice", greeting = 'Hello'
    -> Booleanos (bool): Valores lógicos True ou False, usados em operações de comparação e controle de fluxo.
        Exemplo: is_student = True, is_sunny = False    

Variáveis são "caixas" que armazenam dados.
    -> Atribuição: O operador = é usado para atribuir valores a variáveis.
        Exemplo: age = 25, height = 1.75
        age é uma variavel, height é uma variavel
    -> Nomeação: Os nomes de variáveis podem conter letras, números e underscores (_), mas não podem começar com números.
        Exemplo: valid_variable_name = 10, invalid-variable-name = 5 # Não permitido

Estruturas de controle são usadas para controlar o fluxo de execução do programa com base em condições.
    -> Condicionais (if, elif, else): Permitem executar blocos de código com base em condições.
        if: Executa um bloco de código se a condição for verdadeira.
            if age < 18:
            print("Menor de idade")

        elif: Executa um bloco de código se a condição anterior foi falsa e esta condição for verdadeira.
            elif age < 65:
            print("Adulto")

        else: Executa um bloco de código se todas as condições anteriores foram falsas.
            else:
            print("Idoso")

Loops são usados para repetir um bloco de código várias vezes.
-> For Loop: Itera sobre uma sequência (como uma lista, tupla, string) ou um intervalo de números.
        range(): Função usada frequentemente com for para gerar uma sequência de números
                for i in range(5):
                print(i)
                # Output: 0 1 2 3 4
-> While Loop: Repete um bloco de código enquanto a condição especificada for verdadeira.
                count = 0
                while count < 5:
                print(count)
                count += 1
                # Output: 0 1 2 3 4

Resumo
    ->Tipos de Dados: Inteiros, flutuantes, strings, booleanos.
    ->Variáveis: Armazenam dados, criadas com atribuição usando =.
    ->Estruturas de Controle: if, elif, else para decisões condicionais.
    ->Loops: for para iterar sobre sequências; while para repetição baseada em uma condição.
    ->Sintaxe Básica: Indentação para definir blocos de código, comentários para anotações, declaração de variáveis sem ->necessidade de especificar tipo.