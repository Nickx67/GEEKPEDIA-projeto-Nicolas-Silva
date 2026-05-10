class Node:

    def __init__(
        self,
        id,
        titulo,
        midia,
        genero,
        temas,
        publico_alvo,
        franquia
    ):

        self.id = id
        self.titulo = titulo
        self.midia = midia
        self.genero = genero
        self.temas = temas
        self.publico_alvo = publico_alvo
        self.franquia = franquia

    def __repr__(self):

        return f"{self.titulo}"