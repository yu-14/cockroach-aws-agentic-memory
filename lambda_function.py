import json
import os
import pg8000

def lambda_handler(event, context):
    try:
        db_host = os.environ['DB_HOST']
        db_port = int(os.environ['DB_PORT'])
        db_user = os.environ['DB_USER']
        db_password = os.environ['DB_PASSWORD']
        db_name = os.environ['DB_NAME']

        conn = pg8000.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name,
            ssl_context=True
        )
        cur = conn.cursor()
        cur.execute("""
            SELECT session_id, message->>'content', created_at
            FROM chat_history
            ORDER BY created_at DESC
            LIMIT 5
        """)
        rows = cur.fetchall()
        conn.close()

        messages = [
            {"session_id": r[0], "content": r[1], "created_at": str(r[2])}
            for r in rows
        ]

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': '✅ Retrieved persistent memory from CockroachDB!',
                'memory': messages
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
