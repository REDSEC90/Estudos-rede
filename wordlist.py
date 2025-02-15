print("Desenvolvido por REDSEC90")

#!/usr/bin/env python3
import argparse
import itertools
import string
import sys

def gerar_wordlist(char_set, tamanho):
    """
    Gera todas as combinações de tamanho 'tamanho'
    a partir do conjunto de caracteres 'char_set'.
    """
    # Aviso: Para conjuntos grandes, o número total de combinações é (len(char_set))^tamanho.
    total = len(char_set) ** tamanho
    print(f"[INFO] Total de combinações: {total}")
    
    # Itera e gera cada combinação
    for combinacao in itertools.product(char_set, repeat=tamanho):
        yield ''.join(combinacao)

def main():
    parser = argparse.ArgumentParser(
        description="Gerador de wordlist baseado em permutações de caracteres."
    )
    # Definindo os argumentos de conjunto de caracteres
    parser.add_argument("-L", dest="lower", action="store_true",
                        help="Usar letras minúsculas (a-z)")
    parser.add_argument("-LL", dest="both", action="store_true",
                        help="Usar letras maiúsculas e minúsculas (A-Z + a-z)")
    parser.add_argument("-N", dest="numbers", action="store_true",
                        help="Usar números (0-9)")
    parser.add_argument("-C", dest="chars", action="store_true",
                        help="Usar caracteres especiais (p.ex.: !@#$...)")
    # Argumento posicional para o tamanho da wordlist (quantidade de caracteres por string)
    parser.add_argument("tamanho", type=int,
                        help="Número de caracteres para cada string gerada")

    args = parser.parse_args()

    # Construindo o conjunto de caracteres com base nas flags fornecidas
    conjunto = ""
    if args.both:
        conjunto += string.ascii_lowercase + string.ascii_uppercase
    elif args.lower:
        conjunto += string.ascii_lowercase

    if args.numbers:
        conjunto += string.digits

    if args.chars:
        conjunto += string.punctuation

    if not conjunto:
        parser.error("Nenhuma opção de conjunto de caracteres selecionada. Use -L, -LL, -N e/ou -C.")

    tamanho = args.tamanho

    # Aviso para o usuário se o número total de combinações for muito alto.
    total_combinacoes = len(conjunto) ** tamanho
    if total_combinacoes > 10**6:
        print(f"[AVISO] Você está prestes a gerar {total_combinacoes} combinações. Isso pode levar muito tempo e consumir muitos recursos.", file=sys.stderr)
        resposta = input("Deseja continuar? (s/n): ")
        if resposta.lower() not in ['s', 'sim']:
            sys.exit("Operação abortada.")

    # Gerando e imprimindo cada combinação
    for palavra in gerar_wordlist(conjunto, tamanho):
        print(palavra)

if __name__ == "__main__":
    main()
