from sqlalchemy import create_engine, inspect, text

class TableClass:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_users(self):
        connection = self.db.connect()
        result = connection.execute(text("SELECT * FROM users"))
        rows = result.mappings().all()
        connection.close()
        return rows

    def delete(self, user_id):
        connection = self.db.connect()
        connection.execute(text("DELETE FROM users WHERE user_id =:user_id"), {"user_id": user_id})
        connection.commit()
        connection.close()


    def create_user(self, user_id, user_email, subject_id):
        connection = self.db.connect()
        sql = text("""
                INSERT INTO users (user_id, user_email, subject_id)
                VALUES (:user_id, :user_email, :subject_id)
            """)
        result = connection.execute(sql, {'user_id': user_id, 'user_email': user_email, 'subject_id': subject_id})
        connection.commit()
        connection.close()

    def update_user(self, new_email, id):
        connection = self.db.connect()
        sql = text("UPDATE users SET user_email = :new_email WHERE user_id = :id")
        result = connection.execute(sql, {"new_email": new_email, "id": id})
        connection.commit()
        connection.close()

    def get_user_by_id(self, user_id):
        connection = self.db.connect()
        sql = text("SELECT * FROM users WHERE id =:select_id")
        result = connection.execute(sql, {"select_id": user_id})
        rows = result.mappings().all()
        connection.close()
        return rows

