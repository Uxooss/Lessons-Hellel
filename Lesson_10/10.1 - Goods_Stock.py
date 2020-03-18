'''
Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, колличестве и стоимости одной книги, как
представленно ниже, в таблице.
+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einfuhrung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
[
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей.
    Каждый кортеж состоит из номера заказа и произведения цены на товары и количества.
    Стоимость товара должена быть увеличена на $10, если стоимость заказа меньше $100.
Программа должна использовать lambda и map.
'''


def item_record_gen(i=0):
    """
    Creating List with Item's description.

    Gathering information through Inputs and appending them to the list, as per required order.
    :param i:
    :return: (Order Number, Book Title, Author Name, Quantity, Item Price)
    """
    fst_lst = []
    ii = ('\nOrder Number:\t',
      'Book Title:\t\t',
      'Author Name:\t',
      'Quantity:\t\t',
      'Item Price:\t\t')

    while i < 5:
        fst_lst.append(input(ii[i]))
        i += 1
    return fst_lst


def list_of_items(qtn=True):
    """
    The List of Items lists.

    Requesting intention on item list input and append available list, if any, to the summary list.
    :param qtn:
    :return:
    """
    ttl_lst = []
    while qtn:
        if qtn == 'y':
            ttl_lst.append(item_record_gen())
        elif qtn == 'n':
            break
        qtn = str(input('\nWould you like to insert new item? (y / n):\t'))
    return ttl_lst


fin_lst = list(map(lambda a: (a[0],
        round((int(a[3]) * float(a[4]) if int(a[3]) * float(a[4]) >= 100 else int(a[3]) * float(a[4]) + 10), 2),
        a[3]), list_of_items()))

print(fin_lst)
