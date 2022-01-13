import csv

def write_info_csv(info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()== 0:
            writer.writerow(["Name","Age","Contact Number","Email ID"])
        
        writer.writerow(info_list)


if __name__=="__main__":
    condition=True
    student_num=1
    while (condition):
        
        student_info=input("\nPlease enter the information for student {} in the following format [Name, Age, Contact Number, Email ID]: ".format(student_num))
        
        #Split of input
        student_info_list=student_info.split(" ")
        print("\nThe entered infromation is -- \nName: {}\nAge: {}\nContact Number: {}\nEmail ID: {}"
                .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("\nIs the entered information correct? (yes/no): ")
        if choice_check=="yes":
            write_info_csv(student_info_list)
            student_num+=1

            condition_check=input("\nDo you want to enter another student information (yes/no):")
            print(condition_check)
            
            if condition_check=="yes":
                condition=True
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\nKindly re-enter the information")