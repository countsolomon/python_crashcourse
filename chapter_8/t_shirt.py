#exercise 8-3
#a tshirt function. 
#function accepts the tshirt size and the tshirt text. 

def make_shirt(size='large', text="i love Python"):
    print(f'the tshirts size is {size.upper()}.')
    print(f'the text on the front of your tshirt is {text.title()}\n')

print('the following is the default value of the shirt making function:\n')
#make_shirt default values. 
make_shirt()

#positional arguments
make_shirt('medium', 'morbid is the best podcast ever! ')

#keywork arguments
make_shirt(size = 'small', text = 'magnus archives is a great podcast! ')


