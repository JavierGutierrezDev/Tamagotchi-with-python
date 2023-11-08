# Aspectos del Tamagotchi
def get_aspect(happiness, alive, accessories=None):
    happy_cat = """
     /\_/\  
    ( ^.^ ) 
     > ^ <
    """
    
    neutral_cat = """
     /\_/\  
    ( o.o ) 
     > ^ <
    """
    
    sad_cat = """
     /\_/\  
    ( -.- ) 
     > ^ <
    """
    
    dead_cat = """
     x.x  
     > ^ <
    """
    
    hat_cat = """
     /\_/\  
    ( o.o ) 
     /🎩\\ 
    """
    
    bow_cat = """
     /\_/\  
    ( o.o ) 
     /🎀\\  
    """
    
    glasses_cat = """
     /\_/\  
    ( -.- ) 
    --| |-- 
     > ^ <
    """
    
    scarf_cat = """
     /\_/\  
    ( o.o ) 
    /🧣\\ 
     > ^ <
    """
    
    party_hat_cat = """
     /\_/\  
    ( ^.^ ) 
     /🎉\\ 
     > ^ <
    """

    # Elegir el arte ASCII basado en los niveles de felicidad y estado de vida
    if not alive:
        return dead_cat
    if happiness > 7:
        face = happy_cat
    elif happiness > 4:
        face = neutral_cat
    else:
        face = sad_cat

    # Añadir accesorios si existen
    if accessories == 'hat':
        return hat_cat
    elif accessories == 'bow':
        return bow_cat
    elif accessories == 'glasses':
        return glasses_cat
    elif accessories == 'scarf':
        return scarf_cat
    elif accessories == 'party_hat':
        return party_hat_cat

    return face
