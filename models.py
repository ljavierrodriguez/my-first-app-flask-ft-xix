from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Todo(db.Model):
    __tablename__ = 'todos'
    username = db.Column(db.String(120), primary_key=True)
    tasks = db.Column(db.Text(), nullable=False)

    def serialize(self):
        return {
            "tasks": self.tasks
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()