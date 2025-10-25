# Conversor de Bases

Primeiro projeto (ou melhor, lista de exercícios) da disciplina de Introdução a Computação do Bacharelado em Ciência da Computação na UFLA ministrada pelo Doutor Rafael Serapilha Durelli.

Um conversor de número de uma base qualquer entre 2 a 36 para outra base qualquer junto com outros conversores e exercícios relacionados.

## Uso 

O programa foi oficialmente testado na versão 3.11.0 de Python, sem bibliotecas instaladas por meio do [pip](https://pypi.org/project/pip/).

Cada exercício está separado por arquivos, seguindo o padrão `ex{número do exercício}.py`.

Em cada um deles há as funções principais pedidas e uma função para testar o funcionamento de cada função principal.

Executar diretamente o arquivo do exercício com o interpretador Python faz com que ele rode os casos de testes pré-definidos para verificar se a função está funcionando corretamente.

Para usar alguma função específica, importe do arquivo do exercício que ela foi exigida.

### Exemplo com o Exercício 4 (conversão de octal para decimal)

```py
from ex004 import oct_to_dec

print(oct_to_dec('127')) # 87
```

Foram feitas duas questões bônus, `b1.py` e `b2.py`. A primeira sendo uma adaptação da função principal de `ex007.py`, que agora suporta números fracionários, e a segunda implementando funções para o [complemento de dois](https://pt.wikipedia.org/wiki/Complemento_para_dois), para representar inteiros negativos em largura fixa.

## Autores

Turma: 10A

Semestre: 2025/2

- Cristian Lima Vilela
- Yuri Carvalho Alonso