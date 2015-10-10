def main():
    dictFile = open('vendors.txt','r')
    macSearch = input("Please enter the MAC address you are searching for?\n")
    temp = 0
    for x in range(7234):
        item = dictFile.readline()
        ## print (item)
        parts = item.split("	")
        if macSearch in item:
            print(macSearch + " = " + parts[1])
            temp = 1
            break
    if temp == 0:
        print("The MAC address entered could not found in the database")

if __name__ == "__main__":
    main()
