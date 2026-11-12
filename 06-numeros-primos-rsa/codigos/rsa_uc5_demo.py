"""Demonstração acadêmica do RSA para a UC5 — sem segurança criptográfica real.

Usa primos pequenos e RSA sem padding para facilitar a visualização.
Não utilizar para proteger informações verdadeiras.
"""


def main():
    print('=== UC5 - Criptografia Assimetrica: Demonstracao RSA ===')
    print('Algoritmo: RSA didatico (sem padding, inseguro para uso real)')

    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)

    print(f'Chave publica (n, e): ({n}, {e})')
    print(f'Chave privada (n, d): ({n}, {d})')

    mensagem = input('\nDigite uma mensagem de sua escolha: ')
    if not mensagem:
        print('Erro: a mensagem nao pode estar vazia.')
        return

    dados = mensagem.encode('utf-8')
    criptografada = [pow(byte, e, n) for byte in dados]
    recuperados = bytes(pow(bloco, d, n) for bloco in criptografada)
    descriptografada = recuperados.decode('utf-8')

    print(f'\nMensagem original: {mensagem}')
    print('Mensagem criptografada (blocos numericos):')
    print(criptografada)
    print(f'Mensagem descriptografada: {descriptografada}')
    print(f'Conferencia: {"SUCESSO" if descriptografada == mensagem else "FALHA"}')
    print('\nAVISO: exemplo matematico. Nao usar para proteger dados reais.')


if __name__ == '__main__':
    main()
