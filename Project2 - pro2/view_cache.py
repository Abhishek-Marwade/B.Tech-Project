"""
SQLite Cache Viewer
View the contents of cache.db
"""
import sqlite3
import json

# Connect to database
conn = sqlite3.connect('cache.db')
cursor = conn.cursor()

# Get table schema
print("=" * 80)
print("DATABASE SCHEMA")
print("=" * 80)
cursor.execute("PRAGMA table_info(cache)")
schema = cursor.fetchall()
for col in schema:
    print(f"Column: {col[1]:<20} Type: {col[2]:<10} Not Null: {col[3]}")

# Get total entries
print("\n" + "=" * 80)
print("DATABASE STATISTICS")
print("=" * 80)
cursor.execute("SELECT COUNT(*) FROM cache")
total = cursor.fetchone()[0]
print(f"Total cached entries: {total}")

# Count by type (based on key suffix)
cursor.execute("SELECT key FROM cache")
all_keys = cursor.fetchall()

embeddings = sum(1 for k in all_keys if '_embedding_001' in k[0])
summaries = sum(1 for k in all_keys if '_summary' in k[0])
other = total - embeddings - summaries

print(f"  - Embeddings: {embeddings}")
print(f"  - Summaries: {summaries}")
print(f"  - Other: {other}")

# Show sample entries
print("\n" + "=" * 80)
print("SAMPLE CACHE ENTRIES (First 5)")
print("=" * 80)

cursor.execute("SELECT key, LENGTH(value) as value_size FROM cache LIMIT 5")
samples = cursor.fetchall()

for i, (key, size) in enumerate(samples, 1):
    # Truncate long keys
    display_key = key[:60] + "..." if len(key) > 60 else key
    print(f"\n{i}. Key: {display_key}")
    print(f"   Value size: {size} bytes")
    
    # Determine type
    if '_embedding_001' in key:
        print(f"   Type: Embedding (768-dim vector)")
    elif '_summary' in key:
        print(f"   Type: Summary")
    else:
        print(f"   Type: Unknown")

# Show embedding keys specifically
print("\n" + "=" * 80)
print("EMBEDDING CACHE SAMPLES")
print("=" * 80)

cursor.execute("SELECT key FROM cache WHERE key LIKE '%_embedding_001' LIMIT 5")
emb_keys = cursor.fetchall()

for i, (key,) in enumerate(emb_keys, 1):
    # Remove the suffix to see the actual text
    text = key.replace('_embedding_001', '')
    display_text = text[:100] + "..." if len(text) > 100 else text
    print(f"{i}. Cached text: {display_text}")

print("\n" + "=" * 80)
print("To view full database, use:")
print("  - DB Browser for SQLite (GUI): https://sqlitebrowser.org/")
print("  - Or command: sqlite3 cache.db")
print("=" * 80)

conn.close()
