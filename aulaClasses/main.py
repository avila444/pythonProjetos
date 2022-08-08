def main():

    pass

    # Paradigmas da Computação:
    # Imperativo (C, C++): Manda - Obedece
    # Funcional (Haskell, LISP): Modela os problemas como funções matemáticas
    # Orientado à objetos (Java): Modela os problemas como funções objetos

    # Diferenças entre função e método:
    # Ambos são funções, porém funções não dependem de contexto, enquanto métodos dependem
    # Por exemplo, o método senta da classe cadeira só funciona se uma cadeira invocar o método

    # Diferenças entre variável e atributo:
    # Atributos são variáveis, porém são variáveis que dizem respeito ao contexto de uma classe
    # Os atributos de uma classe podem ser como no exemplo abaixo:
    # Número de pés, se tem encosto ou não, cor, material, etc.
    # Em outras palavras, um atributo é uma característica modelada de um objeto.

    def AulaClasses():

        class Cadeira(object):

            def __init__(self, material, pernas, encosto, cor):
                # Construtor: é o código chamado quando criamos um novo objeto classe cadeira
                # No construtor nós inicializamos os atributos de um objeto da classe cadeira

                self.material = material
                self.pernas = pernas
                self.encosto = encosto
                self.cor = cor

                # Para criar uma nova cadeira (com os parametros inicializados), usamos o construtor
                # como no código abaixo
                # nova_cadeira = Cadeira('Preta', 3, False, 'Couro')

            def senta(self, pessoa):
                pass
                #  Método é uma função que depende do contexto do objeto naquele momento.
                print(
                    pessoa,
                    "sentou em uma cadeira", self.cor, "de", self.pernas, "pernas"
                )

            def __str__(self):
                pass
                # Deve retornar uma string com todas as características da cadeira

                return "Esta cadeira é feita de {0}, tem {1} pernas, encosto = {2} e é da cor {3}".format(self.material,
                                                                                                          self.pernas,
                                                                                                          self.encosto,
                                                                                                          self.cor)

            def quebra(self):
                # Quebra 1 perna da cadeira (perna - 1)
                if self.pernas > 0:
                    pernas = (self.pernas - 1)

                return pernas

# def CadeiraImperativo(material: str, pernas: int, encosto: bool, cor: str):
#
#         dicionario = {
#             'Material': material,
#             'Pernas': pernas,
#             'Encosto': encosto,
#             'Cor': cor
#         }
#
#         return dicionario


if __name__ == "__main__":
    main()
