import psycopg2
import psycopg2.extras



try:
    conn = psycopg2.connect("dbname='attila' user='attila' host='localhost' password='Orsolya1986'" )
except:
    print ("CONECTION ERROR")


def show_mentor_table():

        data=[]

        cur = conn.cursor()

        cur.execute("""SELECT * FROM mentors """)

        column_names = [desc[0] for desc in cur.description]
        
        rows = cur.fetchall()

        data.append(column_names)

        data.append(rows)

        print (data)




def show_applicant_table():

        data=[]

        cur = conn.cursor()

        cur.execute("""SELECT * FROM applicants """)

        column_names = [desc[0] for desc in cur.description]
        
        rows = cur.fetchall()

        data.append(column_names)

        data.append(rows)

        print (data)



show_applicant_table()
show_mentor_table()

