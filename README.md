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

## Setup Instructions
1. Clone this repo.
2. Create a CockroachDB Cloud cluster and get the connection string.
3. Set environment variables:
   ```bash
   export DATABASE_URL="postgresql://user:pass@host:26257/defaultdb?sslmode=verify-full"
