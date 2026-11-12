import time
import math
import sys

def crivo_eratostenes(limite):
    # Uso de bytearray para economizar memória (1 byte por número)
    primos = bytearray([1]) * (limite + 1)
    primos[0] = primos[1] = 0
    p = 2
    while (p * p <= limite):
        if primos[p]:
            # Marcar múltiplos usando fatiamento (slice) é muito mais rápido em Python
            primos[p*p : limite+1 : p] = bytearray([0]) * len(range(p*p, limite+1, p))
        p += 1
    return primos

def fatorar(n):
    inicio = time.perf_counter()
    fatores = []
    d = 2
    temp_n = n
    # Tentativa de divisão básica
    while d * d <= temp_n:
        while (temp_n % d) == 0:
            fatores.append(d)
            temp_n //= d
        d += 1
    if temp_n > 1:
        fatores.append(temp_n)
    fim = time.perf_counter()
    return fatores, fim - inicio

# 1. Gerar os primos
LIMITE = 1000000000
print(f"Gerando crivo até {LIMITE:,} (isso pode levar alguns segundos)...".replace(',', '.'))
status_crivo = crivo_eratostenes(LIMITE)

# Extrair apenas uma amostra inicial para exibir (os primeiros 80 primos, por exemplo)
# Não extraímos 1 bilhão de números para uma lista para não travar a memória
print("\nExtraindo primeiros números para exibição...")
amostra_primos = [i for i, vivo in enumerate(status_crivo) if vivo][:80]

# 2. Mostrar a lista em 8 colunas
print("-" * 80)
print(f"EXEMPLO DOS PRIMEIROS NÚMEROS ENCONTRADOS (8 COLUNAS):")
print("-" * 80)
for i in range(0, len(amostra_primos), 8):
    linha = amostra_primos[i:i+8]
    print("".join(f"{num:10}" for num in linha))
print("-" * 80)

# Conta total de primos (opcional, pode demorar um pouco)
total_primos = status_crivo.count(1)
print(f"Total de números primos encontrados: {total_primos:,}".replace(',', '.'))

# 3. Entrada do usuário
try:
    print(f"\nEscolha índices entre 0 e {total_primos - 1}")
    idx1 = int(input("Digite o índice do primeiro número primo: "))
    idx2 = int(input("Digite o índice do segundo número primo: "))
    
    # Busca o n-ésimo primo no bytearray de forma eficiente
    def buscar_por_indice(target_idx, crivo):
        count = -1
        for num, vivo in enumerate(crivo):
            if vivo:
                count += 1
                if count == target_idx:
                    return num
    
    p = buscar_por_indice(idx1, status_crivo)
    q = buscar_por_indice(idx2, status_crivo)
    
    # MOSTRAR NÚMEROS SELECIONADOS IMEDIATAMENTE
    print(f"\n>>> NÚMEROS SELECIONADOS: P = {p} | Q = {q}")

    # 4. Multiplicação
    start_mul = time.perf_counter()
    n = p * q
    end_mul = time.perf_counter()
    tempo_mul = end_mul - start_mul

    print(f"\nResultado da multiplicação (Chave Pública N): {n}")
    print(f"Tempo de multiplicação: {tempo_mul:.10f} segundos")

    # 5. Fatoração (O "Ataque")
    print("\nIniciando fatoração (tentando quebrar a chave)...")
    fatores_encontrados, tempo_fato = fatorar(n)

    print(f"Fatores encontrados: {fatores_encontrados}")
    print(f"Tempo de fatoração: {tempo_fato:.10f} segundos")

    if tempo_mul > 0:
        proporcao = tempo_fato / tempo_mul
        print(f"\nA fatoração foi {proporcao:,.2f} vezes mais lenta que a multiplicação.".replace(',', 'X').replace('.', ',').replace('X', '.'))

except Exception as e:
    print(f"Erro: {e}")