"""
Есть два списка разной длины. В первом содержатся ключи,
а во втором значения. Напишите функцию, которая создаёт
из этих ключей и значений словарь. Если ключу не хватило
значения, в словаре должно быть значение None. Значения,
которым не хватило ключей, нужно игнорировать.
"""

def yandex_exersise_one(list_key,list_value):
    dictionary = {}
    i = 0
    for n in list_key:
        try:
            dictionary[n] = list_value[i]
        except IndexError:
            dictionary[n] = None
        i+=1
    return dictionary

def main():
    yandex_one(["one","two","three"],[1,2])


if __name__ == '__main__':
  main()