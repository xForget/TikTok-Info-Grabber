import sys
from datetime import datetime
import requests
print("""
Telegram : Jxshe | Github : xForget
""")
def awemeRequest(request_path, type="get"):
    headers = {
        "User-Agent": "okhttp",
    }
    url = "https://api-t2.tiktokv.com" \
          + request_path \
          + "&device_id=6158568364873266588" \
          + "&version_code=100303" \
          + "&build_number=10.3.3" \
          + "&version_name=10.3.3" \
          + "&aid=1233" \
          + "&app_name=musical_ly" \
          + "&app_language=en" \
          + "&channel=googleplay" \
          + "&device_platform=android" \
          + "&device_brand=Google" \
          + "&device_type=Pixel" \
          + "&os_version=9.0.0"
    if type == "get":
        resp = requests.get(url, headers=headers)
    if type == "post":
        resp = requests.post(url, headers=headers)
    return resp


def getUidByUsername(username):
    endpoint = "/aweme/v1/discover/search/" \
               + "?keyword=" + username \
               + "&cursor=0" \
               + "&count=10" \
               + "&type=1" \
               + "&hot_search=0" \
               + "&search_source=discover"
    response = awemeRequest(endpoint, type="post").json()
    print(response)

    for userObj in response.get("user_list"):
        userInfo = userObj.get("user_info")
        if userInfo.get("unique_id") == username:
            userId = userInfo.get('uid')

            return int(userId)
    return ""

def tiktok_timestamp(urlid):
    binary = "{0:b}".format(urlid)
    i=0
    bits=""
    while i < 31:
        bits += binary[i]
        i+=1
    timestamp = int(bits,2)
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


ask = input('[?] Get info from\n[1] Username\n[?] Username ID\n[?] :')
if ask == "1":
    username = input('[?] Username :')
    id = getUidByUsername(username=username)
    if id:
        s = tiktok_timestamp(id)
        input(f"[+] Username :{username}\n[+] username_id :{id}\n[+] Create Time:{s}\n")
        exit()
    else:
        print('[X] Username Not Found')

else:
    username_id = int(input('[?] Username_id :'))
    s = tiktok_timestamp(username_id)
    input(f"[+] Create Time: {s}")
