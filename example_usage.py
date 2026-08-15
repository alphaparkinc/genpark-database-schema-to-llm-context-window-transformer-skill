from client import DatabaseSchemaToLlmContextWindowTransformerClient

def main():
    client = DatabaseSchemaToLlmContextWindowTransformerClient()
    res = client.transform_schema_to_context("postgresql://localhost:5432/prod_db", ["users", "orders"])
    print(f"Token Size: {res['context_token_size']} tokens")
    print(res["compressed_schema_md"])

if __name__ == "__main__":
    main()
