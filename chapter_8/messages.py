#8-9
#pass a list of text messages to a function
def make_texts(texts):
    """a function that takes a list of messages (str), and prints them out"""
    for text in texts:
        print(text.title())

messages = ['hello', 'how are you?', 'who are you?', 'how are you?']

#call function and pass with the argument targeting the previous line. 
complete_messages = make_texts(messages)
