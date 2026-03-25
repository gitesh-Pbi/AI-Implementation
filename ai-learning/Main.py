from src.gemini_client import GeminiClient

def main():
    print("=" * 50)
    print("   Gemini AI - First Test")
    print("=" * 50)
    
    client = GeminiClient()
    
    while True:
        prompt = input("\nYou: ")

        if prompt.lower() in ["exit", "quit"]:
            break

        response = client.ask(prompt)
        print(f"\nAI: {response}")

if __name__ == "__main__":
    main()