
#t8-10 
#pass a list of text messages to a function
#pass the list of text messages to a function that 
#that appends the messages to a new list 
def make_texts(completed_messages):
    """a function that takes a list of messages (str), and prints them out"""
    for complete_message in completed_messages:
        print(f"these messages have been sent: {complete_message.title()}")

def send_messages(unprinted_messages, completed_messages):
    """a message that verifies sent text messages from a list."""
    #the while loop will run until no other messages are available to print
    while unprinted_messages:
        send_message = unprinted_messages.pop()
        #t a print statement for verification that the message is sending. 
        print(f"\nSending the following message: {send_message}")
        completed_messages.append(send_message)
        
  
unprinted_messages = ['hello', 'how are you?', 'who are you?', 'how are you?']
completed_messages = []

#call function and pass with the argument targeting the previous line. 
#t calling this function first to make certain that the lists align with the needed task. 
send_messages(unprinted_messages, completed_messages)
make_texts(completed_messages)

#print out both lists for verification. 
print('\n')
print(unprinted_messages)
print(completed_messages)


