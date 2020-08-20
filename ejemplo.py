from logic import Logic
from categoria import categoriaObj


class CategoriaLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "categoria",
        ]

    def getAllCategorias(self):
        dataBase = self.get_databaseXObj()
        sql = "SELECT * FROM fishingdb1.categoria;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    def insertCategoria(self, categoria):
        database = self.get_databaseXObj()
        sql = f"insert into fishingdb1.categoria (categoria) values ('{categoria}');"
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCategoria(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from fishingdb1.categoria where categoria.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCategoria(self, id, categoria):
        database = self.get_databaseXObj()
        sql = f"update fishingdb1.categoria set categoria.categoria= '{categoria}' where categoria.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows
