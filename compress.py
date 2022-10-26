class Compress:
    def __init__(self):
        self.tokens = []
        self.num = []
        self.values = {}
        self.compressed = []

    def compress(self, text):
        # Separar cada token y añadirlo a una lista.
        for token in text.split(" "):
            if token not in self.tokens:
                self.tokens.append(token)
        
        # Crear una lista enumerando los tokens.
        for token in self.tokens:
            self.num.append(self.tokens.index(token)+1)
        
        # Crear el diccionario de valores para cada token.
        for i in range(len(self.tokens)):
            self.values[self.tokens[i]] = self.num[i]
        
        # Traducir cada palabra a su valor y agregarlo a la lista self.compressed.
        for token in text.split(" "):
            self.compressed.append(self.values[token])
        
        return self.compressed, self.values

    def uncompress(self, compressed, values):
        # Traducir valores de compressed a tokens.
        text = ""
        for i in compressed:
            for key, value in values.items():
                if i == value:
                    text += key + " "
        return text.rstrip()