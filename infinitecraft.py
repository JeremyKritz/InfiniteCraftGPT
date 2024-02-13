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
    current_elements = ["Water", "Fire", "Wind", "Earth"]
    history = []  # Keep track of combinations tried
    emojis = {"Water": "💧", "Fire": "🔥", "Wind": "🌬️", "Earth": "🌍"}  # Initial emojis

    while target not in current_elements:
        input("Press Enter.")
        
        # Assuming system_prompt and iterative_prompt are properly defined and return the correct strings
        prompt = iterative_prompt(current_elements, history)
        suggestion = send_prompt_to_gpt3(system_prompt(), prompt)

        if suggestion and len(suggestion) == 2 and all(elem in current_elements for elem in suggestion):
            combined_elements = (suggestion[0], suggestion[1])
            result = combine(combined_elements)
            history.append({'first': suggestion[0], 'second': suggestion[1], 'result': result["result"]})
            
            if result and result["result"] not in current_elements:
                current_elements.append(result["result"])
                # Update emojis dictionary with new element's emoji if it's provided
                if "emoji" in result:
                    emojis[result["result"]] = result["emoji"]
                if result["result"] == target:
                    print(f"Successfully created {target}!")
                    break
            print(f"{emojis.get(suggestion[0], '❓')} {suggestion[0]} + {emojis.get(suggestion[1], '❓')} {suggestion[1]} -> {emojis.get(result['result'], '❓')} {result['result']}")
        else:
            print("Invalid suggestion or elements not in current list.")

if __name__ == "__main__":
    main()