import pandas as pd


def getData(Data):
    dataSet = []
    for head in Data.head():
        tmp = list(Data[head])
        tmp.insert(0, head)
        dataSet.append(tmp)
    dataSet.pop(-len(dataSet))
    return dataSet


def AssociationRule(Rule, DataSet):
    Nx = Ny = N_Y = 0
    col1 = []
    col2 = []
    c = 0
    for col in DataSet:
        if col[0].lower() in Rule.split('->'):
            if Rule.index(col[0].lower()) == 0:
                col1 = col[1:]
                Nx = sum(col1)
            else:
                col2 = col[1:]
                Ny = sum(col2)

            if col1 != [] and col2 != []:
                for i in range(len(col1)):
                    if col1[i] == col2[i]:
                        c += 1
            N_Y = c
    print(f"Nx = {Nx} \nNy = {Ny} \nN^y = {N_Y} \nN = {len(DataSet)}")
    print(f"Support: {N_Y / len(DataSet)} \nConfidence: {N_Y / Nx} \nLift: {(N_Y * len(DataSet)) / (Nx * Ny)}")


data = pd.read_excel('Data Set.xlsx')
"""
* data.head()
* data.values
"""
# print(getData(data))

rule = input("Enter The Rule\n")

AssociationRule(rule, getData(data))
