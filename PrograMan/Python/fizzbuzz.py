if __name__ == '__main__':
    
    print('F I Z Z B U Z Z  E N  P Y T H O N')
    
    for i in range (1, 100):   
        if i % 3 ==0:
            print('Fizz')
        if i % 5 ==0:
            print('Buzz')
        if i % 3 == 0 and i % 5 ==0:
            print('FizzBuzz')    
        if i % 3 != 0 and i % 5 !=0:
            print(i)
