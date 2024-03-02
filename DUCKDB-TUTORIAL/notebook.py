# %%
import pandas as pd
import glob
import time
import duckdb
# %%
conn = duckdb.connect()
# %%
cur_time = time.time()
df = conn.execute("""
			 SELECT *
			 FROM read_csv_auto('dataset/*.csv', header=True)
			 LIMIT 10
			""").df()
print(f"time: {(time.time() - cur_time)}")
print(df)
# %%
conn.register("df_view", df)
conn.execute("DESCRIBE df_view").df()
# %%
