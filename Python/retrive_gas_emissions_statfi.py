# Simply downloads data from the StatFin public API and dumps it to the terminal.
# Pipe the dump to a file and go from there.

import requests

url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/khki/statfin_khki_pxt_138v.px'

query = {
  "query": [
    {
      "code": "Kasvihuonekaasu",
      "selection": {
        "filter": "item",
        "values": [
          "SS",
          "01",
          "02",
          "03",
          "04",
          "05",
          "06",
          "07"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

response = requests.post(url, json=query)
data = response.json()
print(data)
