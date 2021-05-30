s_1 = b'attribute'
s_2 = b'класс'
s_3 = b'функция'
s_4 = 'type'

#   s-2 и s-3 невозможно записать в байтовом типе, будут ошибки:
#
#     s_2 = b'класс'
#            ^
#   SyntaxError: bytes can only contain ASCII literal characters.
#
#     s_3 = b'функция'
#            ^
#   SyntaxError: bytes can only contain ASCII literal characters.