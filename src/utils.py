import pandas as pd
import numpy as np
import random

def gerar_dataset_simulado(qtd_linhas=3000):
    dados = []
    especies = ['canino', 'felino']
    
    
    for _ in range(qtd_linhas):
        especie = random.choice(especies)
        idade = random.randint(1, 180)
        diagnostico = random.choice([0, 1, 2, 3])
        
        hemo = random.uniform(12.0, 18.0)
        hemacias = random.uniform(5.5, 8.5)  
        hematocrito = random.uniform(37.0, 55.0)
        leucocitos = random.uniform(6000, 17000) 
        plaquetas = random.uniform(200000, 500000)
        
        crea = random.uniform(0.5, 1.5)
        ureia = random.uniform(20.0, 50.0)
        alt = random.uniform(20.0, 80.0)
        ast = random.uniform(20.0, 50.0)       
        glicose = random.uniform(70.0, 110.0)
        prot = random.uniform(6.0, 7.5)
        
        if diagnostico == 1:
            fator_queda = random.uniform(0.3, 0.7)
            hemo *= fator_queda
            hemacias *= fator_queda
            hematocrito *= fator_queda
            
        elif diagnostico == 2:
            crea = random.uniform(2.5, 10.0)
            ureia = random.uniform(80.0, 250.0)
            prot -= random.uniform(0.0, 1.5)

        elif diagnostico == 3:
            alt = random.uniform(200.0, 1200.0)
            ast = random.uniform(150.0, 800.0)
            prot -= random.uniform(1.0, 2.5)  
            glicose -= random.uniform(0.0, 30.0)

        glicose += np.random.normal(0, 2)
        
        dados.append([especie, idade, 
                      round(hemo,2), round(hemacias,2), round(hematocrito,2),
                      round(leucocitos,0), round(plaquetas,0),
                      round(crea,2), round(ureia,2), 
                      round(alt,2), round(ast,2), 
                      round(glicose,2), round(prot,2), 
                      diagnostico])
        
    cols = ['especie', 'idade_meses', 
            'hemoglobina', 'hemacias', 'hematocrito', 'leucocitos', 'plaquetas',
            'creatinina', 'ureia', 'alt', 'ast', 'glicose', 'proteinas', 
            'diagnostico']
    return pd.DataFrame(dados, columns=cols)