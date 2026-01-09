import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return "Meaning not found."

    results = []

    data = response.json()

    for meaning in data[0]["meanings"]:
        for definition_data in meaning["definitions"]:
            definition = definition_data.get(
                "definition", "No definition available."
            )
            example = definition_data.get(
                "example", "No example available."
            )

            results.append((definition, example))
            
    return results