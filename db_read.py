"""
Safi Ullah
Muhammad Daud
Kyal Nyugen
user screenshare to code together
"""
import mysql.connector

# Create connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wahid0616",
  database="Project1"
)

mycursor = mydb.cursor()

'''

Retieve the emplyee names and the count of emplyees that work under them
'''
sql="SELECT Manager_Number FROM Department"


'''
mycursor.execute(sql)
myresult=mycursor.fetchall()

supervisors = []
for x in myresult:
    supervisors.append(x[0])
f_name = []
l_name = []
sup_count = []
for x in supervisors:
    sql="SELECT name,Last_name FROM Employee WHERE Employee_Number='{}'"
    sql2 = sql.format(x)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    for x in myresult:
        tup = x
        f_name.append(str(tup[0]))
        l_name.append(str(tup[1]))


for r in supervisors:
    sql="SELECT * FROM Employee WHERE Supervisor_Number='{}'"
    sql3 = sql.format(r)
    mycursor.execute(sql3)
    myresult=mycursor.fetchall()
    sup_count.append(len(myresult))

for i in range(len(sup_count)):
    min_idx =i
    for j in range(i+1,len(sup_count)):
        if sup_count[min_idx] > sup_count[j]:
            min_idx = j
    sup_count[i],sup_count[min_idx] = sup_count[min_idx],sup_count[i]
    f_name[i],f_name[min_idx] = f_name[min_idx],f_name[i]
    l_name[i],l_name[min_idx] = l_name[min_idx],l_name[i]


order_r=[]
k = len(sup_count)-1
while k != -1:
    order_r.append((f_name[k],l_name[k],sup_count[k]))
    k-=1
print(order_r)


'''



















'''
number 7) decending order

sql="SELECT name,Manager_Number FROM Department"



mycursor.execute(sql)
myresult=mycursor.fetchall()
dept = []
emp_num = []
order_l = []
count_emp_l = []
for x in myresult:
    tup = x
    dept.append(str(tup[0]))
    emp_num.append(tup[1])


for i in emp_num:
    sql="SELECT name FROM Employee WHERE Supervisor_Number='{}'"
    sql2 = sql.format(i)
    mycursor.execute(sql2)
    myresult1=mycursor.fetchall()
    count_emp_l.append(len(myresult1)+1)



for i in range(len(count_emp_l)):
    min_idx =i
    for j in range(i+1,len(count_emp_l)):
        if count_emp_l[min_idx] > count_emp_l[j]:
            min_idx = j
    count_emp_l[i],count_emp_l[min_idx] = count_emp_l[min_idx],count_emp_l[i]
    dept[i],dept[min_idx] = dept[min_idx],dept[i]



k = len(count_emp_l)-1
while k != -1:
    order_l.append((dept[k],count_emp_l[k]))
    k-=1
print(order_l)

'''



























'''

dname=raw_input("Enter department name: ")


str=(dname,)

sql="SELECT Manager_Number FROM Department WHERE name=%s"



mycursor.execute(sql,str)
myresult=mycursor.fetchall()
tup=myresult[0]



sql="SELECT name,Salary FROM Employee WHERE Supervisor_Number=%s"
mycursor.execute(sql,tup)
myresult1=mycursor.fetchall()

Salarytotal=0
for x in myresult1:

    Salarytotal+=x[1]




sql="SELECT name,Salary FROM Employee WHERE Employee_Number=%s"
mycursor.execute(sql,tup)
myresult6=mycursor.fetchall()

tup = myresult6[0]
Salarytotal =  Salarytotal + tup[1]
print "Total Salary in the department is ",
print(Salarytotal)
'''






















'''
#search for lastname firstname to get hours and project name
fullname=raw_input("Enter full name (lastname firstname): ")
fullname=fullname.split(" ")
sql="SELECT Last_Name,Employee_Number FROM Employee WHERE name='{0}'"
sql1=sql.format(fullname[1])
mycursor.execute(sql1)
myresult=mycursor.fetchall()
id=0
for x in myresult:
    tup=x
    if(tup[0]==" "+fullname[0]):
        id=tup[1]

sql="SELECT Project_Number,Hours FROM Works_on WHERE Employee_Num='{0}'"
sql1=sql.format(id)
mycursor.execute(sql1)
myresult2=mycursor.fetchall()

hours = 0
for x in myresult2:
    tup = x
    hours = tup[1]
    sql="SELECT name FROM Project WHERE Project_Number='{0}'"
    sql1=sql.format(tup[0])
    mycursor.execute(sql1)
    myresult=mycursor.fetchall()
    tup=myresult[0]
    projectname=tup[0]
    print "Name: "+fullname[0]+", "+fullname[1]+", Projectname: "+projectname+", Hours: "+str(hours)
'''





















#Retrieves name and salary from department
dname=raw_input("Enter department name: ")


str=(dname,)

sql="SELECT Manager_Number FROM Department WHERE name=%s"



mycursor.execute(sql,str)
myresult=mycursor.fetchall()
tup=myresult[0]



sql="SELECT name,Salary FROM Employee WHERE Supervisor_Number=%s"
mycursor.execute(sql,tup)
myresult1=mycursor.fetchall()



for x in myresult1:

    print "Name: "+x[0]+", Salary: ",
    print(x[1])





sql="SELECT name,Salary FROM Employee WHERE Employee_Number=%s"
mycursor.execute(sql,tup)
myresult6=mycursor.fetchall()


for x in myresult6:

    print "Name: "+x[0]+", Salary: ",
    print(x[1])















"""
f = open("EMPLOYEE.txt", "r")





for readline in f:

    list_A=readline.split(",")
    list_A[0]=list_A[0].replace("'",'')
    list_A[1]=list_A[1].replace("'",'')
    list_A[2]=list_A[2].replace("'",'')
    list_A[3]=list_A[3].replace("'",'')
    list_A[4]=list_A[4].replace("'",'')
    list_A[5]=list_A[5].replace("'",'')
    list_A[6]=list_A[6].replace("'",'')
    list_A[7]=list_A[7].replace("'",'')
    list_A[8]=list_A[8].replace("'",'')
    list_A[10]=list_A[10].replace("'",'')

    list_b=[]
    str=list_A[5]+" "+list_A[6]+" "+list_A[7]
    for i in range(0,12):

        if(i==5):
            list_b.append(str)
        elif(i==6 or i==7):
            continue
        else:
            list_b.append(list_A[i])

    for x in range(0,len(list_b)):
        if(list_b[x]==' null'):
            list_b[x]='-1'



    sql="INSERT INTO Employee (name,middle_I,Last_Name,Employee_Number,Bday,Address,Gender,Salary,Supervisor_Number,Dept_Number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(list_b[0],list_b[1],list_b[2],list_b[3],list_b[4],list_b[5],list_b[6],list_b[7],list_b[8],list_b[9])


    mycursor.execute(sql,val)
    mydb.commit()"""


























"""

table for works_on
f = open("WORKS_ON.txt", "r")





for readline in f:
    list_A=readline.split(",")
    x=list_A[0].replace("'",'')



    list_A[2]
    sql="INSERT INTO Works_on (Employee_Num,Project_Number,Hours) VALUES (%s,%s,%s)"
    val=(x,list_A[1],float(list_A[2]))
    mycursor.execute(sql,val)
    mydb.commit()



"""













"""
table for project
f = open("PROJECT.txt", "r")





for readline in f:
    list_A=readline.split(",")
    x=list_A[0].replace("'",'')
    z=list_A[2].replace("'",'')



    sql="INSERT INTO Project (name,Project_number,Location,Dept_Num) VALUES (%s,%s,%s,%s)"
    val=(x,list_A[1],z,list_A[3])
    mycursor.execute(sql,val)
    mydb.commit()
"""








"""
putting data into Dept_location table

f = open("DEPT_LOCATIONS.txt", "r")





for readline in f:
    list_A=readline.split(",")

    y=list_A[1].replace("'",'')




    sql="INSERT INTO Dept_location (dept_number, location) VALUES (%s,%s)"
    val=(list_A[0],y)
    mycursor.execute(sql,val)
    mydb.commit()
    """



















"""
this is to update department table

f = open("DEPARTMENT.txt", "r")





for readline in f:
    list_A=readline.split(",")
    x=list_A[0].replace("'",'')
    y=list_A[3].replace("'",'')
    z=list_A[2].replace("'",'')
    print(x)


    sql="INSERT INTO Department (name,location,Manager_Number,Start_date) VALUES (%s,%s,%s,%s)"
    val=(x,list_A[1],z,y)
    mycursor.execute(sql,val)
    mydb.commit()"""
