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


	elif len(lista)>=1 and len(lista)<=4:
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
	if len(list_of_lists) >= 3:
	lista1 = list_of_lists[0]
        lista2 = list_of_lists[1]
        lista3 = list_of_lists[2]
       
	elif len(list_of_lists) < 3:
	return "la lista no tiene tres listas"
	       
	if len(lista1) >= 2:
        lista1 = lista1[0:2]
  
	elif len(lista1) < 2:
        lista1 = lista1[0:1]

	if len(lista2) >= 4:
        lista2 = lista2[1:4]
	
	elif len(lista2) < 4:
        lista2 = lista2[1:]
	lista3 = lista3[-2:]
	
	return [lista1, lista2, lista3]
