from numpy.core.fromnumeric import shape
import pandas as pd
import csv
import numpy as np
from numpy import savetxt

df = pd.read_csv('final_stats.csv', sep=' ')
#print(df)

def get_column(ls, col_num, iteration_of_stats_printer_loop):
    y = []
    for i in ls:
        df2 = df.loc[df['NAME'] == i]

        if len(df2.iloc[:, 2]) != iteration_of_stats_printer_loop:     # if some column has less values then zeros will append in it
            var = iteration_of_stats_printer_loop - len(df2.iloc[:, 2]) # it will find how many values are less
            #print("number of zeros: ", var)
            #print(len(df2))
            #print(df2)
            for i in range(0,var):
                df2.loc[len(df2)] = 0       #this line is appinding zeros
            #print(len(df2))
            #print(df2)

        y.append(df2.iloc[:, col_num]) 
        #print(shape(df2))
        #print(type(df2))
        #print(len(df2.iloc[:, col_num]))        

    # print(type(y[1]))
    # print(len(y))
    # print(shape(y))
    return y


def column_concatenation(ls, container_count):

#     for i in range(0,20):
#         print(i,": ",shape(ls[i]))


    arr = np.array(ls[0])
    
    for i in range(1, container_count):                   #<..............................
        arr = np.c_[ arr, ls[i] ]

    #print(arr.shape)
    #print(shape(ls[0]))
    return arr

def numpy_to_csv(np_arr, file_name):
    #directory path where you want to send process files
    pd.DataFrame(np_arr).to_csv("stats_file/"+file_name+".csv",header=None, index=None, sep=',')


def insert_container_name_first_line(file_name_ls, row):
    #row = ['A','B','C','D']


    for filename in file_name_ls:

        print(filename)

        with open("stats_file/"+filename+".csv", 'r') as readFile:
            rd = csv.reader(readFile)
            lines = list(rd)
            lines.insert(0, row)

        with open("stats_file/"+filename+".csv", 'w',newline='') as writeFile:
            wt = csv.writer(writeFile)
            wt.writerows(lines)

        readFile.close()
        writeFile.close()


#...................[Main].........................


def main_fun(containers_names_ls, col_num, files_names, container_count, iteration_of_stats_printer_loop):


    for c_number,f_names in zip(col_num, files_names):
        
        ls2  = get_column(containers_names_ls, c_number, iteration_of_stats_printer_loop)       

        np_arr = column_concatenation(ls2, container_count)  

        #print("np_arr: ",np_arr)

        numpy_to_csv(np_arr, f_names) 

    insert_container_name_first_line(files_name, containers_names_ls)  

#..................................................................................................
        
containers_names_ls = list()

for i in df["NAME"]:
    #print(i)
    if i != "ID" and  i not in containers_names_ls:
        containers_names_ls.append(i)

print(containers_names_ls)
print("number of containers: ", len(containers_names_ls))

container_count = len(containers_names_ls)

 #Enter column number here you want to process
col_number = [2,3,4,5,6,7,8,9,10]
#Enter the name of the file that you want to process
files_name = ["CPU_%","MEM", "MEM_USAGE_LIMIT", "MEM_%", "NET_I", "NET_O", "BLOCK_I", "BLOCK_O","PIDS"]

# main_fun(containers_ids_ls, col_you_want_to_pick, files_from_these_column_you_want_to_genrate, iteration_of_stats_printer_loop)
main_fun(containers_names_ls, col_number, files_name, container_count, 16) 


