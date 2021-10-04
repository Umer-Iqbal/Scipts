from numpy.core.fromnumeric import shape
import pandas as pd
import csv
import numpy as np
from numpy import savetxt

df = pd.read_csv('stats36.csv', sep=' ')
#print(df)

def get_column(ls, col_num):
    y = []
    for i in ls:
        df111 = df.loc[df['CONTAINER ID'] == i]
        y.append(df111.iloc[:, col_num]) 
        #print(y)
    return y


def column_concatenation(ls):

    arr2 = np.array(ls[1])

    print("arr2.shape: ",shape(arr2))
    arr3 = np.zeros(198)
    #print(shape(arr3))

    arr2 = np.concatenate((arr2,arr3), axis=0, out=None)
    #print(shape(arr2))

    arr = np.array(ls[0])
    print("arr2.shape: ",shape(arr))
    arr = np.c_[ arr, arr2 ]

    
    
    #print(shape(ls[1]))

    for i in range(2,20):
        arr = np.c_[ arr, ls[i] ]

    print(arr.shape)
    #print(arr)

    return arr

def numpy_to_csv(np_arr, file_name):
    #directory path where you want to send process files
    pd.DataFrame(np_arr).to_csv("/home/hut/Documents/stats_of_diff_container/"+file_name+".csv",header=None, index=None, sep=',')


#...................[Main].........................


def main_fun(containers_ls, col_num, files_names):


    for c_number,f_names in zip(col_num, files_names):
        
        ls2  = get_column(containers_ls, c_number)       

        np_arr = column_concatenation(ls2)  

        numpy_to_csv(np_arr, f_names)   



#Enter the containers id you want to extract or want to process
containers_ids_ls = ["31cb109cbd8c","4fa522acd82d","1dde2b0fbfdc","d41abce9cb6d","203dc851872f","b6547ac1192a","b01c86d4c49c",
"58fb53d3faed","7b3ddf825f80","36560e917e73","892bcdffdfa7","4be3467c6777","51c842ef19bd","6f90968b7c1e","3fb2625ac442",
"cbf80c5f523c","87d796c8e2c1","fd5736e9c579","64cf55cd9975","7470e5918d52"]
 #Enter column number here you want to process
col_number = [2,3,4,5,6,7]
#Enter the name of the file that you want to process
files_name = ["CPU_%", "MEM_USAGE_LIMIT", "MEM_%", "NET_IO", "BLOCK", "PIDS"]

main_fun(containers_ids_ls, col_number, files_name)


































# arr2 = np.array(y[1])

# print(shape(arr2))
# arr3 = np.zeros(923)
# print(shape(arr3))

# arr2 = np.concatenate((arr2,arr3), axis=0, out=None)
# print(shape(arr2))

# arr = np.array(y[0])
# arr = np.c_[ arr, arr2 ]





























#savetxt('/home/hut/Documents/csv_file4.csv', arr, delimiter=',')


#print(y[0])

#y[0].to_csv('/home/hut/Documents/csv_file3.csv', sep=' ', index=False, encoding='utf-8')


#y[1].to_csv('/home/hut/Documents/csv_file3.csv', sep=' ', columns='C', index=False, encoding='utf-8')
#df = pd.read_csv("/home/hut/Documents/csv_file3.csv")
# with open('/home/hut/Documents/csv_file3.csv', 'a') as f:
#     y[1].to_csv(f, header=False)






# df = pd.read_csv("/home/hut/Documents/csv_file3.csv")
# df["new_column"] = y[1]
# df.to_csv("/home/hut/Documents/csv_file3.csv", )
    

#print("df2",df2)
#print(type(df2))

#df2.to_csv('/home/hut/Documents/csv_file.csv', sep=' ', encoding='utf-8')

#df2.columns = ['']
#df2.columns = ["CONTAINER ID",'NAME']



# y = df2.iloc[:, [2]]
# y.to_csv('/home/hut/Documents/csv_file2.csv', sep=' ', encoding='utf-8')
# print(y)



# df2 = df.loc[df['CONTAINER ID'] == "d6804e96d85f"]
# df3 = df.loc[df['CONTAINER ID'] == "ff19ae6a650a"]
# df4 = df.loc[df['CONTAINER ID'] == "c9ee2b642633"]
# df5 = df.loc[df['CONTAINER ID'] == "e872cd7b3608"]
# df6 = df.loc[df['CONTAINER ID'] == "2067a41f8631"]
# df7 = df.loc[df['CONTAINER ID'] == "a8742b9e27b8"]
# df8 = df.loc[df['CONTAINER ID'] == "6ae41ac791ef"]
# df9 = df.loc[df['CONTAINER ID'] == "479be5cf1711"]
# df10 = df.loc[df['CONTAINER ID'] == "f616c36d2711"]
# df11 = df.loc[df['CONTAINER ID'] == "fa1b937aaca9"]
# df12 = df.loc[df['CONTAINER ID'] == "aa65fc6a0059"]
# df13 = df.loc[df['CONTAINER ID'] == "a5a6b96f27b2"]
# df14 = df.loc[df['CONTAINER ID'] == "00e3bda124c0"]
# df15 = df.loc[df['CONTAINER ID'] == "aa77a83d496d"]
# df16 = df.loc[df['CONTAINER ID'] == "f3bb1c1310b4"]
# df17 = df.loc[df['CONTAINER ID'] == "891d18bc87ca"]
# df18 = df.loc[df['CONTAINER ID'] == "2a462109ce41"]
# df19 = df.loc[df['CONTAINER ID'] == "d28adab8a798"]
# df20 = df.loc[df['CONTAINER ID'] == "f61fffbdaf0c"]
# df21 = df.loc[df['CONTAINER ID'] == "29748380ca50"]
