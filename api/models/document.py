class Document:
    """
    Representa un documento con un identificador, hora del sistema y dos listas (una no ordenada y otra ordenada).

    Attributes:
        id (str): Identificador del documento.
        hora_sistema (str): Hora en la que se creó o procesó el documento.
        lista_no_ordenada (list): Lista que no está ordenada.
        lista_ordenada (list): Lista que está ordenada.
    """
    
    def __init__(self, id: str, hora_sistema: str, lista_no_ordenada: list, lista_ordenada: list):
        """
        Inicializa una instancia de la clase Document.

        Args:
            id (str): Identificador del documento.
            hora_sistema (str): Hora en la que se creó o procesó el documento.
            lista_no_ordenada (list): Lista que no está ordenada.
            lista_ordenada (list): Lista que está ordenada.
        """
        self.id = id
        self.hora_sistema = hora_sistema
        self.lista_no_ordenada = lista_no_ordenada
        self.lista_ordenada = lista_ordenada

    def to_dict(self):
        """
        Convierte el objeto Document en un diccionario.

        Returns:
            dict: Un diccionario con las claves 'id', 'hora_sistema', 'lista_no_ordenada', y 'lista_ordenada'.
        """
        return {
            "id": self.id,
            "hora_sistema": self.hora_sistema,
            "lista_no_ordenada": self.lista_no_ordenada,
            "lista_ordenada": self.lista_ordenada
        }
