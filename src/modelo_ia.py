import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

class ModeloDiagnostico:
    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        self.le_especie = LabelEncoder()
        self.acuracia = 0.0
        self.report = ""

    def preparar_dados(self, df):
        df = df.copy()
        if 'especie' in df.columns:
            df['especie_encoded'] = self.le_especie.fit_transform(df['especie'])
        return df

    def treinar(self, df):
        print("Iniciando pré-processamento...")
        df_proc = self.preparar_dados(df)
        
        features = ['especie_encoded', 'idade_meses', 'hemoglobina', 'creatinina', 'ureia', 'alt', 'glicose', 'proteinas']
        target = 'diagnostico'
        
        X = df_proc[features]
        y = df_proc[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        print(f"Treinando com {len(X_train)} exemplos...")
        self.modelo.fit(X_train, y_train)
        
        y_pred = self.modelo.predict(X_test)
        self.acuracia = accuracy_score(y_test, y_pred)
        
        self.report = classification_report(y_test, y_pred, target_names=['Saudável', 'Anemia', 'Renal', 'Hepática'])
        
        print("-" * 30)
        print(f"Acurácia Global: {self.acuracia * 100:.2f}%")
        print("Relatório Detalhado:")
        print(self.report)
        print("-" * 30)

    def salvar_modelo(self, caminho='models/mnb_vet_model.pkl'):
        payload = {
            'modelo': self.modelo,
            'encoder': self.le_especie,
            'acuracia': self.acuracia,
            'features_esperadas': ['especie', 'idade', 'hemo', 'crea', 'ureia', 'alt', 'glicose', 'proteinas']
        }
        joblib.dump(payload, caminho)
        print(f"Modelo salvo com sucesso em: {caminho}")