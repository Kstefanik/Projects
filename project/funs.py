import mysql.connector

#funkcja, która sprawdza czy dany student należy do zadanej grupy i przeszukuje pozostałe jeśli nie znajdzie w zadanej

def which_group(student_id,db,groups,class_name):          
    mycursor = db.cursor()
    i = 0
    i_max = len(groups)
    
    while(True):
        
        group = groups[i]
        mycursor.execute(f"SELECT * FROM `{class_name}_CW{group}_attendance` WHERE student_id = {student_id}")
        
        if mycursor.fetchall() == []:
            i = i + 1
            
            if i == i_max:
                return 'brak w bazie'
                
            
            continue
        
        else:
            return group

