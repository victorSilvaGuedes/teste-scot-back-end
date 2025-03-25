import pandas as pd
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="victorsg",
        database="graos"
    )

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

def insert_data(sheet_name, table_name):
    df = pd.read_excel("Grao.xlsx", sheet_name=sheet_name)

    df["Estado"].fillna(method='ffill', inplace=True)
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (estado, cidade, compra)
            VALUES (%s, %s, %s)
        """, (row["Estado"], row["Cidade"], row["Compra"]))
    
    conn.commit()
    cursor.close()
    conn.close()

def main():
    create_tables()
    insert_data("Soja", "tb_soja")
    insert_data("Milho", "tb_milho")
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    main()
