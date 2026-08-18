import os
import psycopg
import json

DATABASE_URL = os.getenv("DATABASE_URL")

conversation = [
    ("user", "Hello! I need a system that remembers conversations."),
    ("assistant", "I can help! I use CockroachDB for persistent memory across sessions."),
    ("user", "How does it handle large-scale data?"),
    ("assistant", "CockroachDB has distributed vector indexing for fast semantic search at scale."),
    ("user", "Can it store embeddings too?"),
    ("assistant", "Yes! We use the VECTOR type with vector indexes for RAG pipelines."),
    ("user", "What AWS services does it integrate with?"),
    ("assistant", "It works perfectly with AWS Bedrock for LLMs and Lambda for serverless deployment.")
]

def insert_conversation():
    try:
        with psycopg.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                for role, content in conversation:
                    message = json.dumps({"role": role, "content": content})
                    cur.execute("""
                        INSERT INTO chat_history (session_id, message)
                        VALUES (%s, %s::jsonb)
                    """, ("hackathon-demo", message))
                conn.commit()
                print("✅ Inserted 8 messages into chat_history!")
                
                cur.execute("""
                    SELECT COUNT(*) FROM chat_history WHERE session_id = 'hackathon-demo'
                """)
                count = cur.fetchone()[0]
                print(f"📊 Total messages in session 'hackathon-demo': {count}")
                
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    insert_conversation()
