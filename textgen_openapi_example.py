from openai import OpenAI

if __name__ == '__main__':
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming "
                                          "concepts in limerick."},
            {"role": "user", "content": "Explain B-trees."}
        ]
    )
    print(completion.choices[0].message.content)
    print(completion.usage)
    
    