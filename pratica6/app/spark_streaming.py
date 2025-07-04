from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnull
from pyspark.sql.types import StructType, StringType, DoubleType, LongType # Importe os tipos necessários

spark = SparkSession.builder \
    .appName("IoT Data Processing") \
    .config("spark.sql.parquet.compression.codec", "snappy") \
    .getOrCreate()

# Configurações de diretório
input_dir = "/data_input"
output_dir = "/data_lake/sensores"

# -------------------------------------------------------------------
# NOVO: Defina o schema explícito para seus dados
schema = StructType() \
    .add("tipo", StringType(), True) \
    .add("cidade", StringType(), True) \
    .add("no2", StringType(), True) \
    .add("noise", StringType(), True) \
    .add("pm25", StringType(), True) \
    .add("pressao", LongType(), True) \
    .add("temp", DoubleType(), True) \
    .add("timestamp", StringType(), True) \
    .add("umidade", LongType(), True)
# -------------------------------------------------------------------

# Processamento principal
def process_data():
    # Lê todos os dados com schema unificado
    # AGORA USAMOS O SCHEMA DEFINIDO ACIMA
    df = spark.read.json(input_dir, multiLine=True, schema=schema) # Adicione schema=schema

    # Mostra schema para debug
    print("Schema dos dados:")
    df.printSchema()

    # Filtros específicos para cada tipo de dado
    df_filtrado = df.filter(
        ((col("tipo") == "clima") & (col("temp").isNotNull()) & (col("temp") > 20)) |
        ((col("tipo") == "smartcitizen") & (col("noise").isNotNull()) & (col("noise").cast("int") > 50))
    )

    # Mostra estatísticas
    print(f"Total de registros: {df.count()}")
    print(f"Registros filtrados: {df_filtrado.count()}")

    # Escreve resultados
    df_filtrado.write.mode("append") \
        .partitionBy("cidade") \
        .parquet(f"file://{output_dir}")

    # Mostra resultados (apenas se houver dados filtrados)
    print("Dados filtrados:")
    df_filtrado.show(truncate=False)

if __name__ == "__main__":
    while True:
        process_data()
        spark.streams.awaitAnyTermination(timeout=30)