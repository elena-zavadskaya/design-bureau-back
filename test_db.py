import os
import dj_database_url

url = os.environ.get("DATABASE_URL")
print("DATABASE_URL:", repr(url))

config = dj_database_url.parse(url, conn_max_age=600, ssl_require=True)
print(config)
