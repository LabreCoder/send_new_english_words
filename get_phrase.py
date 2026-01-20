import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url, timeout=10)

    results = []
    dictionary_url = f"https://dictionary.cambridge.org/"

    if response.status_code != 200:
        results.append((f"Definition not found. Please, check on: {dictionary_url}", f"No example available. Please, check on: {dictionary_url}"))
        return results

    else:

        data = response.json()

        if data[0]["meanings"]:
            for meaning in data[0]["meanings"]:
                for definition_data in meaning["definitions"]:
                    definition = definition_data.get(
                        "definition", f"No definition available. Please, check on: {dictionary_url}"
                    )
                    example = definition_data.get(
                        "example", f"No example available. Please, check on: {dictionary_url}"
                    )

                    results.append((definition, example))
        else: 
            results.append((f"Definition not found. Please, check on: {dictionary_url}", f"No example available. Please, check on: {dictionary_url}"))
                
        return results