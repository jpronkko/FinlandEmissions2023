# Simply downloads data from the StatFin public API and dumps it to file given as argument.

import requests
import sys

if len(sys.argv) != 2:
  print(f"Usage: python ${sys.argv[0]} <output_file>")
  sys.exit(1)

output_file = sys.argv[1]
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
    "format": "csv"
  }
}

response = requests.post(url, json=query)
data = response.text

with open(output_file, 'w') as f:
  f.write(data)

print(f"Data written to {output_file}")