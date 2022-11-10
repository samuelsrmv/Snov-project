# #('en_GB', 'UTF-8')
# import locale
# #loc = locale.getlocale() # get current locale

# x = locale.setlocale(locale.LC_ALL, '332222.03')
# print(x)
# Funcion Moneda
import locale
locale.setlocale(locale.LC_MONETARY, 'en_US')

print(str(locale.currency(450868,6, grouping=True)))