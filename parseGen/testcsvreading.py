import pandas as pd


#create a method that takes a range (chunks of ten chars that go with a step of 5, 25 chunks in total) that does the exact same thing but only for that range
#then create a method that takes a range (chunks of ten chars that go with a step of 5, 25 chunks in total) that does the exact same thing but only for that range


class DNAPermutations:
    def __init__(self, file):
        self.file = file
        self.df = pd.read_csv(self.file)
        self.string = self.df['string_a_modificar'][0]
        self.alterations = self.df['alteracion']
        self.positions = self.df['posicion']
        self.permutations = []
        self.permutations.append(self.string)
        self.generate_permutations()
        self.df_output = pd.DataFrame({'string_original': self.permutations, 'string_alterado': self.permutations, 'permutaciones': self.permutations})
        self.df_output.to_csv('output.csv', index=False)

    def generate_permutations(self):
        for i in range(len(self.positions)):
            for j in range(len(self.permutations)):
                self.permutations.append(self.permutations[j][:self.positions[i]] + self.alterations[i] + self.permutations[j][self.positions[i]+1:])
        self.permutations = self.permutations[1:]

    def generate_permutations_by_range(self, start, end):
        for i in range(start, end):
            for j in range(len(self.permutations)):
                self.permutations.append(self.permutations[j][:self.positions[i]] + self.alterations[i] + self.permutations[j][self.positions[i]+1:])
        self.permutations = self.permutations[1:]
#Ejecutar el código con el archivo .csv como argumento

DNAPermutations('data/dataset.csv').generate_permutations_by_range(0, 5)


