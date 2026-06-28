from sqlalchemy import text
from db import engine

try:
    conn = engine.connect()
    print("✅ TiDB connection successful!")

    result = conn.execute(text("SELECT 1"))
    print("Test result:", result.fetchone())

    conn.close()

except Exception as e:
    print("❌ Connection failed:")
    print(e)