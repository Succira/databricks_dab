try:
    from databricks.connect import DatabricksSession
    spark = DatabricksSession.builder.getOrCreate()
    print("Using databricks connect ...")
except ImportError:
    try:
        from pyspark.sql import SparkSession

        spark = SparkSession.builder.getOrCreate()
        print("Using local SparkSession ...")
    except:
        print("Neither worked")

spark.sql("SHOW CATALOGS").show()

