#downloads a PDF file into local directory
import requests

url ="https://download.microsoft.com/download/d/0/0/d0001082-eedc-41e2-a7c2-4bd05a7fb63a/BusinessApps_ReleaseNotes_v18.1.4.pdf"
response = requests.get(url)

with open("BusinessApps_ReleaseNotes_v18.1.4.pdf", "wb") as f:
    f.write(response.content)
