from app.database.connection import get_connection


class PilotoModel:
    @staticmethod
    def create(nome, numero_kart, equipe=None):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO pilotos (nome, numero_kart, equipe) VALUES (?, ?, ?)",
            (nome, numero_kart, equipe),
        )
        connection.commit()
        new_id = cursor.lastrowid
        connection.close()
        return new_id

    @staticmethod
    def list_all():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nome, numero_kart, equipe, created_at FROM pilotos ORDER BY id")
        rows = cursor.fetchall()
        connection.close()
        return [dict(row) for row in rows]

    @staticmethod
    def get_by_id(piloto_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, nome, numero_kart, equipe, created_at FROM pilotos WHERE id = ?",
            (piloto_id,),
        )
        row = cursor.fetchone()
        connection.close()
        return dict(row) if row else None

    @staticmethod
    def delete(piloto_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM pilotos WHERE id = ?", (piloto_id,))
        connection.commit()
        affected = cursor.rowcount
        connection.close()
        return affected > 0
