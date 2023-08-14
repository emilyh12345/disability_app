def createDict():
   file = open('/Users/emilyhaller/Downloads/mockFile.txt', 'r')
   disabilityDict = {}
   for line in file:
       columns = line.split('|')
       # print(columns[0])A
       # if columns[0]== key already in list, append it
       if columns[0] in disabilityDict:
           disabilityDict[columns[0]].append(columns[1:])
       else:
           disabilityDict[columns[0]] = [columns[1:]]
       # print(columns)
   return disabilityDict


def main():
   disabilityDict = createDict()
   x = input("what disability do you have? ")
   #print(disabilityDict[x])
   for grant in disabilityDict[x]:
       #print(grant)
       print("Grant Name: " + grant[0] + ", Phone Number: " + grant[1] + ", Email: " + grant[2])

if __name__ == "__main__":
   main()
