class NormalizadorVeterinario:
    def __init__(self):
        self.tabela_referencia = {
            'canino': {
                'hemoglobina': {'min': 12.0, 'max': 18.0},
                'creatinina': {'min': 0.5, 'max': 1.5},
                'ureia': {'min': 20.0, 'max': 50.0},
                'alt': {'min': 20.0, 'max': 80.0},
                'glicose': {'min': 65.0, 'max': 110.0},
                'proteinas': {'min': 5.5, 'max': 7.5}  
            },
            'felino': {
                'hemoglobina': {'min': 8.0, 'max': 15.0},
                'creatinina': {'min': 0.8, 'max': 2.4},
                'ureia': {'min': 30.0, 'max': 60.0},
                'alt': {'min': 25.0, 'max': 100.0},
                'glicose': {'min': 70.0, 'max': 150.0},
                'proteinas': {'min': 6.0, 'max': 8.0}   
            }
        }

    def obter_referencia(self, especie, parametro):
        try:
            return self.tabela_referencia[especie.lower()][parametro.lower()]
        except KeyError:
            return None

    def verificar_normalidade(self, especie, parametro, valor):
        ref = self.obter_referencia(especie, parametro)
        if not ref:
            return "Referência não encontrada"
        
        if valor < ref['min']: return "Baixo"
        elif valor > ref['max']: return "Alto"
        return "Normal"