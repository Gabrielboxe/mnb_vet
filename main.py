from src.utils import gerar_dataset_simulado
from src.modelo_ia import ModeloDiagnostico
from src.normalizacao import NormalizadorVeterinario
import os

def main():
    if not os.path.exists('models'):
        os.makedirs('models')

    print("--- INICIANDO MNB-Vet (Treinamento Melhorado) ---")
    
    print("\n[1/3] Gerando dataset sintético com correlação clínica...")
    df = gerar_dataset_simulado(qtd_linhas=2000)
    print(df.head())
    
    print("\n[2/3] Treinando Random Forest...")
    ia_vet = ModeloDiagnostico()
    ia_vet.treinar(df)
    
    if ia_vet.acuracia >= 0.80:
        print("\n[3/3] SUCESSO: Meta de >80% atingida!")
        ia_vet.salvar_modelo()
    else:
        print("\n[3/3] ALERTA: Modelo não atingiu a meta.")

if __name__ == "__main__":
    main()