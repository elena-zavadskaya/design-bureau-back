import os
import psycopg2
import dj_database_url

def test_connection():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        print("❌ Переменная окружения DATABASE_URL не найдена.")
        return

    print("DATABASE_URL:", database_url)

    try:
        # Парсим URL с помощью dj_database_url
        db_config = dj_database_url.parse(database_url, ssl_require=True)
        print("✅ URL успешно распарсился:", db_config)

        # Пробуем подключиться напрямую через psycopg2
        conn = psycopg2.connect(database_url, sslmode="require")
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("✅ Подключение успешно. Версия PostgreSQL:", version[0])

        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Ошибка подключения:", str(e))

if __name__ == "__main__":
    test_connection()
