from src.utils.DateFormat import DateFormat


class User():
    def __init__(self, cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimineto) -> None:
        self.cedula_identidad = cedula_identidad
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimineto

    def to_JSON(self):
        return {
            'cedula_identidad': self.cedula_identidad,
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'fecha_nacimiento': DateFormat.conver_date(self.fecha_nacimiento)
        }
