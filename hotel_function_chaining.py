import openai

from tooling import tools

if __name__ == '__main__':

    messages = [
        {"role": "system", "content": "You are a help reservation assistant. Use the supplied tools to assist the user."},
        {"role": "user", "content": "Please make a reservation for me near Adrian, Michigan."}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools()
    )

    print(response)
