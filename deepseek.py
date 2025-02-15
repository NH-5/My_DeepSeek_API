
import deepseek_R1
import deepseek_V3

apikey = input('Input your API-Key of Deepseek:')

while True:
    print('1.deepseek-V3')
    print('2.deepseek-R1')
    print('3.exit')
    
    try:
        choice = int(input('Input your choice:'))
    
    except ValueError:
        print('Error input!')
        continue

    if choice == 1:
        print('If you want to exit, input exit or Exit')
        while True:
            prompt=input('>>>')
            if prompt.lower() == 'exit':
                break
            deepseek_V3.V3(prompt,apikey)
        
    elif choice == 2:
        print('If you want to exit, input exit or Exit')
        while True:
            prompt=input('>>>')
            if prompt.lower() == 'exit':
                break
            deepseek_R1.R1(prompt,apikey)
        
    elif choice == 3:
        break
    
    else:
        print('Error input!')