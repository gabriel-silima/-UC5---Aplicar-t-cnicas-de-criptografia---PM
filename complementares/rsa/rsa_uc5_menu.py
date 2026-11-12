"""UC5 — Laboratório RSA com menu interativo.

Evolução do rsa_uc5_demo.py. Usa os mesmos primos e expoentes fixos.
Modelo matemático de RSA sem padding: NÃO protege dados reais.
Requer Python 3.9+; utiliza apenas a biblioteca padrão.
"""

P = 61
Q = 53
N = P * Q
PHI = (P - 1) * (Q - 1)
E = 17
D = pow(E, -1, PHI)


def mostrar_chaves():
    """Exibe parâmetros do exemplo. A chave privada é só para laboratório."""
    print("\n--- Chaves RSA didáticas ---")
    print(f"Primos: P={P}; Q={Q}")
    print(f"N = P x Q = {N}")
    print(f"Chave publica (N, e): ({N}, {E})")
    print(f"Chave privada (N, d): ({N}, {D})")


def criptografar(mensagem):
    """Converte o texto em bytes UTF-8 e cifra cada byte isoladamente."""
    dados = mensagem.encode("utf-8")
    if not dados:
        raise ValueError("A mensagem nao pode estar vazia.")
    if len(dados) > 4096:
        raise ValueError("Use uma mensagem de ate 4096 bytes neste laboratorio.")
    return [pow(byte, E, N) for byte in dados]


def descriptografar(blocos):
    """Recupera os bytes e decodifica UTF-8."""
    if not blocos:
        raise ValueError("A lista de blocos nao pode estar vazia.")
    if len(blocos) > 4096:
        raise ValueError("Limite de 4096 blocos por demonstracao.")
    if any(not isinstance(bloco, int) or isinstance(bloco, bool) or not 0 <= bloco < N for bloco in blocos):
        raise ValueError(f"Cada bloco deve ser um inteiro entre 0 e {N - 1}.")

    recuperados = [pow(bloco, D, N) for bloco in blocos]
    if any(byte > 255 for byte in recuperados):
        raise ValueError("Esses blocos nao representam bytes de uma mensagem UTF-8 valida.")
    try:
        return bytes(recuperados).decode("utf-8")
    except UnicodeDecodeError as erro:
        raise ValueError("Os blocos nao formam texto UTF-8 valido.") from erro


def interpretar_blocos(texto):
    """Aceita: 1759, 1313, 1369  ou  [1759, 1313, 1369]."""
    texto = texto.strip()
    tem_inicio = texto.startswith("[")
    tem_fim = texto.endswith("]")
    if tem_inicio != tem_fim:
        raise ValueError("Use os colchetes completos ou remova os dois.")
    if tem_inicio:
        texto = texto[1:-1].strip()
    partes = [parte.strip() for parte in texto.split(",")]
    if not texto or any(not parte.isdecimal() for parte in partes):
        raise ValueError("Digite numeros inteiros separados por virgula.")
    if len(partes) > 4096:
        raise ValueError("Limite de 4096 blocos por demonstracao.")
    return [int(parte) for parte in partes]


def executar_criptografia():
    mensagem = input("\nDigite a mensagem para criptografar: ")
    blocos = criptografar(mensagem)
    print(f"Mensagem original: {mensagem}")
    print("Mensagem criptografada (copie os blocos para a opcao 2):")
    print(blocos)


def executar_descriptografia():
    print("\nCole os blocos gerados na opcao 1, separados por virgula.")
    texto = input("Blocos criptografados: ")
    blocos = interpretar_blocos(texto)
    mensagem = descriptografar(blocos)
    print(f"Mensagem descriptografada: {mensagem}")


def testar_ciclo_completo():
    mensagem = input("\nDigite a mensagem para testar o ciclo completo: ")
    blocos = criptografar(mensagem)
    recuperada = descriptografar(blocos)
    mostrar_chaves()
    print(f"\nMensagem original: {mensagem}")
    print(f"Mensagem criptografada (blocos numericos): {blocos}")
    print(f"Mensagem descriptografada: {recuperada}")
    print(f"Conferencia: {'SUCESSO' if recuperada == mensagem else 'FALHA'}")


def main():
    print("=== UC5 - Laboratorio RSA com menu ===")
    print("AVISO: RSA didatico sem padding. Nao usar para proteger dados reais.")
    while True:
        print("\n========== MENU ==========")
        print("1 - Criptografar mensagem")
        print("2 - Descriptografar blocos")
        print("3 - Visualizar chaves RSA")
        print("4 - Testar ciclo completo")
        print("0 - Sair")
        try:
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "0":
                print("Laboratorio encerrado.")
                break
            elif opcao == "1":
                executar_criptografia()
            elif opcao == "2":
                executar_descriptografia()
            elif opcao == "3":
                mostrar_chaves()
            elif opcao == "4":
                testar_ciclo_completo()
            else:
                print("Opcao invalida. Escolha 0, 1, 2, 3 ou 4.")
        except ValueError as erro:
            print(f"ERRO: {erro}")
        except (KeyboardInterrupt, EOFError):
            print("\nLaboratorio encerrado.")
            break


if __name__ == "__main__":
    main()
