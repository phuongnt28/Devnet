import requests
import json 

# base url
base_url = "https://dummyapi.io/data/v1"
# key
headers = {"app-id": "61a1b1a6334d1b538e619c8f"}
limit = "?limit=10"
# API user
user_list = base_url + "/user" + limit
user_detail = base_url + "/user/%s" # user_profile
user_post = base_url + "/user/%s/post" + limit # user_profile post

# API post
post_list = base_url + "/post" + limit
comment_list = base_url + "/post/%s/comment" + limit

# API tag
tag_list = base_url + "/tag" + limit
post_by_tag = base_url + "/tag/water/post" + limit

def get_data_by_url(url, id=None):
    if id:
        url = url % id
    response = requests.get(url, headers=headers)

    if response.ok:
        content = json.loads(response.content)
        if 'data' in content:
            return content['data']
        else:
            return content
    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()

def show_data(data):
    print("The response contains {0} properties".format(len(data)))
    print("\n")
    if isinstance(data, list):
        for item in data:
            for key in item:
                value = item[key]
                if isinstance(value, dict) or isinstance(value, list):
                    value = json.dumps(value)
                print(key + " : %s " % value)
    else:
        for key in data:
            value = data[key]

            if isinstance(value, dict):
                value = json.dumps(value)
            print(key + " : %s " % value)
# get all user
users = get_data_by_url(user_list)
# show_data(users)

for user in users:
    user_id = str(user['id'])

    # get user profile
    user_profile = get_data_by_url(user_detail, user_id)
    # print(user_profile)
    show_data(user_profile)

    #load post by user id
    post = get_data_by_url(user_post, user_id)
    # print(user_profile)
    show_data(post)
# create json
with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)
