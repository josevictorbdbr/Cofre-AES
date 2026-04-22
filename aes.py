#Tabela S-Box
sbox_hex = (
    '63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76'
    'ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0'
    'b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15'
    '04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75'
    '09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84'
    '53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf'
    'd0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8'
    '51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2'
    'cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73'
    '60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db'
    'e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79'
    'e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08'
    'ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a'
    '70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e'
    'e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df'
    '8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16'
).replace(' ', '')
S_BOX = bytearray.fromhex(sbox_hex)

#s-Box inversa
INV_S_BOX = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
]

#Aplica XOR byte a byte entre dois blocos
def xor_bytes(bloco_a: bytes, bloco_b: bytes) -> bytes:
    return bytes(valor_a ^ valor_b for valor_a, valor_b in zip(bloco_a, bloco_b))

#Separa bytes em grupos de 4
def dividir_em_palavras(dados: bytes):
    return [list(dados[i:i + 4]) for i in range(0, len(dados), 4)]

#Transforma 16 bytes em matriz 4x4
def montar_estado(dados: bytes):
    return [list(dados[i * 4:(i + 1) * 4]) for i in range(4)]

#Junta a matriz de volta em bytes
def estado_para_bytes(estado):
    return bytes(estado[0] + estado[1] + estado[2] + estado[3])

#Gira a palavra 1 lugar para a esquerda
def rotacionar_palavra(palavra):
    return palavra[1:] + palavra[:1]

#Troca os bytes da palavra
def substituir_palavra(palavra):
    return bytes(S_BOX[byte] for byte in palavra)

#Constante para a expansão da chave
def obter_rcon(i):
    tabela_rcon = bytearray.fromhex('01020408102040801836')
    return bytes([tabela_rcon[i - 1], 0, 0, 0])

#gera as chaves usadas em cada rodada
def expandir_chave(chave: bytes) -> list:
    quantidade_palavras = len(chave) // 4
    blocos_por_round = 4
    tamanho = len(chave) * 8

    if tamanho == 128:
        total_rounds = 10
    elif tamanho == 192:
        total_rounds = 12
    else:
        total_rounds = 14

    palavras = dividir_em_palavras(chave)

    for i in range(quantidade_palavras, blocos_por_round * (total_rounds + 1)):
        palavra_temp = palavras[i - 1][:]

        if i % quantidade_palavras == 0:
            palavra_temp = xor_bytes(
                substituir_palavra(rotacionar_palavra(palavra_temp)),
                obter_rcon(i // quantidade_palavras)
            )
        elif quantidade_palavras > 6 and i % quantidade_palavras == 4:
            palavra_temp = substituir_palavra(palavra_temp)

        nova_palavra = xor_bytes(bytes(palavras[i - quantidade_palavras]), bytes(palavra_temp))
        palavras.append(list(nova_palavra))

    chaves = []
    for i in range(0, len(palavras), 4):
        chaves.append([list(palavras[i + deslocamento]) for deslocamento in range(4)])

    return chaves

#Aplica XOR entre o estado e a chave da rodada
def adicionar_round_key(estado, chave_round):
    for linha in range(4):
        for coluna in range(4):
            estado[linha][coluna] ^= chave_round[linha][coluna]

def substituir_bytes(estado):
    for linha in range(4):
        for coluna in range(4):
            estado[linha][coluna] = S_BOX[estado[linha][coluna]]

def deslocar_linhas(estado):
    estado[0][1], estado[1][1], estado[2][1], estado[3][1] = estado[1][1], estado[2][1], estado[3][1], estado[0][1]
    estado[0][2], estado[1][2], estado[2][2], estado[3][2] = estado[2][2], estado[3][2], estado[0][2], estado[1][2]
    estado[0][3], estado[1][3], estado[2][3], estado[3][3] = estado[3][3], estado[0][3], estado[1][3], estado[2][3]

#Multiplicação usada no AES
def multiplicar_galois(valor_a, valor_b):
    resultado = 0
    for _ in range(8):
        if valor_b & 1:
            resultado ^= valor_a

        bit_alto = valor_a & 0x80
        valor_a <<= 1
        if bit_alto:
            valor_a ^= 0x1B

        valor_b >>= 1

    return resultado & 0xFF

def misturar_coluna(coluna):
    coluna_original = coluna[:]
    coluna[0] = multiplicar_galois(coluna_original[0], 2) ^ multiplicar_galois(coluna_original[1], 3) ^ coluna_original[2] ^ coluna_original[3]
    coluna[1] = coluna_original[0] ^ multiplicar_galois(coluna_original[1], 2) ^ multiplicar_galois(coluna_original[2], 3) ^ coluna_original[3]
    coluna[2] = coluna_original[0] ^ coluna_original[1] ^ multiplicar_galois(coluna_original[2], 2) ^ multiplicar_galois(coluna_original[3], 3)
    coluna[3] = multiplicar_galois(coluna_original[0], 3) ^ coluna_original[1] ^ coluna_original[2] ^ multiplicar_galois(coluna_original[3], 2)

def misturar_colunas(estado):
    for linha in range(4):
        misturar_coluna(estado[linha])

def substituir_bytes_inv(estado):
    for linha in range(4):
        for coluna in range(4):
            estado[linha][coluna] = INV_S_BOX[estado[linha][coluna]]

def deslocar_linhas_inv(estado):
    estado[0][1], estado[1][1], estado[2][1], estado[3][1] = estado[3][1], estado[0][1], estado[1][1], estado[2][1]
    estado[0][2], estado[1][2], estado[2][2], estado[3][2] = estado[2][2], estado[3][2], estado[0][2], estado[1][2]
    estado[0][3], estado[1][3], estado[2][3], estado[3][3] = estado[1][3], estado[2][3], estado[3][3], estado[0][3]

def misturar_coluna_inv(coluna):
    byte0, byte1, byte2, byte3 = coluna
    coluna[0] = multiplicar_galois(byte0, 0x0E) ^ multiplicar_galois(byte1, 0x0B) ^ multiplicar_galois(byte2, 0x0D) ^ multiplicar_galois(byte3, 0x09)
    coluna[1] = multiplicar_galois(byte0, 0x09) ^ multiplicar_galois(byte1, 0x0E) ^ multiplicar_galois(byte2, 0x0B) ^ multiplicar_galois(byte3, 0x0D)
    coluna[2] = multiplicar_galois(byte0, 0x0D) ^ multiplicar_galois(byte1, 0x09) ^ multiplicar_galois(byte2, 0x0E) ^ multiplicar_galois(byte3, 0x0B)
    coluna[3] = multiplicar_galois(byte0, 0x0B) ^ multiplicar_galois(byte1, 0x0D) ^ multiplicar_galois(byte2, 0x09) ^ multiplicar_galois(byte3, 0x0E)

def misturar_colunas_inv(estado):
    for linha in range(4):
        misturar_coluna_inv(estado[linha])

#Cifrar
def cifrar_bloco(bloco: bytes, chave: bytes) -> bytes:
    estado = montar_estado(bloco)
    chaves = expandir_chave(chave)
    ultimo_round = len(chaves) - 1

    adicionar_round_key(estado, chaves[0])

    for i_round in range(1, ultimo_round):
        substituir_bytes(estado)
        deslocar_linhas(estado)
        misturar_colunas(estado)
        adicionar_round_key(estado, chaves[i_round])

    substituir_bytes(estado)
    deslocar_linhas(estado)
    adicionar_round_key(estado, chaves[ultimo_round])

    return estado_para_bytes(estado)

#Decifrar
def decifrar_bloco(bloco: bytes, chave: bytes) -> bytes:
    estado = montar_estado(bloco)
    chaves = expandir_chave(chave)
    ultimo_round = len(chaves) - 1

    adicionar_round_key(estado, chaves[ultimo_round])
    deslocar_linhas_inv(estado)
    substituir_bytes_inv(estado)

    for i_round in range(ultimo_round - 1, 0, -1):
        adicionar_round_key(estado, chaves[i_round])
        misturar_colunas_inv(estado)
        deslocar_linhas_inv(estado)
        substituir_bytes_inv(estado)

    adicionar_round_key(estado, chaves[0])

    return estado_para_bytes(estado)