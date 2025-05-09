# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
	nuevalista1= lista [:]

	if len(lista) >=6:
		del nuevalista1 [5]
		del nuevalista1 [4]
		del nuevalista1 [0]


	elif len(lista)==5:
		del nuevalista1 [4]
		del nuevalista1 [0]


	elif len(lista)>=1 and len(lista)<=3:
		del nuevalista1 [0] 

	return nuevalista1
   

def add_elements(list_to_add_elements):
    nuevalista2= lista[:]
	nuevalista2.append('Yellow')
	nuevalista2.insert(0, 'Pink')

    return nuevalista2
    

def is_empty(list_to_check):
    if lista == []:
		return True 

	else:
		return False


def check_lists(lista1, lista2):
    nuevalista1= lista1 [:]
	nuevalista2= lista2 [:]

	if nuevalista1[2]== nuevalista2[2]:
		return True

	else:
		return False



def list_of_lists(list_of_lists_to_modify):
    return "ANSWER HERE"  # Remove this line and implement
