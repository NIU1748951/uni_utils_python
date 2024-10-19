from typing import List, Optional, Union


def LlegirLlista(dimensio: int) -> List[int]:
    """
    Llegeix una llista d'enters de l'usuari.
    
    Args:
        dimensio (int): La quantitat d'elements a llegir.

    Returns:
        List[int]: La llista d'elements introduïts per l'usuari.
    """

    llista = []
    for i in range(dimensio):
        while True:
            try:
                element = int(input(f"Introdueix el element #{i+1}: "))
                llista.append(element)
                break
            except ValueError:
                print("Introdueix un valor enter")
    return llista        

def InicialitzarLlista(dimensio: int, element: Union[int, float, str]) -> List[Union[int, float, str]]:
    """
    Inicialitza una llista d'una longitud especificada amb un valor predeterminat.
    
    Args:
        dimensio (int): La longitud de la llista.
        element: L'element amb el qual inicialitzar la llista.

    Returns:
        List[int]: 
            Una llista d'elements introduïts per l'usuari.
            Conté números enters.
    """

    return [element] * dimensio

def MitjanaLlista(llista: List[Union[float, int]]) -> float:
    """
    Calcula la mitjana d'una llista d'enters o flotants.

    Args:
        llista: La llista d'elements (int / float).
    Returns:
        float: La mitjana de la llista.
        Si la llista està buida, retorna -1.
    """

    return sum(llista) / len(llista) if llista else -1

def MaximLlista(llista: List[Union[float, int]]) -> Optional[int]:
    """
    Troba l'índex del valor màxim en una llista.
    
    Args:
        llista (List[Union[int, float]]): La llista d'elements.

    Returns:
        Optional[int]: L'índex del valor màxim, o None si la llista és buida.
    """
    if not llista:
        return None
    maxim = max(llista)
    return llista.index(maxim)

def MinimLlista(llista: List[Union[float, int]]) -> Optional[int]:
    """
    Troba l'índex del valor mínim en una llista.
    
    Args:
        llista (List[Union[int, float]]): La llista d'elements.

    Returns:
        Optional[int]: L'índex del valor mínim, o None si la llista és buida.
    """
    if not llista:
        return None
    minim = min(llista)
    return llista.index(minim)

def MinimLlistaNoZero(llista: List[Union[float, int]]) -> Optional[int]:
    """
    Troba l'índex del valor mínim en una llista que no sigui zero.
    
    Args:
        llista (List[Union[int, float]]): La llista d'elements.

    Returns:
        Optional[int]: L'índex del valor mínim no zero, o None si no existeix o està buida.
    """
    minim = None
    for i in range(len(llista)):
        if llista[i] != 0:
            minim = llista[i]
            index = i
            break
    if minim is None:
        return None

    for i in range(index + 1, len(llista)):
        if llista[i] < minim and llista[i] != 0:
            minim = llista[i]
    
    return llista.index(minim)

# Funció Inutil
def reduce_llista(llista: List[Union[float, int]]) -> List[Union[int, float]]:
    """
    Redueix la llista eliminant elements duplicats mantenint l'ordre original.

    Args:
        llista (List[Union[int, float]]): La llista d'elements.

    Returns:
        List[Union[int, float]]: La llista sense duplicats.
    """

    vista = set()  # Conjunt per guardar els elements ja vistos
    reduida = []   # Llista per guardar els resultats

    for element in llista:
        if element not in vista:
            vista.add(element)  # Afegir a la llista de vistos
            reduida.append(element)  # Afegir a la llista reduïda

    return reduida

def ordenar_llista(llista, algoritme: Optional[str] = 'bombolla') -> None:
    """
    Ordena la llista de més petit a més gran amb l'algorisme seleccionat (Actualment només bombolla!).
    Modifica la llista d'entrada.

    Args:
        llista (List[Union[int, float]]): La llista a ordenar.
        algoritme (Optional[str]): L'algorisme a utilitzar. Actualment només 'bombolla'!. 
    """

    def ord_bombolla(llista):
        n = len(llista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if llista[j] > llista[j + 1]:
                    llista[j], llista[j + 1] = llista[j + 1], llista[j]

    ord_bombolla(llista)