import requests
import json

instructions = {
  'parts': [
    {
      'file': 'first_half'
    },
    {
      'file': 'second_half'
    }
  ]
}

response = requests.request(
  'POST',
  'https://api.pspdfkit.com/build',
  headers = {
    'Authorization': 'Bearer pdf_live_eZFObhRnaQa4cufDtiSxpfLKAcAIsjYQqQeF3nipnn8'
  },
  files = {
    'first_half': open('output_pdf.pdf', 'rb'),
    'second_half': open('result.pdf', 'rb')
  },
  data = {
    'instructions': json.dumps(instructions)
  },
  stream = True
)

if response.ok:
  with open('result2.pdf', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=8096):
      fd.write(chunk)
else:
  print(response.text)
  exit()
