from huffman import Huffman

if __name__ == "__main__":
    texto = "{}{}{}{}{}{}{}{}{}".format(
        "E"*15, 'A'*14, 'O'*11, 'S'*10, 'R'*8, 'N'*7, 'I'*6, 'D'*5, 'T'*4)

    codificador = Huffman(texto)

    print(codificador.tablaCodigos)
    print(codificador.comprimir("TIENDADANESA"))
    print(codificador.graficar())
