from decouple import config
import psycopg2
from urllib.parse import urlparse
from decouple import config
import sys
sys.stdout.reconfigure(encoding="utf-8")

DATABASE_URL = config("DATABASE_URL")

print("DATABASE_URL:", DATABASE_URL)

try:
    url = urlparse(DATABASE_URL)

    conn = psycopg2.connect(
        dbname=url.path[1:],  # убираем первый /
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        sslmode="disable"  # попробуй и "require"
    )
    print("✅ Успешное подключение к базе!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)
    print("Len DATABASE_URL:", len(DATABASE_URL))
    print("Bytes:", list(DATABASE_URL.encode("utf-8")))



