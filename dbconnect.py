import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="really_hard_p_word")
    c = conn.cursor()

    return c, conn