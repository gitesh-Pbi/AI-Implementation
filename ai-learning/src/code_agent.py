def generate_code_prompt(df_columns, question):
    return f"""
You are a Python data analyst.

A pandas DataFrame named df is already loaded.

Columns:
{df_columns}

Write ONLY Python code (no explanation).
The final result MUST be stored in a variable called result.

User question:
{question}
"""