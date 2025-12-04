from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from src.database import Base

class ExameHistorico(Base):
    __tablename__ = "historico_exames"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, default=datetime.now)
    
    species = Column(String)  
    breed = Column(String)   
    age_range = Column(String)    
    
    hemacias = Column(Float)
    hemoglobina = Column(Float)
    hematocrito = Column(Float)
    leucocitos = Column(Float)
    plaquetas = Column(Float)
    
    glicose = Column(Float)
    ureia = Column(Float)
    creatinina = Column(Float)
    alt = Column(Float)
    ast = Column(Float)
    proteina_total = Column(Float)
    
    diagnostic_pattern = Column(String)
    confidence = Column(Float)          