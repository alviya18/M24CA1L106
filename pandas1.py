#Write a program to insert row at a given position in pandas DataFrame
import pandas as p
datadict={'Name' :['Arya','Liya','Miya'],'Age':[20,19,23]}
dataframe=p.DataFrame(datadict)
print(dataframe)
pos=int(input('Row? :'))
name=input('Name? :')
age=int(input('Age? :'))
print('UPDATED DATA\n**********')
dataframe=p.concat([dataframe[:pos-1], p.DataFrame({'Name' :[name],'Age':[age]}), dataframe[pos-1:]]).reset_index(drop=True)
print(dataframe)
