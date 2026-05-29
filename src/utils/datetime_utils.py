
from pyspark.sql.functions import to_date

def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    return df.withColumn(output_col, to_date(timestamp_col))