import requests
loop=range(1, 100)
for i in loop:
    URL=f"https://networking-ecommerce-new.onrender.com/profile?id={i}"
    r=requests.get(url=URL)
    if r.status_code==200:
        print(URL)