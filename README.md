#  Compilador SIMPLE → SML (Simpletron)

Este projeto implementa um **compilador que traduz programas escritos na linguagem SIMPLE para a Simpletron Machine Language (SML)**, permitindo que programas de alto nível sejam executados em uma máquina virtual chamada **Simpletron**.

---

##  Visão Geral

- **SIMPLE**: linguagem de programação simples, de alto nível, inspirada em versões iniciais do BASIC.
- **SML (Simpletron Machine Language)**: linguagem de máquina entendida diretamente pelo Simpletron.
- O compilador realiza a **tradução de código SIMPLE para SML**, respeitando regras sintáticas e semânticas da linguagem.

---

##  Modo de Uso

Este compilador recebe um programa escrito na linguagem **SIMPLE** como entrada e gera, como saída, o código equivalente em **Simpletron Machine Language (SML)**.

###  Entrada

- Arquivo de texto contendo um programa válido na linguagem **SIMPLE**
- As instruções devem estar numeradas em ordem crescente
- Apenas letras minúsculas são permitidas

###  Saída

- Código gerado em **SML**, pronto para ser carregado e executado no Simpletron
- Cada instrução ocupa uma palavra de memória

---

###  Como executar o compilador

1. Certifique-se de ter a linguagem utilizada no projeto instalada  
   (Python)

2. Execute o programa principal do compilador:


python simple_to_sml.py

---

##  Linguagem de Programação SIMPLE

A linguagem **SIMPLE** é composta por instruções numeradas em **ordem crescente**, onde cada linha contém um comando da linguagem.

###  Características principais

- Apenas **letras minúsculas** são permitidas  
- Variáveis:
  - Possuem **apenas uma letra**
  - São do tipo **inteiro**
  - Não precisam ser declaradas (inicializadas automaticamente com zero)
- Expressões aritméticas inteiras com os operadores:
  - `+` adição
  - `-` subtração
  - `*` multiplicação
  - `/` divisão inteira
  - `%` resto da divisão
- Controle de fluxo feito exclusivamente com `goto` e `if/goto`

---

###  Comandos da linguagem SIMPLE

| Comando    | Descrição |
|------------|----------|
| `rem`      | Comentário (ignorado pelo compilador) |
| `input`    | Lê um valor inteiro do teclado |
| `let`      | Atribuição de expressão aritmética |
| `print`    | Exibe o valor de uma variável |
| `goto`     | Desvia a execução para uma linha |
| `if/goto`  | Desvio condicional |
| `end`      | Finaliza o programa |

---

### Operadores relacionais (if/goto)

>   maior que
>=  maior ou igual
<   menor que
<=  menor ou igual
==  igual
!=  diferente

---

### Simpletron Machine Language (SML)

O Simpletron é uma máquina virtual simples, porém poderosa, que executa programas escritos em SML.

# Estrutura do Simpletron

Memória: 100 palavras (00 a 99)

Palavra:
Número decimal de 4 dígitos com sinal
Ex: +3364, -0001

Acumulador:
Registrador especial usado em operações aritméticas e lógicas
O programa sempre inicia na posição 00 da memória

# Instruções SML

Cada instrução SML ocupa uma palavra de memória e possui:

2 primeiros dígitos → código de operação
2 últimos dígitos → endereço de memória

## Códigos de Operação da SML

Operações de Entrada e Saída

| Código	| Operação	| Descrição |
|-----------|-----------|-----------|
|10	| READ	| Lê uma palavra do teclado|
|11	| WRITE	| Escreve uma palavra na tela|

Operações de Carga e Armazenamento
| Código	| Operação	| Descrição |
|-----------|-----------|-----------|
|  20	|  LOAD	| Carrega valor da memória no acumulador|
| 21	| STORE	| Armazena o valor do acumulador na memória|

Operações Aritméticas
| Código	| Operação	| Descrição |
|-----------|-----------|-----------|
| 30	| ADD	| Soma uma palavra da memória ao acumulador|
| 31	| SUBTRACT	| Subtrai uma palavra da memória do acumulador|
| 32	| DIVIDE	| Divide o acumulador por uma palavra da memória|
| 33	| MULTIPLY	| Multiplica uma palavra da memória pelo acumulador|
| 34	| MODULE	| Calcula o resto da divisão|

### Operações de Controle de Fluxo

Operações Aritméticas
| Código	| Operação	| Descrição |
|-----------|-----------|-----------|
| 40	| BRANCH	| Desvio incondicional para um endereço de memória|
| 41	| BRANCHNEG	| Desvio se o acumulador for negativo|
| 42	| BRANCHZERO	| Desvio se o acumulador for zero|
| 43	| HALT	| Finaliza a execução do programa|

### Objetivo do Projeto

Estudar compiladores e tradução de linguagens
Entender a relação entre linguagem de alto nível e linguagem de máquina
Simular a execução de programas em uma máquina virtual
Aplicar conceitos de:
Análise léxica
Tradução de instruções
Organização de memória

# Contexto Acadêmico

Este projeto é inspirado em exercícios clássicos de Compiladores e Arquitetura de Computadores, utilizando o modelo do Simpletron como base didática.

# Licença

Projeto destinado a fins educacionais e de estudo.

##  Referências

- [Linguagem de Programação SIMPLE](http://www.ybadoo.com.br/tutoriais/cmp/11/)
- [Simpletron Machine Language (SML)](http://www.ybadoo.com.br/tutoriais/cmp/10/)

# Autor 

Bruno Lopes Bellinazo