# This is my submission to WM Challenge 2 for the Data Analyst Position.

import pandas as pd
import collections
import numpy as np

# Making a csv file into a Data Frame.

df = pd.read_csv('NYC_Jobs.csv')

# This function Sum takes an array and adds all the elements in that array.

def Sum(A):
    u = 0
    for i in range(len(A)):
        u = u + A[i]
    return u

# The CleanColumnNames function takes a data frame and changes the column names (attributes) so that they are valid Python identifiers.

def CleanColumnNames(df):
    c = []
    for i in range(len(df.columns)):
        newString = df.columns[i].replace(" ", "").replace("#", "Number").replace("/","")
        c.append(newString)
    return c

df.columns = CleanColumnNames(df)

# The function Mapping takes a data frame and a column name. d is a dictionary that maps an attribute to a list.

def Mapping(df, p):
    d = collections.defaultdict(list)
    for index, column in p.iteritems():
        d[column].append(index)
    return d

print("Who has the most openings?")

ListToSet = set(df.Agency)
SetToList = list(ListToSet)
AgencyMapping = Mapping(df, df.Agency)

for i in range(len(SetToList)):
    indices = AgencyMapping[SetToList[i]]
    q = Sum(df.NumberOfPositions[indices].values)
    print(SetToList[i], q)

maxi = 0
j = 0
for i in range(len(SetToList)):
    indices = AgencyMapping[SetToList[i]]
    s = Sum(df.NumberOfPositions[indices].values)
    if q > maxi:
        j = i
        maxi = s

print("Department with most openings:")

print SetToList[j], ", " , maxi, "openings"

print("Which departments have the highest and the lowest paying positions based on current job openings?")

#print(df.SalaryRangeTo.value_counts().sort_index())

AgencyMapping = Mapping(df, df.SalaryRangeTo)
HighestSalary = df.SalaryRangeTo.max()
indices = AgencyMapping[HighestSalary]

print "Departments with Highest Salary, ", HighestSalary , "dollars annually"

print(df.Agency[indices].values)

LowestSalary = df.SalaryRangeTo.min()
indices = AgencyMapping[LowestSalary]

print "Departments with Lowest Salary:", LowestSalary , "dollars hourly"

print(df.Agency[indices].values)

print("The jobs that are hardest to fill are probably those which have been posted up the earliest.")

#  Changing the PostingDate. I only care about the year that the job was posted.

def Year(Date):
    StringDate = str(Date)
    StringYear = StringDate[6:10]
    return int(StringYear)

df['PostingDate'] = df['PostingDate'].apply(Year)

AgencyMapping = Mapping(df, df.PostingDate)
EarliestDate = df.PostingDate.min()
indices = AgencyMapping[EarliestDate]

print("Jobs that are hardest to fill:")

print (df.BusinessTitle[indices].values)


