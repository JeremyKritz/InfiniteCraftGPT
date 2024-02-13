
import openai

# Initialize your OpenAI API key here
openai.api_key = ''

def send_prompt_to_gpt3(system, prompt):
    #print(prompt)
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": system
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=700
            )

    suggestion = response.choices[0].message.content.strip().split(", ")
    #print(suggestion)
    return suggestion