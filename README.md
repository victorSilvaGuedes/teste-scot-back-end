## Victor Silva Guedes

- sguedes.victor@gmail.com

- https://www.linkedin.com/in/victorsilvaguedes/

# Solução teste back-end Scot Consultoria

## Passo a passo para rodar a aplicação:
Este guia descreve o passo a passo para rodar a aplicação que insere dados de uma planilha Excel no banco de dados MySQL.

## Pré-requisitos
Antes de iniciar, certifique-se de que os seguintes softwares estão instalados:

1. **Python 3**: [Download Python](https://www.python.org/downloads/)
2. **MySQL Server**: [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **VS Code**: [Download VS Code](https://code.visualstudio.com/)
4. **Extensão Python para VS Code** (disponível no marketplace do VS Code)

## Passo a Passo

### 1. Clonar ou Criar o Projeto
Caso ainda não tenha o código no seu computador, crie um diretório e abra o VS Code nessa pasta.

```sh
mkdir meu_projeto
cd meu_projeto
code .
```

Se o código já estiver disponível, copie os arquivos para a pasta do projeto.

### 2. Instalar Dependências
No terminal do VS Code, execute:

```sh
pip install pandas mysql-connector-python openpyxl
```

### 3. Criar o Banco de Dados MySQL

1. Acesse o MySQL via terminal ou ferramenta gráfica (como MySQL Workbench).
2. Execute o seguinte comando para criar o banco de dados:

```sql
CREATE DATABASE graos;
```

### 4. Configurar a Conexão com o Banco de Dados
No arquivo Python, edite as credenciais de conexão se necessário:

```python
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="graos"
    )
```

### 5. Adicionar a Planilha `Grao.xlsx`
Coloque o arquivo `Grao.xlsx` na mesma pasta do código. Ele deve conter as abas `Soja` e `Milho`, com as colunas:
- **Estado**
- **Cidade**
- **Compra**

### 6. Executar o Script
No terminal do VS Code, execute:

```sh
python script.py
```

Se tudo estiver correto, você verá a mensagem:

```
Dados inseridos com sucesso!
```

Agora os dados da planilha foram inseridos no banco de dados MySQL.
