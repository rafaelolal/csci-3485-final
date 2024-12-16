import requests

texts = [
    "The efficiency of modern solar panels has increased dramatically, with new photovoltaic technologies achieving conversion rates of over 20% in residential installations, making them increasingly viable for homeowners.",
    "Pineapples are unique tropical fruits that contain bromelain, an enzyme mixture with anti-inflammatory properties, which has been studied for its potential therapeutic applications in modern medicine.",
    "The classic Rubik's cube puzzle has spawned numerous variations, including the 4x4 and 5x5 versions, challenging enthusiasts with more complex algorithms and longer solving times.",
    "Solar power installations in desert regions face unique challenges, including dust accumulation and extreme temperature variations, requiring specialized maintenance protocols and cleaning schedules.",
    "The cultivation of pineapples requires specific soil conditions and approximately 18-24 months to produce the first fruit, making it a significant investment for agricultural entrepreneurs.",
    "Speed cubing competitions have evolved to include multiple categories, with world records being broken using advanced solving techniques and specially designed cubes with enhanced turning mechanisms.",
    "Recent innovations in solar energy storage systems have revolutionized off-grid living possibilities, with advanced battery technologies providing reliable power throughout non-daylight hours.",
    "The global pineapple industry faces sustainability challenges, including water usage optimization and soil conservation, prompting research into more environmentally friendly farming practices.",
    "Mathematical analysis of Rubik's cube combinations reveals over 43 quintillion possible positions, making it one of the most complex mechanical puzzles ever created.",
    "Floating solar farms represent an innovative approach to renewable energy generation, utilizing water bodies to cool panels and increase efficiency while preserving valuable land resources.",
]

collection_name = "my_collection"

for i, text in enumerate(texts):
    response = requests.post(
        "http://localhost:8000/create",
        json={"doc": text, "index": i, "collection": collection_name},
    )

    print(f"Status code {i}: {response.status_code}")
