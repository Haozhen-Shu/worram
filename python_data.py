import requests
import json
response_API = requests.get("https://top-100-example.s3.amazonaws.com/t100_2021_full.json", verify=False)
# print(response_API.status_code)
response = response_API.json()
# print(response)

# pip install requests,and json
#
#  "id", "winery_full", "wine_full", "color", "price"
{"id": 1280675}
arr =[]
for item in response:
    obj = {}
    # print(item["id"])
    obj["id"]= item["id"]

    arr.append(obj)
print(arr)


# fileter function 

[
  {
    application: 1,
    emails: ["a@gmail.com", "b@gmail.com"],
    name: "A",
  },
  {
    application: 1,
    emails: ["c@gmail.com", "d@gmail.com"],
    name: "C",
  },
  {
    application: 2,
    emails: ["a@yahoo.com"],
    name: "A",
  },
  {
    application: 3,
    emails: ["a@gmail.com", "a@yahoo.com"],
    name: "A",
  },
]