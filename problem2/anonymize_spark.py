from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws, col

def main():
    spark = SparkSession.builder \
        .appName("CSV Anonymization") \
        .getOrCreate()

    input_path = "large_dataset.csv"
    output_path = "anonymized_dataset"

    # Read CSV file
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Anonymize columns
    df_anonymized = df.withColumn("first_name", sha2(col("first_name"), 256)) \
                      .withColumn("last_name", sha2(col("last_name"), 256)) \
                      .withColumn("address", sha2(col("address"), 256))

    # Write anonymized data to CSV
    df_anonymized.write.csv(output_path, header=True, mode='overwrite')

    spark.stop()

if __name__ == '__main__':
    main()
