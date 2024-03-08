from kindwise import CropHealthApi

API_KEY = "your_api_key"

if __name__ == "__main__":
    api = CropHealthApi(API_KEY)

    identification = api.identify("../images/example.jpg", asynchronous=True)
    assert identification.result is None
    identification = api.get_identification(identification.access_token)
    assert identification.result is not None
