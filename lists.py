# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    nuevalista1 = list_to_remove_elements[:]

    if len(nuevalista1) >= 6:
        del nuevalista1[5]
        del nuevalista1[4]
        del nuevalista1[0]

    elif len(nuevalista1) == 5:
        del nuevalista1[4]
        del nuevalista1[0]

    elif 1 <= len(nuevalista1) <= 4:
        del nuevalista1[0]

    return nuevalista1


def add_elements(list_to_add_elements):
    nuevalista2 = list_to_add_elements[:]
    nuevalista2.insert(0, 'Pink')
    nuevalista2.append('Yellow')
    return nuevalista2


def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False


def check_lists(lista1, lista2):
    if len(lista1) > 2 and len(lista2) > 2:
        return lista1[2] == lista2[2]
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify) < 3:
        return "la lista no tiene tres listas"

    lista1 = list_of_lists_to_modify[0]
    lista2 = list_of_lists_to_modify[1]
    lista3 = list_of_lists_to_modify[2]

    if len(lista1) >= 2:
        lista1 = lista1[0:2]
    else:
        lista1 = lista1[0:1]

    if len(lista2) >= 4:
        lista2 = lista2[1:4]
    else:
        lista2 = lista2[1:]

    lista3 = lista3[-2:]

    return [lista1, lista2, lista3]
