from app import db
from passlib.hash import bcrypt

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # admin or default
    senha_hash = db.Column(db.String(255), nullable=False)

    atendimentos = db.relationship('Appointment', backref='usuario', lazy=True)

    def set_password(self, senha):
        self.senha_hash = bcrypt.hash(senha)

    def check_password(self, senha):
        return bcrypt.verify(senha, self.senha_hash)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'nome': self.nome,
            'tipo': self.tipo
        }
