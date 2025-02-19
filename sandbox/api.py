# import asyncio
# from typing import Union

# from nekosbest import Client, Result

# client = Client()

# async def get_img(type: str, amount: int = 1) -> Union[Result, list[Result]]:
#     result = await client.get_image(type, amount)
#     print(result)

# loop = asyncio.get_event_loop()

# loop.run_until_complete(get_img("shoot"))
# # loop.run_until_complete(get_img("neko", 2))

# loop.close()

from openai import OpenAI
client = OpenAI(
   api_key='sk-DyynT5CmKFJUobOrXKsRjCSVyVNqMUnZN6BEbfOzTkovbNMI',
   base_url='https://api.opentyphoon.ai/v1'
)

names = ["Frieren", "Fern", "Stark", "Himmel", "Übel", "Methode", "Eisen", "Flamme", "Heiter", "Sein"]


task = f" สรุปเรื่องย่อของอนิเมะเรื่องนี้เป็นภาษาไทยโดยไม่ใช้คำว่า \"{", ".join(names)}\" เรื่องย่อมีดังนี้"
print(task)
print()

synopsis = """
During their decade-long quest to defeat the Demon King, the members of the hero's party—Himmel himself, the priest Heiter, the dwarf warrior Eisen, and the elven mage Frieren—forge bonds through adventures and battles, creating unforgettable precious memories for most of them. However, the time that Frieren spends with her comrades is equivalent to merely a fraction of her life, which has lasted over a thousand years. When the party disbands after their victory, Frieren casually returns to her "usual" routine of collecting spells across the continent. Due to her different sense of time, she seemingly holds no strong feelings toward the experiences she went through. As the years pass, Frieren gradually realizes how her days in the hero's party truly impacted her. Witnessing the deaths of two of her former companions, Frieren begins to regret having taken their presence for granted; she vows to better understand humans and create real personal connections. Although the story of that once memorable journey has long ended, a new tale is about to begin.
"""

content = task + synopsis

chat_completion = client.chat.completions.create(
  model="typhoon-v1.5x-70b-instruct",
  messages=[{"role": "user", "content": content}]
)

print(chat_completion.choices[0].message.content)
