import urllib.request, json

try:
    url = "https://gateway.apiportal.ns.nl/public-prijsinformatie/prices?fromStation=es&toStation=aml"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '807462db71c64449a8ba7aef0c56c43c',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)