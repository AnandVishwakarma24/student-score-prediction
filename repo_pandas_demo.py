# %%
import pandas as pd


print(pd.__version__)

# %%
#Data Structures in pandas in python 

# 1).Series data structure
     
x=[1,2,3,4,5,6,7,8,9]    #using list
var=pd.Series(x)

print(var)
print(type(var))

#access values by index
print(var[1:5])

#changing index values
var1=pd.Series(x,index=['a','b','c','d','e','f','g','h','i'])
print(var1)

dic={
    "name":["Anand","Vishal","Rahul"],
    "subject":["Python","Java","C++"],
    "Rank":[1,2,3]

}

var2=pd.Series(dic)
var2

# %%
s=pd.Series(12)
s
#strectching data into multiple indexs
s1=pd.Series(12,index=[1,10])
s1

s2=pd.Series(12,index=[1,2,3,4,5,6])
s3=pd.Series(12,index=[1,2,3,4])
print(s2+s3)


# %%
py_list=[1,2,3,4,5,6,7,8,9]
var=pd.DataFrame(py_list)
print( var,type(var))

# %%
dictionar={
    "a":[1,2,3,4,5,6]
    ,
    "b":[1,2,3,4,4,5]
    ,
    "c":[6,7,8,9,0,0]
    ,
    "d":[11,22,3,4,5,88]
}
var1=pd.DataFrame(dictionar)
print(var1,type(var1))

#specific column 
var2=pd.DataFrame(dictionar,columns=["a","d"])
print(var2,type(var2))

#access by index
var3=pd.DataFrame(dictionar)
print(var3)
print()
print(var3["a"][4])



# %%
#using python list
py_list=[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
var=pd.DataFrame(py_list)
print(var,type(var))

# %%
#using python series
sr={
    "s":pd.Series([1,2,3,4,5]),"r":pd.Series([6,7,8,9,0])
}
var=pd.DataFrame(sr)
print(var,type(var))

# %%
#Arithmetic operation on pyhton pandas
var=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[7,8,9,1,2,3]})
print(f"{var}\n")
var["C"]=var["A"]+var["B"]
print(f"{var}\n")
var["C"]=var["A"]-var["B"]
print(f"{var}\n")
var["C"]=var["A"]*var["B"]
print(f"{var}\n")
var["C"]=var["A"]/var["B"]
print(f"{var}\n")

# %%
var1=pd.DataFrame({"A":[20,12,32,54,34],
                   "B":[45,22,55,21,11]})
var1["Result"]=var1["A"]<=20
var1

# %%
#Insert
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]
                  ,"C":[111,222,333,444,555]})
var
var.insert(1,"A_1",[1.1,2.2,3.3,4.4,5.5])
var

var["D"]=var["A"][:3]
var

# %%
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]
                  ,"C":[111,222,333,444,555]})
var1=var.pop("B")

print(f"Deleted Valus: \n{var1}")
print(f"Updated Values: \n{var}")

# %%
#Create Csv file
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]
                  ,"C":[111,222,333,444,555]})
print(var)

var.to_csv("Test.csv")
#to remove index from CSV file
var.to_csv("Test_Without_Index.csv",index=False)
#to change headers
var.to_csv("Test_changed_header.csv",header=["AA","BB","CC"])
var

# %%
#Read CSV files
csv_1=pd.read_csv("student_scores.csv")
print(csv_1)
csv_2=pd.read_csv("student_scores.csv", nrows=1) # print number of rows want
print(csv_2)
csv_3=pd.read_csv("student_scores.csv", usecols=["Math"]) #single column print
print(csv_3)
csv_4=pd.read_csv("student_scores.csv", usecols=[4,3]) #multiple columns print
print(csv_4)
csv_5=pd.read_csv("student_scores.csv", skiprows=[1]) #single row skip
print(csv_5)
csv_6=pd.read_csv("student_scores.csv", skiprows=[3,6,8]) #multiple skipping rows
print(csv_6)
csv_7=pd.read_csv("student_scores.csv", index_col=["Attendance"]) #change the inex with the any column
print(csv_7)
csv_8=pd.read_csv("student_scores.csv", header=3) #change the header to any row of the csv file
print(csv_8)
csv_9=pd.read_csv("student_scores.csv", names=["Student_Score"])
print(csv_9)
csv_10=pd.read_csv("student_scores.csv", names=["ID","NAME","MATH","SCIENCE","ENGLISH","ATTENDEANCE"])
print(csv_10)


# %%
csv_1=pd.read_csv("student_scores.csv")
# print(csv_1)
csv_2=pd.read_csv("student_scores.csv",dtype={"Math":"float","Science":"float","English":"float"} )
print(csv_2)

# %%
#pandas function
csv_1=pd.read_csv("student_scores.csv")
print(csv_1.index) #print range of index
print(csv_1.columns) #print all columns name
print(csv_1.describe()) # numerical columns calculate [count,mean,std,min,max etc]
#get data
print(csv_1.head()) #first 5 rows
print(csv_1.head(2))

print(csv_1.tail()) #last 5 rows
print(csv_1.tail(2))
print()
print(csv_1[:2]) # slicing
print(csv_1[2:5]) #

print(csv_1.index.array) #index into array
import numpy as np
print(csv_1.to_numpy) #csv_1 into numpy
v=np.asarray(csv_1) #csv_1 into numpy
print("Helo")
csv_1.sort_index(axis=0,ascending=False) 
#csv_1["Name"][0]="Anand"


# %%
#Access elements & Rows & Columns
csv_1=pd.read_csv("student_scores.csv")
print(csv_1.loc[:,["Math","Science"]])
print(csv_1.loc[[2,3],:])
print(csv_1.iloc[0,3])
print(csv_1.drop("English",axis=1))
print(csv_1.drop(8,axis=0))

# %%
# import pandas as pd
csv=pd.read_csv("handle.csv")
print(csv)

#dropna

print(csv.dropna()) # it delete the rows which have Nan
print(csv.dropna(axis=1)) # it delete the columns which have Nan

print(csv.dropna(how="any")) # it drops the rows which have Nan in any column
print(csv.dropna(how="all")) # it drops the rows which have Nan in all columns

print(csv.dropna(subset=["Department"])) #it drops the rows which have Nan in Department column

print(csv.dropna(inplace=True)) # reove rows which have Nan
print(csv.dropna(thresh=2))




# %%
csv=pd.read_csv("handle.csv")
print(csv)

# fillna

print(csv.fillna({"City":"Silvass", "Salary":20000}))

print(csv.ffill())
print(csv.ffill(axis=1))

print(csv.bfill())
print(csv.bfill(axis=1))



# %%
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Replace 'Alice' with 'Anna'
df['Name'] = df['Name'].replace('Alice', 'Anna')

print(df)

# %%
data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value1': [1, 2, 3, 4, 5],
    'Value2': [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Group by 'Category' and calculate mean of 'Value1'
grouped_df = df.groupby('Category').mean()

print(grouped_df)


# %%

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

# Concatenate vertically
concat_df_vertical = pd.concat([df1, df2])

print(concat_df_vertical)

# Concatenate horizontally
concat_df_horizontal = pd.concat([df1, df2], axis=1)

print(concat_df_horizontal)


# %%

left_df = pd.DataFrame({
    'Key': ['A', 'B'],
    'Value1': [1, 2]
})

right_df = pd.DataFrame({
    'Key': ['A', 'C'],
    'Value2': [3, 4]
})

# Join on 'Key'
join_df = pd.merge(left_df, right_df, on='Key')

print(join_df)


# %%

data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Subcategory': ['X', 'Y', 'Z', 'X', 'Y'],
    'Value': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot(index='Category', columns='Subcategory', values='Value')

print(pivot_table)



# %%
data = {
    'Country': ['USA', 'Canada'],
    'Year2019': [100, 50],
    'Year2020': [110, 60]
}

df = pd.DataFrame(data)

# Melt the DataFrame
melted_df = df.melt(id_vars='Country', var_name='Year', value_name='Value')

print(melted_df)



