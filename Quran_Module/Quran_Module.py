import os
from pkg_resources import resource_string, resource_filename

class Project_Quran:
    def __init__(self):
        Quran_English = []
        Quran_English_path = resource_filename(__name__, 'Quran_English.csv')
        with open(Quran_English_path, 'rt') as f:
            for rows in f:
                Quran_English.append(rows)
        self.Quran_English = Quran_English
        Quran_Arabic = []
        Quran_Arabic_path = resource_filename(__name__, 'Quran_Arabic.csv')
        with open(Quran_Arabic_path) as v:
            for rows in v:
                Quran_Arabic.append(rows)
            self.Quran_Arabic = Quran_Arabic
        Allah_Names = []
        Allah_Names_path = resource_filename(__name__, 'Allah_Names.csv')
        with open(Allah_Names_path) as v:
            for i, rows in enumerate(v):
                if i == 0:
                    continue
                Allah_Names.append(rows)
            self.Allah_Names = Allah_Names
    def Check_Ayah(self, Ayah_Number):
        self.Check_Ayah_Results = False
        for enteries in self.Quran_English:
            if Ayah_Number in enteries:
                self.Check_Ayah_Results = True

    def     Get_Ayah_English(self, Ayah_Number):
        for enteries in self.Quran_English:
            if Ayah_Number in enteries:
                self.Ayah_English = enteries
                return self.Ayah_English
    def Get_Ayah_Arabic(self, Ayah_Number):
        for enteries in self.Quran_Arabic:
            if Ayah_Number in enteries:
                self.Ayah_Arabic = enteries
                return self.Ayah_Arabic
    def Get_Quran(self):
        self.All_Quran_English = self.Quran_English
        self.All_Quran_Arabic = self.Quran_Arabic
        return self.All_Quran_Arabic, self.All_Quran_English
    def Get_Custom_Quran_text(self, Ayah_List, filename = 'Quran_text.txt'):
        f = open(filename, 'a+')
        for Ayah_Number in Ayah_List:
            Arabic_Num = '1,' + Ayah_Number
            self.Get_Ayah_Arabic(Arabic_Num)
            f.write(self.Ayah_Arabic)
            English_Num = '59,' + Ayah_Number
            self.Get_Ayah_English(English_Num)
            f.write(self.Ayah_English)
        f.close()
    def Find_Text_English(self, Text_to_Find):
        self.Search_Results_English = []
        for enteries in self.Quran_English:
            if Text_to_Find in enteries:
                print(enteries)
                self.Search_Results_English.append(enteries)
        print(str(len(self.Search_Results_English)) + ' Ayahs found! ;)')
        return self.Search_Results_English

    def Find_Text_Arabic(self, Text_to_Find):
        self.Search_Results_Arabic = []
        for enteries in self.Quran_Arabic:
            if Text_to_Find in enteries:
                print(enteries)
                self.Search_Results_Arabic.append(enteries)
        print(str(len(self.Search_Results_Arabic)) + ' Ayahs found! ;)')
        if len(self.Search_Results_Arabic) == 0:
            print("Try Searching the same word in English, or If you want it in Arabic Add Proper (َ ِ ُ ّ )")
        return self.Search_Results_Arabic
    
    def Get_Names_of_Allah_English(self):
        self.Allah_Names_English = []
        for enteries in self.Allah_Names:
            self.Allah_Names_English.append(enteries.split(',')[-1].replace('\n',''))
        return self.Allah_Names_English
    
    def Get_Names_of_Allah_Arabic(self):
        self.Allah_Names_Arabic = []
        for enteries in self.Allah_Names:
            self.Allah_Names_Arabic.append(enteries.split(',')[0])
        return self.Allah_Names_Arabic
    
    def Get_Names_of_Allah_Transliteration(self):
        self.Allah_Names_Transliteration = []
        for enteries in self.Allah_Names:
            self.Allah_Names_Transliteration.append(enteries.split(',')[1])
        return self.Allah_Names_Transliteration


if __name__ == '__main__':
    print("[+] Prosperity to All Humankind!")