def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 178.53

    return mex_to_col_rate * ammount

def run():
    print('C A L C U LA D O R A  D E  D I V I S A S')
    print('Convierté pesos Mexicanos a pesos Colombianos.')
    print('')

    ammount = float(input('Ingrese el valor que desea convertir:'))
    print('')
    result = foreign_exchange_calculator(ammount)

    print ('${} pesos mexicanos son ${} pesos colombianos.' .format(ammount, result))

if __name__ == '__main__':
    run()