        
def string_to_boolean(value):
    """
    >>> string_to_boolean('true')
    True
    >>> string_to_boolean('false')
    False
    >>> string_to_boolean('t')
    True
    >>> string_to_boolean('f')
    False
    """
    
    if value is None or value.lower() in ['false', 'f', '0', '']:
        return False
    elif value.lower() in ['true', 't', '1']:
        return True
    else:
        raise ValueError(f"{value} is not a valid boolean value")
    