import requests
import json

instructions = {
  'parts': [
    {
      'file': 'file'
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
    'file': open('testdoc.docx', 'rb')
  },
  data = {
    'instructions': json.dumps(instructions)
  },
  stream = True
)

if response.ok:
  with open('result_doc.pdf', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=8096):
      fd.write(chunk)
else:
  print(response.text)
  exit()
