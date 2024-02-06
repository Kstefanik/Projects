import mysql.connector
import funs

#OPIS: Dodaje kolumnę o nazwie odpowiadającej zadanej dacie i zaznacza '1'(obecny) jeśli legitymacja została zeskanowana, domyślnie przy tworzeniu kolumny każdy ma w obecności '0'(nieobecny)


db = mysql.connector.connect(         #Baza danych
    host='',
    database='',
    user='',
    password='',
    port='')
mycursor = db.cursor()
scaned_list = []    #lista zeskanowanych id
groups = [1,2]      #numery grup przedmiotowych
    
            
today = input("Pojad datę: ")                                                                                                 
class_name = input("Podaj przedmiot: ")    #np AUE
group_id = int(input("Podaj nr grupy: "))           

while True:                                                 
                                                                                                                                    
    student_id = input("Nr. indexu: ")                                                                                       #Tu będzie system sczytywania nr indexu z legitki
    mycursor.execute(f"ALTER TABLE `{class_name}_CW{group_id}_attendance` ADD COLUMN `{today}` VARCHAR(20) DEFAULT '0';")    #Dodaje kolumnę o dzisiejszej dacie(np. 2023-12-12 == nazwa kolumny)

    if student_id not in scaned_list:                                                                                        #Sprawdza czy dane id nie było już skanowane
            
        if funs.which_group(student_id,db,groups,class_name) != group_id:                                                   #Sprawdza czy dany student należy do zadanej grupy
            print(f"Student z grupy: {funs.which_group(student_id,db,groups,class_name)}")        # TO DO: co jeśli student jest spoza zadanej grupy
            
            
        mycursor.execute(f"UPDATE `{class_name}_CW{group_id}_attendance` SET `{today}` = '1' WHERE student_id = '{student_id}'")    #Dodaje '1'(obecność) do bazy danych
        scaned_list.append(student_id)
        
    else:
        continue
        
    db.commit()

mycursor.close()
db.close()
    
   