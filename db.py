import mysql.connector
"""
This is the sql create statements. 
"""
# Create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wahid0616",
  database="Project1"
)

mycursor = mydb.cursor()

"""

mycursor.execute("CREATE TABLE Department (name VARCHAR(255), location INTEGER(15), Manager_Number INTEGER(15), Start_date VARCHAR(255) )")
mycursor.execute("CREATE TABLE Dept_location (dept_number INTEGER(15), location VARCHAR(255) )")

mycursor.execute("CREATE TABLE Employee (name VARCHAR(255), middle_I VARCHAR(10), Last_Name VARCHAR(50), Employee_Number INTEGER(15), Bday VARCHAR(255), Address VARCHAR(255), Gender VARCHAR(2), Salary INTEGER(15), Supervisor_Number INTEGER(15), Dept_Number INTEGER(2) )")
mycursor.execute("CREATE TABLE Project (name VARCHAR(255), Project_Number INTEGER(5), Location VARCHAR(255), Dept_Num INTEGER(5) )")
mycursor.execute("CREATE TABLE Works_on (Employee_Num INTEGER(15), Project_Number INTEGER(5), Hours FLOAT(10) )")
"""
"""
f = open("DEPARTMENT.txt", "r")





for readline in f:
    list_A=readline.split(",")
    x=list_A[0].replace("'",'')
    y=list_A[3].replace("'",'')
    z=list_A[2].replace("'",'')
    print(x)


    #sql="INSERT INTO Department (name,location,Manager_Number,Start_date) VALUES (%s,%s,%s,%s)"
    #val=(x,list_A[1],z,y)
    #mycursor.execute(sql,val)
    #mydb.commit()
"""
