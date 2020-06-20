#Prescription form
import datetime
#*************************** Creating list to use formating ***********************************
# info list contains basic details like age, weight, sex ,illness , name etc

info_li = []
treatment_li = []
medicines = []
foods_to_eat = []
foods_to_avoid = []
filename = []

print("           ~~~~~~~~ FAITH HOSPITAL ~~~~~~~~            ")

td = datetime.date.today()

name = input("Name : ")
filename.append(name)           #to use patient name as file name we need to store his name into a list

file = open("{}.txt".format(filename[0]),'w') #to create patient name as file name

age = input("Age : ")
weight = input("Weight : ")
address = input("Address : ")
phone = input("Mobile : ")
sex = input("Sex : ")
illness = input("Illness in Breif : ")
medical_history = input("Medical History : ")

treatment_explain = input("Describe about treatment and illness : ")
treatment_li.append(treatment_explain)

info_li.extend((name, age,sex,weight,address,illness,medical_history,phone,td) )

while True:
    medicine = input("Enter name of Medicines Given : ")
    if medicine == "/":
        break
    else:
        medicines.append(medicine)

while True:
    foods = input("Enter name of foods to eat most : ")
    if foods == "/":
        break
    else:
        foods_to_eat.append(foods)


noteli = []
note = input("Give Special Note : ")
noteli.append(note)

#************************** Prescription Format *******************************************

file.write(("                  FAITH HOSPITAL          \n"
            "Phone : +91 987655432           Email : faith@hospital.com\n"
            "__________________________________________________________\n"
            "                   Patient Details             \n"
            "       Name : {}      Age : {}     Sex : {}    \n"         
            "       Weight : {}        Address : {}\n"
            "       Phone : {}          Date : {}\n"  
            "       Illness : {}     Medical History : {}\n"
            "__________________________________________________________\n"
            "About illness : {} \n"
            "\n"
            "Medicines Given :\n"

            ).format(info_li[0],info_li[1],info_li[2],info_li[3],info_li[4],info_li[7],info_li[8],info_li[5],info_li[6],treatment_li[0]))


for i in range(0,len(medicines)):
    file.write(("- {} \n").format(medicines[i]))


file.write((  "\n" "Foods to Eat : \n"))


for i in range(0,len(foods_to_eat)):
    file.write(("- {} \n".format(foods_to_eat[i])))

file.write(("\n Note : {} \n").format(noteli[0]))

file.write(("            ~~~~ Get Well Soon ~~~~            "))
