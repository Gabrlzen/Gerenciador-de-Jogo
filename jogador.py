class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.xp = 0
        self.nivel = 1
        self.xp_maximo = 100
    
    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        # Verifica se o jogador subiu de nível
        while self.xp >= self.xp_maximo:
            self.xp -= self.xp_maximo
            self.nivel += 1
            self.xp_maximo *= 1.5
        
        
    def __str__(self):
        return f'Jogador: {self.nome} | XP: {self.xp} | Nível: {self.nivel}'

