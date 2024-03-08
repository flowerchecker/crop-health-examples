# crop.health API
*⚠️ This service is in beta version and can undergo changes which might not be compatible with the curent version.*

[Crop.health](https://crop.kindwise.com) offers crop health assessment identification API based on machine learning. [Obtain the API key](https://admin.mlapi.ai/signup) and get started with your implementation.

See our **[documentation](http://crop.kindwise.com/docs)** for the full reference.

## Crop and disease Identification
Send us your crop images encoded in base64, and get a list of possible crop and diseases suggestions with additional information.

```bash
pip install kindwise-api-client
```

```python
from kindwise import CropHealthApi

api = CropHealthApi("your_api_key")
identification = api.identify("../images/example.jpg", details=["taxonomy", "wiki_url"])

for suggestion in identification.result.crop.suggestions:
    print(suggestion.probability, suggestion.name)

print()
for suggestion in identification.result.disease.suggestions:
    print(suggestion.probability, suggestion.name)
```

Same example in pure python

```python
import base64

import requests

with open('../images/example.jpg', 'rb') as file:
    images = [base64.b64encode(file.read()).decode('ascii')]

response = requests.post(
    'https://crop.kindwise.com/v1/identification',
    params={'details': 'taxonomy,wiki_url'},
    headers={'Api-Key': 'your_api_key'},
    json={'images': images},
)

identification = response.json()

for suggestion in identification['result']['crop']['suggestions']:
    print(suggestion["probability"], suggestion['name'])
    
print()

for suggestion in identification['result']['disease']['suggestions']:
    print(suggestion["probability"], suggestion['name'])

```
