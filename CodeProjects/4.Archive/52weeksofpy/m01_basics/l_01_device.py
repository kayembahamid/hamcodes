from pprint import pprint


# DICTIONARY representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLE PRINT
print("\n_____ SIMPLE PRINT_______________")
print("device:", device)
print("device name:", device["name"])

# PRETTY PRINT
print("\n_____ PRETTY PRINT_______________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____ FOR LOOP,USING F-STRING _____________")
for key, value in device.items():
    print("{key:>16s} : {value}")
