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
    lst = []
    ii = ('\nOrder Number:\t',
      'Book Title:\t\t',
      'Author Name:\t',
      'Quantity:\t\t',
      'Item Price:\t\t')

    while i < 5:
        lst.append(input(ii[i]))
        i += 1
    return lst


def list_of_items(q=True):
    """
    The List of Items lists.

    Requesting intention on item list input and append available list, if any, to the summary list.
    :param q:
    :return:
    """
    m_lst = []
    while q:
        if q == 'y':
            m_lst.append(item_record_gen())
        elif q == 'n':
            print('\n\t\u2139\tHere is the list of new items added\t\u2B07\n\n', m_lst)
            break
        q = str(input('\nWould you like to insert new item? (y / n):\t'))
    return m_lst


def price_list_gen():
    """
    Order total price and quantity.

    Getting Order Numbers, Total prices (based on item price and item quantity) and Items quantity.
    (i) if Total price less than 100$, another 10$ will be added.
    :return: tuple of lists, containing ('Order Number', Total price, Quantity)
    """
    a = list_of_items()
    f_lst = []

    for n in range(len(a)):
        itm = str(a[n][0])
        qtt = int(a[n][3])
        prc = float(a[n][4])

        if (prc * qtt) < 100 and (prc * qtt) != 0:
            prc = (prc * qtt) + 10
        elif (prc * qtt) >= 100:
            prc = (prc * qtt)

        x = (itm, prc, qtt)
        f_lst.append(x)
    return f_lst


print('\n\t\u2139\tHere is list of tuples, containing:\n',
      '(\'Order Number\', Total price, Quantity)\t\u2B07\n\n',
      price_list_gen())
