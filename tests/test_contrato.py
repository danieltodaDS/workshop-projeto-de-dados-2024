
from datetime import datetime
import pytest
from src.contratos import Vendas
from pydantic import ValidationError

def test_vendas_com_dados_validos (): 
    
    dados_validos = {
        'email': 'comprador@email.com', 
        'data': datetime.now(),
        'valor': 100.50, 
        'produto': 'produto x',
        'quantidade': 3,  
        'categoria': 'categoria3'
    }

    venda = Vendas (**dados_validos)

    assert venda.email == dados_validos['email']
    assert venda.data == dados_validos['data']
    assert venda.valor == dados_validos['valor']
    assert venda.produto == dados_validos['produto']
    assert venda.quantidade == dados_validos['quantidade']
    assert venda.categoria == dados_validos['categoria']

def teste_vendas_dados_invalidos(): 

    dados_invalidos = {
        'email': 'comprador', 
        'data': 'nao é data',
        'valor': -100, 
        'produto': '',
        'quantidade': -3,  
        'categoria': '-categoria31'
        }
    
    # venda1 = Vendas(**dados_invalidos)

    # assert venda1.email == dados_invalidos['email']
    # assert venda1.data == dados_invalidos['data']
    # assert venda1.valor == dados_invalidos['valor']
    # assert venda1.produto == dados_invalidos['produto']
    # assert venda1.quantidade == dados_invalidos['quantidade']
    # assert venda1.categoria == dados_invalidos['categoria']

    with pytest.raises(ValidationError): 
        Vendas(**dados_invalidos)



def teste_validacao_categoria(): 

    dados_invalidos2 = {
        'email': 'comprador', 
        'data': 'nao é data',
        'valor': '-100', 
        'produto': '',
        'quantidade': -3,  
        'categoria': '-categoria31'
        }
    
    with pytest.raises(ValidationError): 
        Vendas(**dados_invalidos2)