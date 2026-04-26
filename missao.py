class Missao:
    """
    Classe base para representar uma missão genérica.
    Atributos:
    - nome: O nome da missão.
    - recompensa: A recompensa associada à missão.
    - concluida: Um booleano indicando se a missão foi concluída.
    Métodos:
    - concluir(): Marca a missão como concluída.
    - obter_recompensa(): Retorna a recompensa associada à missão, se ela foi concluída.
    - __str__(): Retorna uma representação string da missão.
    """
    def __init__(self, nome = '<não informado>'):
        self.nome = nome
        self.concluida = False
    
    def concluir(self):
        self.concluida = True

    def obter_recompensa(self):
        if self.concluida:
            return 50
        return 0
    
    def __str__(self):
        status = 'X' if self.concluida else ' '
        return f'[{status}] {self.nome} - Recompensa: {self.obter_recompensa()}'


class MissaoCombate(Missao):
    """
    Classe derivada de Missao para representar uma missão de combate.
    Atributos adicionais:
    - inimigo: O inimigo que deve ser derrotado.
    Métodos adicionais:
    - obter_recompensa(): Retorna uma recompensa maior se a missão de combate for concluída.
    - __str__(): Retorna uma representação string da missão de combate, incluindo o inimigo.
    """
    def __init__(self, nome = '<não informado>', inimigo = '<não informado>'):
        super().__init__(nome)
        self.inimigo = inimigo
    
    def obter_recompensa(self):
        if self.concluida:
            return 100
        return 0
    
    def __str__(self):
        base = super().__str__()
        return f'{base} | Inimigo: {self.inimigo}'


class MissaoExploracao(Missao):
    """
    Classe derivada de Missao para representar uma missão de exploração.
    Atributos adicionais:
    - local: O local que deve ser explorado.
    Métodos adicionais:
    - obter_recompensa(): Retorna uma recompensa maior se a missão de exploração for concluída.
    - __str__(): Retorna uma representação string da missão de exploração, incluindo o local.
    """
    def __init__(self, nome = '<não informado>', local = '<não informado>'):
        super().__init__(nome)
        self.local = local
    
    def obter_recompensa(self):
        if self.concluida:
            return 75
        return 0
    
    def __str__(self):
        base = super().__str__()
        return f'{base} | Local: {self.local}'
