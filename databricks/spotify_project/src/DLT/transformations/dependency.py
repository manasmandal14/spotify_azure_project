# Create Empty Stream Table
# Then Add Expectations to validate the data

dimuser_rules = {
    "rule_1": "user_id is not null",
    "rule_2": "user_name is not null"
}

import dlt

#When we have to apply rules across the empty streaming table.
dlt.create_streaming_table(
    name="streaming_table", comment="This is a streaming table",
    expect_all_or_drop=dimuser_rules
    )

@dlt.append_flow(target="streaming_table")
def streaming_table():
    return spark.readStream.table("spotify_catalogue.dev_schema.dimuser")

#################################################################
"""
Now we will see AUTO CDC which is basically a feature of Databricks Lakehouse where we do upsert
"""





