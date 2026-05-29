import os, sys
import pytest

sys.path.append(os.getcwd())


@pytest.fixture(scope='package')
def spark():
    """Provide a SparkSession fixture for tests.
    """
    # return DatabricksSession.builder.getOrCreate()

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
    yield spark
    spark.stop()