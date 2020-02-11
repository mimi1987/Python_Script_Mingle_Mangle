class FileReader():
    def __init__(self, file):
        self.__file = file
    
    def lines(self):
        lines = []
        with open(self.__file, 'r') as file:
            for line in file:
                lines.append(line.strip())
        return lines
    
class CsvReader(FileReader):
    def lines(self, sep):
        lines = []
        self.__sep = sep
        for field in super().lines():
            lines.append(field.split(sep))
        return lines
        
f = FileReader("./datei.csv")
print(f.lines())

f = CsvReader("./datei.csv")
print(f.lines(','))
