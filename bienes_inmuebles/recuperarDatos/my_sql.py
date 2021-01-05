
class My_sql():
    @staticmethod
    def intancias_bbdd(bbdd_server = "localhost", bbdd_user= "root",bbdd_pass="1234", bbdd_name="db_proyecto_miriadax"):
        return bbdd_server , bbdd_user, bbdd_pass, bbdd_name
