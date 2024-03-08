import base64
import json
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent.parent
API_KEY = "your_api_key"


def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify(file_names):
    # More optional parameters: https://github.com/flowerchecker/Request-id-API/wiki/Insect-identification
    payload = {
        "images": [encode_file(img) for img in file_names],
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "similar_images": True,
    }

    params = {
        # Details docs: https://github.com/flowerchecker/Insect-id-API/wiki/Details
        "details": "common_names,gbif_id,eppo_code,type",
    }
    headers = {
        "Content-Type": "application/json",
        "Api-Key": API_KEY,
    }

    response = requests.post(
        "https://crop.kindwise.com/api/v1/identification",
        params=params,
        json=payload,
        headers=headers,
    )

    assert response.status_code == 201, f"{response.status_code}: {response.text}"
    return response.json()


if __name__ == "__main__":
    identification = identify(
        [
            BASE_DIR / "images" / "example.jpg",
        ]
    )
    print(json.dumps(identification, indent=4))
