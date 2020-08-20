from logic import Logic
from userLogic import UserLogic
from emprendedorLogic import emprendedorLogic
from emprendedorObj import emprendedorObj
from emprendimientoLogic import emprendimientoLogic
from emprendimientoObj import emprendimientoObj


class fundadorLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "biografia",
            "nombreEmp",
            "id_emprendedor",
            "id_emprendimiento",
        ]

    def getAllFundadores(self):
        dataBase = self.get_databaseXObj()
        sql = (
            "select fishingdb1.fundador.id, fishingdb1.emprendedor.nombre, fishingdb1.emprendedor.biografia, fishingdb1.emprendimiento.nombre, "
            + "fishingdb1.emprendedor.id, fishingdb1.emprendimiento.id from fishingdb1.fundador "
            + "inner join fishingdb1.emprendedor  on fishingdb1.fundador.id_emprendedor = fishingdb1.emprendedor.id "
            + "inner join fishingdb1.emprendimiento on fishingdb1.fundador.id_emprendimiento = fishingdb1.emprendimiento.id;"
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    def insertNewFundador(self, user, name):

        id_usuario = UserLogic()
        usuario = id_usuario.getUserByUser(user)

        infoEmprendedor = emprendedorLogic()
        id_emprendedor = infoEmprendedor.getEmprendedorByUser(usuario.getId())

        infoEmprendimiento = emprendimientoLogic()
        id_emprendimiento = infoEmprendimiento.getEmprendimientoByName(name)

        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.fundador (id, id_emprendedor, id_emprendimiento) "
            + f"values (0, {id_emprendedor.getId()}, {id_emprendimiento.getId()});"
        )
        print(sql)
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteFundador(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from fishingdb.fundador where fundador.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateFundador(self, id, user, name):

        id_usuario = UserLogic()
        usuario = id_usuario.getUserByUser(user)

        infoEmprendedor = emprendedorLogic()
        id_emprendedor = infoEmprendedor.getEmprendedorByUser(usuario.getId())

        infoEmprendimiento = emprendimientoLogic()
        id_emprendimiento = infoEmprendimiento.getEmprendimientoByName(name)

        database = self.get_databaseXObj()
        sql = (
            f"update fishingdb.fundador set fundador.id_emprendedor= {id_emprendedor.getId()}, "
            + f"fundador.id_emprendimiento={id_emprendimiento.getId()} where fundador.id = '{id}';"
        )
        print(sql)
        rows = database.executeNonQueryRows(sql)
        return rows

