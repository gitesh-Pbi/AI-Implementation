from src.gemini_client import GeminiClient
from src.data_loader import load_data
from src.code_agent import generate_code_prompt
from src.executor import execute_code


def main():
    client = GeminiClient()

    df = load_data("data/sample.csv")

    print("\n📊 Data Loaded Successfully!")
    print(df.head())

    while True:
        question = input("\nAsk your data question (or 'quit'): ")

        if question.lower() == "quit":
            break

        # Step 1: Generate code
        prompt = generate_code_prompt(df.columns.tolist(), question)

        code = client.ask(prompt)

        print("\n🧠 Generated Code:")
        print(code)

        # Step 2: Execute code
        result = execute_code(code, df)

        print("\n📊 Result:")
        print(result)


if __name__ == "__main__":
    main()