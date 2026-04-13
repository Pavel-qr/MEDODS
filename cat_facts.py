import urllib.request
import json

API_URL = "https://catfact.ninja/fact"
OUTPUT_FILE = "facts.txt"


def fetch_cat_fact():
    try:
        request = urllib.request.Request(
            API_URL, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data["fact"]
    except Exception:
        return None


def save_fact(fact):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(fact + "\n")


def main():
    fact = fetch_cat_fact()
    if fact is None:
        print("Не удалось получить факт")
        return
    save_fact(fact)
    print(f"Факт сохранён: {fact}")


if __name__ == "__main__":
    main()