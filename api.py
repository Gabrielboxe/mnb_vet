# Arquivo: api.py (Raiz do projeto)
import uvicorn
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from src.normalizacao import NormalizadorVeterinario

# Modelo de Entrada ATUALIZADO
class ExameInput(BaseModel):
    especie: str
    idade_meses: int
    hemoglobina: float
    creatinina: float
    ureia: float
    alt: float
    glicose: float    # Novo
    proteinas: float  # Novo

app = FastAPI(title="MNB-Vet API")

# Carregar lógica
norm = NormalizadorVeterinario()
dados_modelo = None
try:
    dados_modelo = joblib.load('models/mnb_vet_model.pkl')
    modelo_ia = dados_modelo['modelo']
    encoder_especie = dados_modelo['encoder']
except:
    print("ALERTA: Execute 'python main.py' para treinar o modelo novo.")

MAPA_DIAG = {0: 'Saudável', 1: 'Anemia', 2: 'Renal', 3: 'Hepática'}

@app.post("/diagnosticar")
def diagnosticar(exame: ExameInput):
    # 1. Normalização (Verificar todos os parâmetros)
    resultados_norm = []
    # Lista de campos para checar na tabela hash
    campos = ['hemoglobina', 'creatinina', 'ureia', 'alt', 'glicose', 'proteinas']
    
    # Pega os valores dinamicamente do objeto 'exame'
    for campo in campos:
        valor = getattr(exame, campo)
        status = norm.verificar_normalidade(exame.especie, campo, valor)
        resultados_norm.append({"parametro": campo, "valor": valor, "status": status})

    # 2. Inteligência Artificial
    if dados_modelo:
        esp_enc = encoder_especie.transform([exame.especie])[0]
        # Array com a ordem exata do treinamento
        feats = np.array([esp_enc, exame.idade_meses, exame.hemoglobina, 
                          exame.creatinina, exame.ureia, exame.alt, 
                          exame.glicose, exame.proteinas]).reshape(1, -1)
        
        pred = modelo_ia.predict(feats)[0]
        diag_texto = MAPA_DIAG.get(int(pred), "Outro")
    else:
        diag_texto = "Modelo não carregado"

    return {
        "paciente": {"especie": exame.especie, "idade": exame.idade_meses},
        "analise_parametros": resultados_norm,
        "diagnostico_sugerido": diag_texto
    }