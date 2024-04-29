# Workshop 01 - 2024 - Projeto e processos de dados

## Jornada de dados - Luciano Galvao

### Instalacao e configuração

1. Clone o repositorio 
```bash 
git clone https://github.com/danieltodaDS/workshop-projeto-de-dados-2024.git
cd workshop-projeto-de-dados-2024
```
2. Configuração da versão do python com `pyenv`: 
```bash 
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Instale dependencias do projeto
```bash 
# Crie um ambiente virtual 
python -m venv .venv

# Ative o ambiente - Linux e Mac
source .venv/bin/activate

# Windows 
.venv\Scripts\Activate

# Instale as dependencias do projeto
pip install -r requirements.txt 
```