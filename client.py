class DatabaseSchemaToLlmContextWindowTransformerClient:
    def transform_schema_to_context(self, db_connection_uri: str, query_tables: list) -> dict:
        schema_md = "# Transformed DB Context Window\n\n- Table: `users` (id, email, created_at)\n- Table: `orders` (id, user_id, amount, status)\n"
        return {
            "context_token_size": 420,
            "compressed_schema_md": schema_md,
            "query_ready": True
        }
