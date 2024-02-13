
import openai

# Initialize your OpenAI API key here
openai.api_key = ''

def send_prompt_to_gpt3(system, prompt):
    #print(system)
    #print(prompt)
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                response_format={ "type": "json_object" },
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
    #print(response)

    suggestion = response.choices[0].message['content'] 
    return suggestion
    #pri.strip().split(", ")nt(suggestion)