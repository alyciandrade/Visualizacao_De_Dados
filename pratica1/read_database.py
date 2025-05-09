# read_database.py
import psycopg2
import pandas as pd
import os
import time

def read_postgres():
    try:
        conn = psycopg2.connect(
            host="db",
            database="meubanco",
            user="postgres",
            password="senha_segura"
        )
        print("\nDados do PostgreSQL:")
        df = pd.read_sql("SELECT * FROM usuarios", conn)
        print(df)
        conn.close()
    except Exception as e:
        print(f"Erro ao ler PostgreSQL: {e}")

def read_csv_files():
    csv_dir = "/usr/src/app/shared_data"
    try:
        files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        if files:
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(csv_dir, f)))
            print(f"\nLendo arquivo CSV mais recente: {latest_file}")
            df = pd.read_csv(os.path.join(csv_dir, latest_file))
            print(df.head())
        else:
            print("\nNenhum arquivo CSV encontrado ainda...")
    except Exception as e:
        print(f"Erro ao ler CSVs: {e}")

while True:
    read_postgres()
    read_csv_files()
    time.sleep(10)  # Verifica a cada 10 segundos