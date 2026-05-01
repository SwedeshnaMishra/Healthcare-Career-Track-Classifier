import json
from logic.classifier import classify

def load_data():
    with open("data/sample_candidates.json", "r") as file:
        return json.load(file)

def main():
    candidates = load_data()

    for c in candidates:
        result = classify(c)

        print("\n==============================")
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()