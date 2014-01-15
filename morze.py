# coding=utf-8
import sublime, sublime_plugin, string

field_rows = [
    [
        ". -   ",      #A
        "- . . .   ",  #B
        "- . - .   ",  #C
        "- . .   ",    #D
        ".   ",        #E
        ". . - .   ",  #F
        "- - .   ",    #G
        ". . . .   ",  #H
        ". .   ",      #I
        ". - - -   ",  #J
        "- . -   ",    #K
        ". - . .   ",  #L
        "- -   ",      #M
        "- .   ",      #N
        "- - -   ",    #O
        ". - - .   ",  #P
        "- - . -   ",  #Q
        ". - .   ",    #R
        ". . .   ",    #S
        "-   ",        #T
        ". . -   ",    #U
        ". . . -   ",  #V
        ". - -   ",    #W
        "- . . -   ",  #X
        "- . - -   ",  #Y
        "- - . .   ",  #Z
        ". - - - -   ", #1
        ". . - - -   ", #2
        ". . . - -   ", #3
        ". . . . -   ", #4
        ". . . . .   ", #5
        "- . . . .   ", #6
        "- - . . .   ", #7
        "- - - . .   ", #8
        "- - - - .   ", #9
        "- - - - -   ", #0
        "       ",      #Space
    ]
]

class morze(sublime_plugin.TextCommand):
    def run(self, edit):
        # получаем объект view
        view = self.view
        # получаем массив координат выделенной области
        for curr_sel in view.sel():
            n = 0
            region = curr_sel
            if not region.empty():
                # если не пустой, берем очередной выбранный блок текста
                selection = view.substr(region)
                result = ''
                #пробегаем по строкам с набором значений и производим подстановку
                for field_row in field_rows:
                    result += selection.replace(
                      'A',field_row[0]).replace(
                      'a',field_row[0]).replace(
                      'B',field_row[1]).replace(
                      'b',field_row[1]).replace(
                      'C',field_row[2]).replace(
                      'c',field_row[2]).replace(
                      'D',field_row[3]).replace(
                      'd',field_row[3]).replace(
                      'E',field_row[4]).replace(
                      'e',field_row[4]).replace(
                      'F',field_row[5]).replace(
                      'f',field_row[5]).replace(
                      'G',field_row[6]).replace(
                      'g',field_row[6]).replace(
                      'H',field_row[7]).replace(
                      'h',field_row[7]).replace(
                      'I',field_row[8]).replace(
                      'i',field_row[8]).replace(
                      'J',field_row[9]).replace(
                      'j',field_row[9]).replace(
                      'K',field_row[10]).replace(
                      'k',field_row[10]).replace(
                      'L',field_row[11]).replace(
                      'l',field_row[11]).replace(
                      'M',field_row[12]).replace(
                      'm',field_row[12]).replace(
                      'N',field_row[13]).replace(
                      'n',field_row[13]).replace(
                      'O',field_row[14]).replace(
                      'o',field_row[14]).replace(
                      'P',field_row[15]).replace(
                      'p',field_row[15]).replace(
                      'Q',field_row[16]).replace(
                      'q',field_row[16]).replace(
                      'R',field_row[17]).replace(
                      'r',field_row[17]).replace(
                      'S',field_row[18]).replace(
                      's',field_row[18]).replace(
                      'T',field_row[19]).replace(
                      't',field_row[19]).replace(
                      'U',field_row[20]).replace(
                      'u',field_row[20]).replace(
                      'V',field_row[21]).replace(
                      'v',field_row[21]).replace(
                      'W',field_row[22]).replace(
                      'w',field_row[22]).replace(
                      'X',field_row[23]).replace(
                      'x',field_row[23]).replace(
                      'Y',field_row[24]).replace(
                      'y',field_row[24]).replace(
                      'Z',field_row[25]).replace(
                      'z',field_row[25]).replace(
                      '1',field_row[26]).replace(
                      '2',field_row[27]).replace(
                      '3',field_row[28]).replace(
                      '4',field_row[29]).replace(
                      '5',field_row[30]).replace(
                      '6',field_row[31]).replace(
                      '7',field_row[32]).replace(
                      '8',field_row[33]).replace(
                      '9',field_row[34]).replace(
                      '0',field_row[35]).replace('    ',field_row[36])
                    #4 пробела берутся так как между каждым знаком расстояние в 3 точки, и если слово закончилось, а заним идёт следующая, то 4 точкой является пробел, потому нужно для пробела найти 4
                #Конец связи
                result += "\r\n. . - . -"
                #заменяем шаблон на сгенерированный блок кода
                self.view.replace(edit, region, result)
