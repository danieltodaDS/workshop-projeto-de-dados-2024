import pandas as pd
from contratos import Vendas
from dotenv import load_dotenv
import os

def process_excel (uploaded_file): 
    try: 
        df = pd.read_excel(uploaded_file)
        erros = []
        # Verifica se ha colunas extras no Dataframe
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        
        if extra_cols: 
            return False, f"Colunas extras detectadas no excel: {','.join(extra_cols)}"

        for index, row in df.iterrows(): 
            try: 
                _ = Vendas(**row.to_dict())
            except: 
                erros.append(f'Erro na linha {index + 2}: {e}')
        
        # Retorna resultado da validacao, erros e o Dataframe
        return True, erros
    
    except Exception as e: 
        # Se houver exceção, retorna o erro e um Dataframe vazio 
        return pd.DataFrame(), f'Erro inesperado: {str(e)}'