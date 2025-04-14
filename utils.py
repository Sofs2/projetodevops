
def e_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False