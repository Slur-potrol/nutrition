# import formula
import sys
import pandas


def guess_kcal(amr):
    index = 0
    if gender == 'ж':
        if amr == 1:
            index = 1.2
        elif amr == 2:
            index = 1.375
        elif amr == 3:
            index = 1.55
        elif amr == 4:
            index = 1.725
        elif amr == 5:
            index = 1.9
        BMR = (447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)) * index
        if goal == '1':
            kcal = float(BMR - float(BMR / 100 * 20))
            if kcal >= 1200 and kcal <= 1400:
                nutrition = pandas.read_csv('nutrition/women/W_1_1_1200-1400.csv', index_col='Еда')
            elif kcal >= 1401 and kcal <= 1600:
                nutrition = pandas.read_csv('nutrition/women/W_1_2_1401-1600.csv', index_col='Еда')
            elif kcal >= 1601 and kcal <= 1800:
                nutrition = pandas.read_csv('nutrition/women/W_1_3_1601-1800.csv', index_col='Еда')
            elif kcal >= 1801 and kcal <= 2000:
                nutrition = pandas.read_csv('nutrition/women/W_1_4_1801-2000.csv', index_col='Еда')
            elif kcal >= 2001 and kcal <= 2200:
                nutrition = pandas.read_csv('nutrition/women/W_1_5_2001-2200.csv', index_col='Еда')
        elif goal == '2':
            kcal = BMR
            if kcal >= 1500 and kcal <= 1700:
                nutrition = pandas.read_csv('nutrition/women/W_2_1_1500-1700.csv', index_col='Еда')
            elif kcal >= 1701 and kcal <= 2000:
                nutrition = pandas.read_csv('nutrition/women/W_2_2_1701-2000.csv', index_col='Еда')
            elif kcal >= 2001 and kcal <= 2200:
                nutrition = pandas.read_csv('nutrition/women/W_2_3_2001-2200.csv', index_col='Еда')
            elif kcal >= 2201 and kcal <= 2500:
                nutrition = pandas.read_csv('nutrition/women/W_2_4_2201-2500.csv', index_col='Еда')
            elif kcal >= 2501 and kcal <= 2700:
                nutrition = pandas.read_csv('nutrition/women/W_2_5_2501-2700.csv', index_col='Еда')
        elif goal == '3':
            kcal = float(BMR + float(BMR / 100 * 15))
            if kcal >= 2400 and kcal <= 2900:
                nutrition = pandas.read_csv('nutrition/women/W_3_1_1800-2000.csv', index_col='Еда')
            elif kcal >= 2901 and kcal <= 3300:
                nutrition = pandas.read_csv('nutrition/women/W_3_2_2001-2300.csv', index_col='Еда')
            elif kcal >= 3100 and kcal <= 3700:
                nutrition = pandas.read_csv('nutrition/women/W_3_3_2301-2600.csv', index_col='Еда')
            elif kcal >= 3500 and kcal <= 4100:
                nutrition = pandas.read_csv('nutrition/women/W_3_4_2601-2900.csv', index_col='Еда')
            elif kcal >= 3900 and kcal <= 4500:
                nutrition = pandas.read_csv('nutrition/women/W_3_5_2901-3200.csv', index_col='Еда')

    elif gender == 'м':
        if amr == 1:
            index = 1.2
        elif amr == 2:
            index = 1.375
        elif amr == 3:
            index = 1.55
        elif amr == 4:
            index = 1.725
        elif amr == 5:
            index = 1.9
        BMR = (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) * index
        if goal == '1':
            kcal = float(BMR - float(BMR / 100 * 20))
            if kcal >= 1700 and kcal <= 2000:
                nutrition = pandas.read_csv('nutrition/men/M_1_1_1700-2000.csv', index_col='Еда')
            elif kcal >= 2001 and kcal <= 2300:
                nutrition = pandas.read_csv('nutrition/men/M_1_2_2001-2300.csv', index_col='Еда')
            elif kcal >= 2301 and kcal <= 2600:
                nutrition = pandas.read_csv('nutrition/men/M_1_3_2301-2600.csv', index_col='Еда')
            elif kcal >= 2601 and kcal <= 2900:
                nutrition = pandas.read_csv('nutrition/men/M_1_4_2601-2900.csv', index_col='Еда')
            elif kcal >= 2901 and kcal <= 3200:
                nutrition = pandas.read_csv('nutrition/men/M_1_5_2901-3200.csv', index_col='Еда')
        elif goal == '2':
            kcal = BMR
            if kcal >= 2100 and kcal <= 2500:
                nutrition = pandas.read_csv('nutrition/men/M_2_1_2100-2500.csv', index_col='Еда')
            elif kcal >= 2501 and kcal <= 2900:
                nutrition = pandas.read_csv('nutrition/men/M_2_2_2501-2900.csv', index_col='Еда')
            elif kcal >= 2800 and kcal <= 3300:
                nutrition = pandas.read_csv('nutrition/men/M_2_3_2800-3300.csv', index_col='Еда')
            elif kcal >= 3000 and kcal <= 3700:
                nutrition = pandas.read_csv('nutrition/men/M_2_4_300-3700.csv', index_col='Еда')
            elif kcal >= 3300 and kcal <= 4000:
                nutrition = pandas.read_csv('nutrition/men/M_2_5_3300-4000.csv', index_col='Еда')
        elif goal == '3':
            kcal = float(BMR + float(BMR / 100 * 15))
            if kcal >= 2400 and kcal <= 2900:
                nutrition = pandas.read_csv('nutrition/men/M_3_1_2400-2900.csv', index_col='Еда')
            elif kcal >= 2901 and kcal <= 3300:
                nutrition = pandas.read_csv('nutrition/men/M_3_2_2901-3300.csv', index_col='Еда')
            elif kcal >= 3100 and kcal <= 3700:
                nutrition = pandas.read_csv('nutrition/men/M_3_3_3100-3700.csv', index_col='Еда')
            elif kcal >= 3500 and kcal <= 4100:
                nutrition = pandas.read_csv('nutrition/men/M_3_4_3500 - 4100.csv', index_col='Еда')
            elif kcal >= 3900 and kcal <= 4500:
                nutrition = pandas.read_csv('nutrition/men/M_3_5_3900-4500.csv', index_col='Еда')

    return nutrition



if __name__ == '__main__':
    gender = input('Введите ваш пол (м/ж): ')
    if not (gender == 'м' or gender == 'ж'):
        raise ValueError('Неправильный ввод, пожалуйста введите "м" либо "ж". ')

    goal = input("Выберете вашу цель(1/2/3): 'Снижение веса(1)', 'Поддержание веса(2)', 'Набор веса(3)': ")
    if not (goal == '1' or goal == '2' or goal == '3'):
        raise ValueError('Неправильный ввод, пожалуйста введите "1", "2", "3"')

    try:
        height = int(input('Ваш рост?: '))
        weight = int(input('Ваш вес?: '))
        age = int(input('Ваш возраст?: '))
        amr = int(input('Укажите ваш уровень активности:'
                        '\n1 - Сидячий образ жизни;'
                        '\n2 - Умеренная активность (легкие физические нагрузки либо занятия 1-3 раз в неделю);'
                        '\n3 - Средняя активность (занятия 3-5 раз в неделю);'
                        '\n4 - Активные люди (интенсивные нагрузки, занятия 6-7 раз в неделю);'
                        '\n5 - Спортсмены и люди, выполняющие сходные нагрузки (6-7 раз в неделю).\n'))
    except ValueError:
        print("Неправильный ввод, пожалуйста используйте цифры в показателях: рост/вес/возраст.")
        sys.exit(13)


    # print('Белки ~>'
    #       'Жиры ~>'
    #       'Углеводы ~>', guess)
    print(guess_kcal(amr))
