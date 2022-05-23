response= [
  {
    "application": 1,
    "emails": ["a@gmail.com", "b@gmail.com"],
    "name": "A",
  },
  {
    "application": 1,
    "emails": ["c@gmail.com", "d@gmail.com"],
    "name": "C",
  },
  {
    "application": 2,
    "emails": ["a@yahoo.com"],
    "name": "A",
  },
  {
    "application": 3,
    "emails": ["a@gmail.com", "a@yahoo.com"],
    "name": "A",
  },
]

# Results:
# // [
# //     {
# //         application: [1,2,3],
# //         email: [a@gmail.com,b@gmail.com,a@yahoo.com],
# //         name: "A"
# //     },
# //     {
# //         application: [1],
# //         email: [c@gmail.com,d@gmail.com],
# //         name: "C"
# //     }
# // ]


def combineData(resp):
    arr = []
    name_arr = []
    for item in resp:
        name_arr.append(item["name"])
    name_list = list(set(name_arr))
    # print(name_list)

    for name  in name_list:
        obj = {}
        app_arr =[]
        email_arr = []
        for res in resp:
            if res["name"] == name:
                app_arr.append(res["application"])
                email_arr.append(res["emails"])
                # print(email_arr)
                list_email=[]
                for i  in email_arr:
                    for j in i:
                        list_email.append(j)
                # print(email_arr)

                obj["application"] = app_arr
                obj["emails"] = list(set(list_email))
                # print(res["name"])
                obj["name"] = res["name"]
        arr.append(obj)
    return arr


        
    # for i in range(len(response)):
    #     obj = {}
    #     if item["name"]

print(combineData(response))
