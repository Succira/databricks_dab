from pyspark.sql.functions import unix_timestamp, round

def get_trip_duration_mins(spark, df, start_col, end_col, output_col):

    return df.withColumn(
        output_col,
        round((unix_timestamp(end_col) - unix_timestamp(start_col)) / 60, 2)
    )