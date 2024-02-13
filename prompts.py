target = "TV"


def system_prompt():
    return """
    You are playing a game where you combine elements to create new elements.
    Your ultimate goal is to create a specific target element, 'TV'.
    By combining these elements, you discover new elements. You must choose combinations wisely to progress towards your goal efficiently, avoiding repeating unsuccessful combinations. 
    Below is the history of your attempts and the outcomes, followed by a question on what to combine next.
    Please respond in JSON format with two fields: "elements", which should be the two elements to combine next, comma-separated, and "reasoning", a one-sentence explanation of your current thinking.
    If there's no history, that means this is your first turn.
    Example response format: 
    {
        "reasoning": "Combining Fire and Water might produce Steam, or Boiling Water, which may be helpful."
        "elements": "Fire, Water",
    }
    {
        "reasoning": "Combining Earth and Water might result in Mud, which could help with building."
        "elements": "Earth, Water",
    }
    {
        "reasoning": "I will combine Wheat and Lightning, just to see what happens."
        "elements": "Wheat, Lightning",
    }
    Ensure the JSON structure is maintained and valid.
    """

def iterative_prompt(elements,  history):
    recent_history = history[-5:]  # Example to limit history length
    history_summary = "; ".join([f"{h['first']}+{h['second']}={h['result']}" for h in recent_history])
    return f"Given elements: {', '.join(elements)}. Recent history: {history_summary}."