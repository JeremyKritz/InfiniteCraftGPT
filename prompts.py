target = "TV"


def system_prompt():
    return f"""
    I am playing a game where I combine elements to create new elements.
    My ultimate goal is to create a specific target element, '{target}'. I start with four basic elements: Water, Fire, Wind, and Earth.
    By combining these elements, I can discover new elements. I must choose combinations wisely to progress towards my goal efficiently, avoiding repeating unsuccessful combinations. 
    Below is the history of my attempts and the outcomes, followed by a question on what to combine next.
    Return value must be the 2 elements, comma separated, nothing else.
    If there's no history that means this is yur first turn.
    Ex: DO NOT RESPOND: "I want to combine Fire and Water"
    Instead, respond "Fire, Water"
    """

def iterative_prompt(elements,  history):
    recent_history = history[-5:]  # Example to limit history length
    history_summary = "; ".join([f"{h['first']}+{h['second']}={h['result']}" for h in recent_history])
    return f"Given elements: {', '.join(elements)}. Recent history: {history_summary}. What two elements should I combine next? Respond only w comma separated values."