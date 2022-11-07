import requests
content = "⬜ "
################################################################################
link = "link to a channel here"
auth = "your auth token here"

###########################################################################
x = int(input("set x: "))
y = int(input("set y: "))
cont = input("what sign to use on making a square(leave blank to defult)")
if x > 7:
    print("x is to big(max 7)")
if cont == "":
    if x < 8:
        for s in range (y):
            payload = {
            'content': (content*x)
}
            header = {
                'authorization': auth
}
            r = requests.post(link, data=payload, headers = header )
else:
    if x < 8:
        for s in range (y):
            payload = {
            'content': (cont*x)
}
            header = {
                'authorization': auth
}
            r = requests.post(link, data=payload, headers = header )
