import json
def bacaJSON(namaFile=""):
    "Read file JSON"
    f = open(namaFile)
    data = json.load(f)
    f.close()
    return data

if __name__=="__main__":
    main()