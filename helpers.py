
def test(passing : bool, description : str):
    if passing :
        print('✔️ Success ' + description + '\n')
    else :
        print('⛔ Failure ' + description + '\n')
        