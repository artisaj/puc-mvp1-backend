from app.database.connection import get_connection


class CorridaModel:
    @staticmethod
    def create(data_corrida, resultado_json):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO corridas (data_corrida, resultado_json) VALUES (?, ?)",
            (data_corrida, resultado_json),
        )
        connection.commit()
        new_id = cursor.lastrowid
        connection.close()
        return new_id

    @staticmethod
    def list_all():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, data_corrida, resultado_json FROM corridas ORDER BY id DESC")
        rows = cursor.fetchall()
        connection.close()
        return [dict(row) for row in rows]
