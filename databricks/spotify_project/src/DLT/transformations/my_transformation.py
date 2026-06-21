
# import dlt

# @dlt.table()
# def intermediate_table_silver_dimuser():
#     return spark.readStream.table("spotify_catalogue.dev_schema.dimuser")

# #Materlized view
# """
# Result of the query will be stored
# """
# @dlt.table()
# def intermediate_table_silver_dimuser_materlizedView():
#     return spark.read.table("spotify_catalogue.dev_schema.dimuser")


# @dlt.view()
# def intermediate_table_silver_dimuser_view():
#     return spark.read.table("spotify_catalogue.dev_schema.dimuser")



