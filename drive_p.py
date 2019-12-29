import psycopg2 as ps
import logging
from vk_pars import genTable

# logging.basicConfig(filename="drive.log", level=logging.INFO)
logger = logging.getLogger("drive_p:")


class driveBase(genTable):
    user = 'python_worker'
    passwd = '123123123'
    database = 'test_work'
    ISOLEVEL = 0
    conn = None
    host = "127.0.0.1"
    port = "5432"

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        try:
            self.conn = ps.connect(database=self.database,
                                   user=self.user,
                                   password=self.passwd,
                                   host=self.host,
                                   port="5432")

            self.conn.set_isolation_level(self.ISOLEVEL)
        except ps.DatabaseError as err:
            logger.warning("error creating database: %s", err)

    def insertDate(self, strs, arg):
        try:
            cursor = self.conn.cursor()
            cursor.execute(strs, arg)
        except ps.DatabaseError as err:
            logger.warning("error insert database: %s", err)
        else:
            self.conn.commit()

    def selectDate(self, sql_statement):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_statement)
            return cursor.fetchall()

        except ps.DatabaseError as err:
            logger.warning("Error selectDate: %s", err)

    def __del__(self):
        if self.conn != None:
            self.conn.close()


if __name__ == "__main__":
    dB = driveBase()
    # for i in dB.createStudent():
    #     dB.insertDate(""" INSERT INTO db.stydent (
    #               bookcheck,
    #               firstname,
    #               secondname,
    #               endname,
    #               kafedra ) VALUES (%s,%s,%s,%s,%s ) ;""", i)
    #
    # for i in dB.createTeachers(650):
    #     dB.insertDate(""" INSERT INTO db.teachers (
    #                       firstname,
    #                       secondname,
    #                       endname,
    #                       kafedra,
    #                       degree ) VALUES (%s,%s,%s,%s,%s ) ;""", i)
    #
    # for i in range(650):
    #     dB.insertDate(""" INSERT INTO db.filestats (
    #     fname,
    #     path ) VALUES (%s,%s ) ;""", dB._getFullPath())
    #
    # for i in range(650):
    #     dB.insertDate(""" INSERT INTO db.filestats (
    #     refteacher,
    #     groupid ) VALUES (%s,%s ) ;""", ())

    # for i in range(5):
    #     for j in range(5):
    #
    #         dB.insertDate(""" INSERT INTO db.commis (
    #                 refteacher,
    #                 groupid ) VALUES (%s,%s ) ;""", (dB._getCom(),i))
    # for i in range(5):
    #     for j in range(5):
    #
     #        dB.insertDate(""" INSERT INTO db.protocol (
     # refstudent,
     # refleadercommis,
     # refdirector,
     # reffile ) VALUES (%s,%s ) ;""", (dB._getCom(),i))

    # t1 = dB.selectDate("""SELECT
    #   filestats.id,
    #   teachers.id
    # FROM db.filestats
    # LEFT JOIN db.teachers ON db.teachers.id = db.filestats.id ;""")
    # t11=dB.selectDate("SELECT   stydent.bookcheck from db.stydent LIMIT 650")
    # t2=dB.selectDate("""SELECT DISTINCT ON (commis.groupid) groupid , commis.id FROM db.commis ORDER BY commis.groupid;""")
    #
    #
    # for i in range(650):
    #     dB.insertDate(""" INSERT INTO db.protocol (
    #        themwork,
    #        refstudent,
    #        refleadercommis,
    #        refdirector,
    #        reffile
    #     ) VALUES (%s,%s,%s,%s,%s ) ;""", (dB._getFNAME(),*t11[i],t2[i % len(t2)][1],*t1[i]))
