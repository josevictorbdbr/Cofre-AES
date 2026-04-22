import sys
import os
from getpass import getpass
from crypto import cifrar_arquivo, decifrar_arquivo, cifrar_cbc
from aes import cifrar_bloco, decifrar_bloco


#Vetores para testar
TESTE_CHAVE = bytes.fromhex('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4')
TESTE_IV = bytes.fromhex('000102030405060708090a0b0c0d0e0f')
TESTE_PT = bytes.fromhex('6bc1bee22e409f96e93d7e117393172a')
TESTE_CT_ECB = bytes.fromhex('f3eed1bdb5d2a03c064b5a7e3db181f8')


def testar():
    print('Fazendo testes...')

    bloco_cifrado = cifrar_bloco(TESTE_PT, TESTE_CHAVE)
    if bloco_cifrado != TESTE_CT_ECB:
        print('FALHA na cifragem do bloco')
        return False

    bloco_decifrado = decifrar_bloco(TESTE_CT_ECB, TESTE_CHAVE)
    if bloco_decifrado != TESTE_PT:
        print('FALHA na decifragem do bloco')
        return False

    #No primeiro bloco do CBC o texto ainda passa pelo XOR com o IV
    texto_com_iv = bytes(byte_texto ^ byte_iv for byte_texto, byte_iv in zip(TESTE_PT, TESTE_IV))
    esperado_cbc = cifrar_bloco(texto_com_iv, TESTE_CHAVE)
    gerado_cbc = cifrar_cbc(TESTE_PT, TESTE_CHAVE, TESTE_IV)

    if gerado_cbc != esperado_cbc:
        print('FALHA no teste do CBC')
        return False

    print('SUCESSO nos testes')
    return True


def main():
    if len(sys.argv) < 2:
        print('\nDigite um dos comandos abaixo para usar:\n')
        print('  python main.py cifrar <nome do arquivo.txt>')
        print('  python main.py decifrar <nome do arquivo.txt.cifrado>')
        print('  python main.py testar\n\n')
        sys.exit(1)

    comando = sys.argv[1]

    if comando == 'cifrar':
        if len(sys.argv) != 3:
            print('Informe o nome do arquivo')
            sys.exit(1)

        caminho = sys.argv[2]
        if not os.path.exists(caminho):
            print(f"ERRO: Arquivo '{caminho}' não encontrado")
            sys.exit(1)

        senha = getpass('Senha: ')
        cifrar_arquivo(caminho, senha)
        return

    if comando == 'decifrar':
        if len(sys.argv) != 3:
            print('Informe o nome do arquivo .cifrado')
            sys.exit(1)

        caminho = sys.argv[2]
        if not caminho.endswith('.cifrado'):
            print("O arquivo não termina com '.cifrado'")

        if not os.path.exists(caminho):
            print(f"Arquivo '{caminho}' não encontrado")
            sys.exit(1)

        senha = getpass('Senha: ')
        
        try:
            conteudo_decifrado = decifrar_arquivo(caminho, senha)
            print('\nConteudo decifrado:')
            print(conteudo_decifrado, "\n")
        except Exception as erro:
            print(f'ERRO: {erro}')
            sys.exit(1)
        return

    if comando == 'testar':
        testes_ok = testar()
        sys.exit(0 if testes_ok else 1)

    print(f'Comando errado: {comando}')
    return


if __name__ == '__main__':
    main()