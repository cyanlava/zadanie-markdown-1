def pikachu(x):
    for i in range(0, 3):
        x=x+i
    return x

def test(): 
    assert pikachu(1) == 4
