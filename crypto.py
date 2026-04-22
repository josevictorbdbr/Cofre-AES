import os
import hashlib
from aes import cifrar_bloco, decifrar_bloco, xor_bytes


#Gera a chave a partir da senha
def derivar_chave(senha: str, salt: bytes, iteracoes: int = 100_000) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', senha.encode('utf-8'), salt, iteracoes, dklen=32)


def pad(dados: bytes, tamanho_bloco: int = 16) -> bytes:
    faltando = tamanho_bloco - (len(dados) % tamanho_bloco)
    return dados + bytes([faltando] * faltando)


def unpad(dados: bytes) -> bytes:
    valor = dados[-1]
    if valor < 1 or valor > 16:
        raise ValueError('Padding invalido')
    return dados[:-valor]


#Cifra os blocos encadeando um com o outro
def cifrar_cbc(conteudo: bytes, chave: bytes, iv: bytes) -> bytes:
    resultado = bytearray()
    anterior = iv

    for indice in range(0, len(conteudo), 16):
        bloco = conteudo[indice:indice + 16]

        combinado = xor_bytes(bloco, anterior)
        bloco_cifrado = cifrar_bloco(combinado, chave)

        resultado.extend(bloco_cifrado)
        anterior = bloco_cifrado

    return bytes(resultado)


#Desfaz o encadeamento
def decifrar_cbc(dados_cifrados: bytes, chave: bytes, iv: bytes) -> bytes:
    resultado = bytearray()
    anterior = iv

    for indice in range(0, len(dados_cifrados), 16):
        bloco = dados_cifrados[indice:indice + 16]
        bloco_decifrado = decifrar_bloco(bloco, chave)
        original = xor_bytes(bloco_decifrado, anterior)

        resultado.extend(original)
        anterior = bloco

    return unpad(bytes(resultado))


def cifrar_arquivo(caminho: str, senha: str) -> None:
    with open(caminho, 'rb') as arquivo:
        conteudo = arquivo.read()

    salt = os.urandom(16)
    iv = os.urandom(16)
    chave = derivar_chave(senha, salt)

    conteudo_preenchido = pad(conteudo)
    cifrado = cifrar_cbc(conteudo_preenchido, chave, iv)

    saida = caminho + '.cifrado'
    with open(saida, 'wb') as arquivo:
        arquivo.write(salt + iv + cifrado)

    print(f'Arquivo salvo como: {saida}')


def decifrar_arquivo(caminho: str, senha: str) -> str:
    with open(caminho, 'rb') as arquivo:
        dados = arquivo.read()

    if len(dados) < 32:
        raise ValueError('ERRO: Arquivo corrompido ou invalido')

    salt = dados[:16]
    iv = dados[16:32]
    conteudo_cifrado = dados[32:]
    chave = derivar_chave(senha, salt)

    try:
        original = decifrar_cbc(conteudo_cifrado, chave, iv)
    except Exception as erro:
        raise ValueError('ERRO: Senha errada ou dados corrompidos') from erro

    return original.decode('utf-8')