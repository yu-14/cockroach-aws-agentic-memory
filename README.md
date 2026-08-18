# CockroachDB × AWS Agentic Memory

An AI agent that uses **CockroachDB as persistent memory**, deployed on **AWS Lambda**.  
The agent stores conversation history in CockroachDB and retrieves it via the Managed MCP Server and a serverless function.

## Features
- ✅ Persistent conversation memory (chat history) in CockroachDB
- ✅ Retrieval through CockroachDB Cloud Managed MCP Server (tested in Cursor)
- ✅ Distributed vector indexing for embeddings (`social_post` table)
- ✅ Serverless execution via AWS Lambda with a public Function URL

## Architecture
[Insert a simple diagram if you have one, otherwise describe in text]

## Tools Used
### CockroachDB
- **Managed MCP Server** – direct agent access to cluster
- **Distributed Vector Indexing** – for semantic search / RAG (table `social_post`)
- **CockroachDB Cloud** – free tier serverless cluster

### AWS
- **AWS Lambda** – hosts the memory retrieval function

### Distributed Vector Indexing
Created a `demo_posts` table with a `VECTOR(3)` column and HNSW index.  
Inserted sample embeddings and ran a similarity query returning distance scores (0, 1.414, 2.828).  
This demonstrates CockroachDB's ability to handle semantic search at scale.

## Setup Instructions
1. Clone this repo.
2. Create a CockroachDB Cloud cluster and get the connection string.
3. Set environment variables:
   ```bash
   export DATABASE_URL="postgresql://user:pass@host:26257/defaultdb?sslmode=verify-full"
4. Run insert_data.py to populate sample memory.
5. Deploy lambda_function.py to AWS Lambda (with pg8000 layer).
6. Enable Lambda Function URL for public access.

Demo: https://rhx4s2ewgmxjjmcjboz6vm27ea0qcoua.lambda-url.ap-south-1.on.aws
Video: https://youtu.be/F83jBCuUAwM?si=svsqrAb80xuQ79sH
