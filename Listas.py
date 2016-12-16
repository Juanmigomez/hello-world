# -*- coding: utf-8 -*-
# Añadiremos elementos a una lista y los ordenaremos.


def print_debug(templist):
    print (templist)


debug = 1

# Declaramos la variable de tipo list vacia
thelist = list()
if 1 == debug:
    print_debug(thelist)

# Añadimos a Carlos a la lista
thelist.append('Carlos')
if 1 == debug:
    print_debug(thelist)

# Añadimos a Antonio, Gerard y a mi a la lista
thelist.append('Antonio')
thelist.append('Gerard')
thelist.append('Juanmi')
if 1 == debug:
    print_debug(thelist)

# Ordenamos la lista
thelist.sort()
if 1 == debug:
    print_debug(thelist)


