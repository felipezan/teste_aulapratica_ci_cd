# Geral
Este repositório contém o programa e os testes desenvolvidos para a aula prática 5 e 6 da disciplina de Testes de Software na UFMG

## Calculadora de Áreas

Este é um projeto Python que calcula a área de diferentes formas geométricas: círculos, quadrados e retângulos. O projeto é acompanhado de testes de unidade e está configurado para ser testado automaticamente utilizando em três sistemas operacionais (Ubuntu, MacOS e Windows) através do GitHub Actions

## Programa base

O arquivo `calculadora_areas.py` contém a classe `CalculadoraDeAreas` com métodos para calcular a área de um círculo, quadrado e retângulo.

## Arquivo de Testes

Os testes de unidade são escritos no arquivo `tests/test_calculadora_de_areas.py`.

## Configuração do GitHub Actions

Este projeto está configurado para executar os testes de unidade automaticamente a cada commit, push e pull request usando GitHub Actions. O arquivo de configuração do GitHub Actions está localizado em `.github/workflows/python-app.yml`.

## Como Executar Localmente o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/felipezan/teste_aulapratica_ci_cd.git
    cd teste_aulapratica_ci_cd
    ```

2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate # se for windows use `venv\Scripts\activate`
    ```
3. Execute os testes:
    ```bash
    python -m unittest discover -s tests
    ```
