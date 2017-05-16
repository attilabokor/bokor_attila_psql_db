import psycopg2
import psycopg2.extras



try:
    conn = psycopg2.connect("dbname='attila' user='attila' host='localhost' password='Orsolya1986'" )
except:
    print ("CONECTION ERROR")



def mentor_name():

        data=[]

        cur = conn.cursor()

        cur.execute("""SELECT first_name as "First Name", last_name as "Last Name" from mentors """)

        column_names = [desc[0] for desc in cur.description]
        
        rows = cur.fetchall()

        data.append(column_names)

        data.append(rows)

        print (data)
        




def mentor_nick():

        data=[]

        cur = conn.cursor()

        cur.execute("""SELECT nick_name FROM mentors WHERE city = 'Miskolc' """)
        
        column_names = [desc[0] for desc in cur.description]
        
        rows = cur.fetchall()

        data.append(column_names)

        data.append(rows)

        print (data)




def application_carol():

    data = []

    cur = conn.cursor()

    cur.execute("""
                   SELECT CONCAT(first_name, ' ', last_name) as "Full name", phone_number as "Phone number"
                    FROM applicants WHERE first_name='Carol'; """)

    column_names = [desc[0] for desc in cur.description]

    rows = cur.fetchall()

    data.append(column_names)

    data.append(rows)

    print (data)


def applicant_found_by_email():

    data = []

    cur = conn.cursor()

    cur.execute("""SELECT CONCAT(first_name, ' ', last_name) AS "Full Name", phone_number AS "Phone Number"
                   FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'; """)

    column_names = [desc[0] for desc in cur.description]

    rows = cur.fetchall()

    data.append(column_names)

    data.append(rows)

    print (data)




def new_applicant_insert():

    data = []

    cur = conn.cursor()

    cur.execute(""" INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                       VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823 ) """)

    cur.execute(""" SELECT * FROM applicants WHERE application_code=54823 """)


    column_names = [desc[0] for desc in cur.description]

    rows = cur.fetchall()

    data.append(column_names)

    data.append(rows)

    print (data)





def j_foreman_tel_number_update():

    data = []

    cur = conn.cursor()

    cur.execute(""" UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman' """)

    cur.execute(""" SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman' """)

    column_names = [desc[0] for desc in cur.description]

    rows = cur.fetchall()

    data.append(column_names)

    data.append(rows)

    print (data)



def del_data_via_email():

    cur = conn.cursor()    
    
    cur.execute(""" DELETE FROM applicants WHERE email LIKE '%@mauriseu.net'""")
    









mentor_name()
mentor_nick()
application_carol()
applicant_found_by_email()
new_applicant_insert()
j_foreman_tel_number_update()
del_data_via_email()



