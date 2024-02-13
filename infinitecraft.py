# Infinite_Craft.py

import requests
import json
from gpt_service import send_prompt_to_gpt3
from prompts import system_prompt, iterative_prompt, target


def combine(elem):
    url = "https://neal.fun/api/infinite-craft/pair"
    params = {"first": elem[0], "second": elem[1]}
    headers = {
        "Referer": "https://neal.fun/infinite-craft/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        output = json.loads(response.text)
        return output
    else:
        print(response.status_code)
        return None

def main():
    print("Starting, press CTRL+C to stop")
    current_elements = ["Water", "Fire", "Wind", "Earth"]
    history = []  # Keep track of combinations tried

    while target not in current_elements:
        input("Press Enter to generate the next combination...")
        # Use GPT-3 to suggest the next combination based on current elements and history
        prompt = iterative_prompt(current_elements, history)
        suggestion = send_prompt_to_gpt3(system_prompt(), prompt)

        if suggestion and all(elem in current_elements for elem in suggestion):
            result = combine(suggestion)
            if result and result["result"] not in current_elements:
                current_elements.append(result["result"])
                history.append({'first': suggestion[0], 'second': suggestion[1], 'result': result["result"]})
                print(f"Combined {suggestion[0]} and {suggestion[1]} to get {result['result']}.")
                if result["result"] == target:
                    print(f"Successfully created {target}!")
                    break
            else:
                print(f"Failed to combine {suggestion[0]} and {suggestion[1]} or already known.")
        else:
            print("Invalid suggestion or elements not in current list.")

if __name__ == "__main__":
    main()