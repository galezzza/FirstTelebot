import json

import requests


def crossout():
    url = "https://crossoutdb.com/data/search"

    response = requests.get(url).json()

    copper_cost = 0
    metal_cost = 0
    wires_cost = 0
    electronics_cost = 0
    batteries_cost = 0
    plastic_cost = 0

    b = 0
    fgh = {}

    for i in response["data"]:
        if i["id"] == 43:
            # print((i["formatBuyPrice"]))
            copper_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = copper_cost
            b = b + 1
        if i["id"] == 53:
            # print((i["formatBuyPrice"]))
            metal_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = metal_cost
            b = b + 1
        if i["id"] == 85:
            # print((i["formatBuyPrice"]))
            wires_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = wires_cost
            b = b + 1
        if i["id"] == 168:
            # print((i["formatBuyPrice"]))
            electronics_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = electronics_cost
            b = b + 1
        if i["id"] == 784:
            # print((i["formatBuyPrice"]))
            batteries_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = batteries_cost
            b = b + 1
        if i["id"] == 785:
            # print((i["formatBuyPrice"]))
            plastic_cost = 0.9 * float(i["formatBuyPrice"])
            fgh[b] = plastic_cost
            b = b + 1


    # print()

    fgh[b] = ((3 * metal_cost + copper_cost) / 2)
    b = b + 1

    fgh[b] = ((4 * metal_cost + 10 * copper_cost + 6 * wires_cost + 3 * plastic_cost) / 10)
    b = b + 1

    fgh[b] = ((8 * metal_cost + 15 * copper_cost + 17 * wires_cost + 8 * plastic_cost) / 10)
    b = b + 1

    fgh[b] = ((1 * metal_cost + 5 * copper_cost + 5 * electronics_cost + 5 * batteries_cost) / 2)
    b = b + 1

    # print()

    for i in response["data"]:
        if (i["rarityName"] != "None") and (i["categoryName"] != "None") and (i["typeName"] != "None"):

            # if i["typeName"] == "Resource":
            #     print(i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"])
            #     a = a + 1

            if i["categoryName"] == "Decor":

                if (i["rarityName"] == "Rare") and (float(i["formatSellPrice"]) < ((3 * metal_cost + copper_cost) / 2)):
                    if (i["formatSellPrice"] != "0.00") and (i["typeName"] != "Decor. Signs"):
                        # print(i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"])
                        #
                        fgh[b] = [i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"]]
                        b = b + 1

                if (i["rarityName"] == "Special") and (float(i["formatSellPrice"]) < ((4 * metal_cost + 10 * copper_cost + 6 * wires_cost + 3 * plastic_cost) / 10)):
                    if i["formatSellPrice"] != "0.00":
                        # print(i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"])
                        #
                        fgh[b] = [i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"]]
                        b = b + 1

                if (i["rarityName"] == "Epic") and (float(i["formatSellPrice"]) < ((8 * metal_cost + 15 * copper_cost + 17 * wires_cost + 8 * plastic_cost) / 10)):
                    if i["formatSellPrice"] != "0.00":
                        # print(i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"])
                        #
                        fgh[b] = [i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"]]
                        b = b + 1

                if (i["rarityName"] == "Legendary") and (float(i["formatSellPrice"]) < ((1 * metal_cost + 5 * copper_cost + 5 * electronics_cost + 5 * batteries_cost) / 2)):
                    if i["formatSellPrice"] != "0.00":
                        # print(i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"])
                        #
                        fgh[b] = [i["id"], i["name"], i["rarityName"], i["categoryName"], i["typeName"], i["formatBuyPrice"], i["formatSellPrice"]]
                        b = b + 1
    return fgh
#

array = crossout()

# print("starting")
# print()

# print(crossout())
# print(array)


# saveResponse = json.dumps(response, indent=3)
#
# with open("sample.json", "w") as outfile:
#
#     outfile.write(saveResponse)
