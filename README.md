# Quran_Module

Using this Module, you can access all verses of Quran in Arabic and their Translations. You can Also search the Quran both in Arabic and English, with as little as 3 lines of Code

## Installation

Clone the repo and run pip install:
```
git clone https://github.com/UBISOFT-1/Quran_Module.git
pip install .
```
Or pip install directly from the repo:
```
pip install git+https://github.com/UBISOFT-1/Quran_Module.git
```
*Make .py files in the cloned folders for this Module to work.*
## Usage

To use this Module, the Documentation is Straight Forward. All of the Code below is super easy
and all the documentation you need to know.
Make Sure you have your .py file in the Github Folder that you will clone.
```python
from Quran_Module import Project_Quran

Quran = Project_Quran()
# Call the Get Ayah Function for English Text, use 59 before the Surah, Verse for English.
Quran.Get_Ayah_English('59,2,20')
# Now Get the Ayah that you called for by using the Print Function to print it.
print(Quran.Ayah_English)
# You can also call the Get Ayah Function for Arabic, use 1 before the Surah and Verse for Arabic.
Quran.Get_Ayah_Arabic('1,2,20')
# Now Print the Arabic Text to see the Output
print(Quran.Ayah_Arabic)

# You can also check if an Ayah is there that you are calling for by using the following Function

Quran.Check_Ayah('59,2,20')
# It would Return as True if the Ayah is there and False if the Ayah is not there
print(Quran.Check_Ayah_Results)
if Quran.Check_Ayah_Results == True:
    print('Ayah is there! ;)')

# If you want all of the Quran as a List you can do
Quran.Get_Quran()
# This will print all of the Quran as Arabic or as English as a List
print(Quran.All_Quran_Arabic)
print(Quran.All_Quran_English)

# If you want a .txt with A range of Arabic and their Translations you can call another method
# Here there is no need to add 59, first for English and 1, first for Arabic. It is there as we add more translations.
Ayah_to_Get = ['1,2', '5,5', '6,8']
# Format <Ayah_Range>, <filename>
# Default filename = 'Quran_text.txt'
Quran.Get_Custom_Quran_text(Ayah_to_Get, filename= 'Quran_Ayah_to_read.txt')

# You can also find text in Quran and show their Results as Output by using the following method
# You can Search in English or Arabic as you like

Quran.Find_Text_English('Muhammad')
Quran.Find_Text_Arabic('إِن')
# Outputs are saved as a List
print(Quran.Search_Results_Arabic)
print(Quran.Search_Results_English)

# Remember The 59, Translation is for Abdullah Yusuf Ali (English) Widely accepted and most used
# And 1, is for the Original Arabic Text.
# That was all you are set to go, tell me what else should I add to this.


```
# Dependancies
None, Only from the Standard Library:
- ``os`` module
- ``csv`` module

# Qur'an Source
See http://www.qurandatabase.org/
All the text and Databases are theirs.

# License

See LICENSE.txt Also, when used in any Commercial Application, Permission must be taken. And for modifiying the code, permission must also be granted. And for Private use, feel free to enjoy.

### Special Thanks
Special Thanks to God Almighty who helped me make this module in less than an Hour Practically.
 
