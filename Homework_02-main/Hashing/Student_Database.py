from HashTable import *

import csv
import os

def create_studentDatabase(studentRecords):
    hashtable_size = 7
    hashtable = create_hashtable(hashtable_size)
    for record in studentRecords:
        key = record['ID']
        put(hashtable, key, record, hashtable_size)
    return hashtable    

def perform_Operations(H, operationFile):
    collision_path = {}
    op_number = 1
    with open(operationFile, 'r') as file:
        for line in file:
            op = line.strip().split()
            if op[0] == 'Find':
                key = op[1]
                get(H, key, len(H[0]), collision_path, op_number)
            elif op[0] == 'Update':
                key = op[1]
                column_name = op[2]
                data = ' '.join(op[3:])
                Update(H, key, column_name, data, len(H[0]), collision_path, op_number)
            elif op[0] == 'Delete':
                key = op[1]
                delete(H, key, len(H[0]), collision_path, op_number)
            op_number += 1
    return collision_path

            

#import pandas as pd

#df = pd.read_csv("C:/Users/haide/OneDrive/Desktop/Homework_02-main/Hashing/data.csv")


'''def main(filename):


    student_records = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            student_records.append(row)
    return student_records

if __name__ == "__main__":
    directory_path = r'C:\Users\haide\OneDrive\Desktop\Homework_02-main'
    file_path = os.path.join(directory_path, 'data.csv')
    student_records = main(file_path)




"""SNo,ID,FirstName,LastName,Sex,Email,Phone,Department
1,88F7B33d2bcf9f5,Shelby,Terrell,Male,elijah57@example.net,001-084-906-7849,CS

    student_records = []
    with open(filename) as file:
        key= ["SNo","ID","FirstName","LastName","Sex","Email","Phone","Department"]

        first= file.readline()"""

studentRecords=main('data.csv')
H=create_studentDatabase(studentRecords)
print(perform_Operations('Operations.txt'))'''


def main(filename):
    try:
        student_records = []
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                student_records.append(row)
        return student_records
    except FileNotFoundError:
        print(f"File not found: '{filename}'")
        return None

# Example usage:
if __name__ == "__main__":
    # Constructing the full path to data.csv file
    directory_path = 'C:\\Users\\haide\\OneDrive\\Desktop\\Homework_02-main'
    file_path = directory_path + '\\data.csv'  # Appending the file name to the directory path
    student_records = main(file_path)
    if student_records:
        print("Student records loaded successfully.")
    else:
        print("Failed to load student records. Exiting...")
