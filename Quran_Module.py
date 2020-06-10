import os
import csv


class Project_Quran:
    def __init__(self):
        Quran_English = []
        with open('C:/Users/ahmad/PycharmProjects/AnonymousTraining/Quran_English.csv', 'rt') as f:
            for rows in f:
                Quran_English.append(rows)
        self.Quran_English = Quran_English
        Quran_Arabic = []
        with open('C:/Users/ahmad/PycharmProjects/AnonymousTraining/Quran_Arabic.csv') as v:
            for rows in v:
                Quran_Arabic.append(rows)
            self.Quran_Arabic = Quran_Arabic
    def Check_Ayah(self, Ayah_Number):
        self.Check_Ayah_Results = False
        for enteries in self.Quran_English:
            if Ayah_Number in enteries:
                self.Check_Ayah_Results = True

    def Get_Ayah_English(self, Ayah_Number):
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


if __name__ == '__main__':
    print("Module has no Errors and it works just fine I suppose, If you have any Questions Related to Project_Quran.\n Contact: Muneebkhurram9@gmail.com \n Note: \n We are AnonymousPAK we are a Legion, We do Forgive, but We do not Forget, Expect us!")
    os.system('pyfiglet AnonymousPAK shall    Rise')
    print('[+] Death is upon Iluminati and New World Order, Insha-Allah!')
    print('[+] Islam shall rise as it a religon of Peace, and those who try to mock Islam, fear the wrath of God, the Almighty, the All Merciful.')
    print('[+] Fear Death as Death will also come to Death on the Day of Judgement')
    print('[+] We follow Hadrat Muhammad (PBUH), We are Only Muslims, we are the Religion of Peace, But when try to take over our homelands, we would retaliate!')
    print('[+] You try to mock Islam, have you ever thought, Ilumninati, in your country USA when a Black man does a firing he is a Terrorist, but when a white man does it, that is Mental Ilness!')
    print('[+] لا الہ الا اللّٰہ محمد الرسول اللّٰہ ﷺ')
    print("We are Peaceful, and we have no racial injustice like you since the beginning of Islam, As our Prophet (PBUH) said; \n We all are the children of Adam (A.S), thus no Arabian has any superiority over Non-Arabian and no Non-Arabian has superiority on Arabian, \n No Black is superior on white and No white is superior on Black!")
    os.system("pyfiglet '/----PAK----/'")
