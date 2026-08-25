from llm import ask_llm
from feeds import get_news

def build_prompt(news, question):
    prompt = """
You are a threat intelligence analyst.

User request:
{question}

Analyze the following security news.
Provide:
- Threat actors mentioned
- Techniques used
- Critical infrastructure affected
- Potential impact

News:

"""

    for item in news:
        prompt += f"- {item}\n"

    prompt += """
Make sure you categorize subject matters properly.

Here are some definitions to refer to:

Threat actors = people who were responsible for the attack (for example: Advanced Persistant Threats (APTs), script kiddies, hackers, online scammers)
Techniques = methods used by threat actor (for example: Initial Access, Execution, Persistence, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, and Impact)
Critical infrastructure = Effected infrastructure sectors within a country that are vital for the country (for example: Energy, Water, Communications, Healthcare, Transportation, Financial Services, Government, Defense, Manufacturing, Food & Agriculture, Chemical, Nuclear, Space)
"""
    return prompt

def main():
    print("CLI Local Threat Intelligence Agent")
    print("Type 'exit' to quit OR 'refresh' to update feed.\n")

    intelligence = []

    while True:
        user_input = input("> ")

        intelligence = get_news()

        if user_input == "exit":
            break

        elif user_input == "refresh":
            intelligence = get_news()
            print("Threat feeds updated.")

        else:
            prompt = build_prompt(intelligence, user_input)
            
            answer = ask_llm(prompt)
            print(answer)


if __name__ == "__main__":
    main()