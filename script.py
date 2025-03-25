import pandas as pd
import mysql.connector

# função que conecta ao banco de dados
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root", # usuário do banco de dados
        password="victorsg", # senha do usuário
        database="graos"
    )

# cria as tabelas se elas não existirem
def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_soja (
            id INT AUTO_INCREMENT PRIMARY KEY,
            estado VARCHAR(255),
            cidade VARCHAR(255),
            compra FLOAT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_milho (
            id INT AUTO_INCREMENT PRIMARY KEY,
            estado VARCHAR(255),
            cidade VARCHAR(255),
            compra FLOAT
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# funcao que insere os dados na tabela
def insert_data(sheet_name, table_name):
    # carrega a planilha
    df = pd.read_excel("Grao.xlsx", sheet_name=sheet_name)

    # na planilha temos valores vazios em "Estado", que serão preenchidos com o valor anterior
    df["Estado"].fillna(method='ffill', inplace=True)
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # insere os dados na tabela
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (estado, cidade, compra)
            VALUES (%s, %s, %s)
        """, (row["Estado"], row["Cidade"], row["Compra"]))
    
    # salva as alterações no banco de dados
    conn.commit()
    cursor.close()
    conn.close()

# função principal
def main():
    create_tables()
    insert_data("Soja", "tb_soja")
    insert_data("Milho", "tb_milho")
    print("Dados inseridos com sucesso!")

# chama a função principal quando o script é executado
if __name__ == "__main__":
    main()
