"""
���� ��� ������ ������ �����. � ������ ���������� �����,
� �� ������ ��������. �������� �������, ������� ������
�� ���� ������ � �������� �������. ���� ����� �� �������
��������, � ������� ������ ���� �������� None. ��������,
������� �� ������� ������, ����� ������������.
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