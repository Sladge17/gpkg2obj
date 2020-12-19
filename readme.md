# Общее описание
Скрипт converter.py разработан под MacOS, на рабочих станциях АНО Школа 21, с учетом прав доступа для студентов.
Скрипт использует для создания 3D моделей, Blender 2.91, и библиотеку geopandas для работы с данными gpkg.
При запуске скрипта через run.sh, blender создает 3D модели в "бесшумном" режиме.
Все созданные 3D модели формата obj, хранятся в папке result.

# Возникшие проблемы, и решения
 Не удалось найти информацию в каких еденицах хранятся значения
 ![alt text](https://github.com/Sladge17/BConv-gpkg2obj-/blob/master/Sceenshoots/Screen1.png) 
 
 Не удалось найти слой pit, про который говорилось в задании
 ![alt text](https://github.com/Sladge17/BConv-gpkg2obj-/blob/master/Sceenshoots/Screen2.png)
 
 Изначально предполагалось, что данные о координатах трубопроводов храняться в поле geometry, но значения хранящиеся там для одного id очень близки по значению, и при создании модели сливаются.
 ![alt text](https://github.com/Sladge17/BConv-gpkg2obj-/blob/master/Sceenshoots/Screen3.png)
 
 Сейчас для создания труб используются поля X1, Y1, Z1, X2, Y2, Z2, но так получается создать только односегментные трубы, хотя возможность создания мультисигментных труб в код заложена.
![alt text](https://github.com/Sladge17/BConv-gpkg2obj-/blob/master/Sceenshoots/Screen4.png)

 На данный момент возможно создать трубы только радиального сечения в 8 сегментов, диаметральное значение берется из поля SECT_HEIGH, и считается по формуле SECT_HEIGH / 1000
