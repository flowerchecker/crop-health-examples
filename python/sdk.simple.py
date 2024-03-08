from kindwise import CropHealthApi

API_KEY = "your_api_key"

if __name__ == "__main__":
    api = CropHealthApi(API_KEY)

    identification = api.identify("../images/example.jpg", details=["taxonomy", "wiki_url"])
    print("is plant" if identification.result.is_plant.binary else "not plant")

    for suggestion in identification.result.crop.suggestions:
        print(suggestion.name)
        print(f"probability {suggestion.probability:.2%}")
        print()

    for suggestion in identification.result.disease.suggestions:
        print(suggestion.name, suggestion.scientific_name)
        print(f"probability {suggestion.probability:.2%}")
        print(suggestion.details["taxonomy"])
        print(suggestion.details["wiki_url"])
        print()
