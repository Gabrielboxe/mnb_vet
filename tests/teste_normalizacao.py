import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.normalizacao import NormalizadorVeterinario

class TestNormalizadorVeterinario(unittest.TestCase):
    
    def setUp(self):
        self.norm = NormalizadorVeterinario()

    def test_busca_referencia_canino_sucesso(self):
        ref = self.norm.obter_referencia('canino', 'hemoglobina')
        self.assertIsNotNone(ref)
        self.assertEqual(ref['min'], 13.1)
        self.assertEqual(ref['max'], 20.5)

    def test_classificacao_valores(self):
        
        resultado_baixo = self.norm.verificar_normalidade('canino', 'hemoglobina', 10.0)
        self.assertEqual(resultado_baixo, "Baixo")

        resultado_normal = self.norm.verificar_normalidade('canino', 'hemoglobina', 15.0)
        self.assertEqual(resultado_normal, "Normal")

        resultado_alto = self.norm.verificar_normalidade('canino', 'hemoglobina', 22.0)
        self.assertEqual(resultado_alto, "Alto")

    def test_especie_inexistente(self):
        ref = self.norm.obter_referencia('dragao', 'fogo')
        self.assertIsNone(ref)
        resultado = self.norm.verificar_normalidade('dragao', 'fogo', 100)
        self.assertEqual(resultado, "Referência não encontrada")

if __name__ == '__main__':
    unittest.main()