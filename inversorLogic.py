from logic import Logic
from inversorObj import inversorObj


class inversorLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "biografia",
            "email",
            "id_usuario",
            "pais",
            "ciudad",
        ]

    # Metodo insert
    def insertNewInversor(self, name, bio, email, id_user, country, city):
        database = self.get_databaseXObj()
        sql = (
            f"insert into fishingdb1.inversionista (id, nombre, biografia, email, id_usuario, pais, ciudad) "
            + f"values (0, '{name}', '{bio}', '{email}', {id_user},'{country}','{city}');"
        )
        # sql = f"insert into fishingdb.categoria (categoria) values ('{categoria}');"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getNewInversor(self, name, bio, email, id_user, country, city):
        dataBase = self.get_databaseXObj()
        sql = (
            "select * from fishingdb1.inversionista " + f"where id_usuario = {id_user};"
        )
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            invObj = inversorObj(
                data_dic["id"],
                data_dic["nombre"],
                data_dic["biografia"],
                data_dic["email"],
                data_dic["id_usuario"],
                data_dic["pais"],
                data_dic["ciudad"],
            )
            return invObj
        else:
            return None

    def insertNewInteres(self, interes, idInversor):

        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb1.interes (id, id_inversionista, id_categoria) "
            + f"values (0, {idInversor}, {interes});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # Metodo get all
    def getAllInversionista(self):
        dataBase = self.get_databaseXObj()
        sql = "SELECT * FROM fishingdb1.inversionista;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    # Metodo delete
    def deleteInversionista(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from fishingdb1.inversionista where inversionista.id = '{id}';"
        row = database.executeNonQueryRows(sql)
        return row

    # Metodo update
    def updateInversionista(self, id, name, bio, email, id_user, country, city):
        database = self.get_databaseXObj()
        sql = f"update fishingdb1.inversionista set inversionista.nombre= '{name}', inversionista.biografia= '{bio}', inversionista.email= '{email}', inversionista.id_usuario= '{id_user}', inversionista.pais= '{country}', inversionista.ciudad= '{city}' where inversionista.id = '{id}';"
        row = database.executeNonQueryRows(sql)
        return row
