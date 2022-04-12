import json

def main():
    fileJSON = json.load(open("rand.json"))
    print(json.dumps(fileJSON, indent=2))

main()