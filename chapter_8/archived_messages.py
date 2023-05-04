#exercise 8-11: archived messages
#call a copy of the list of messages. 

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
        
#a list containing the messages. 
unprinted_messages = ['hello', 'how are you?', 'who are you?', 'what are you?']
#an empty list that the messages will append to.
completed_messages = []

#call the dang thing
send_messages(unprinted_messages[:], completed_messages)
print(f"\nVerification of the copied list and the original list:")
print(unprinted_messages)
print(completed_messages)