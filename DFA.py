
class DFA:
    def getDFA():
    my_states=input("State names: ") #gets the states from the user
    states = my_states.split()  #splits the states
    my_alphabets= input("Alphabet: ").split()#gets the alphabet from the user
    my_dict={} #creates empyty dictinary
    #transition table
    print("Enter transition table: ")
    for z in range(len(my_alphabets)):
        print(my_alphabets[z],end=' ')
    print()
    for a in states:
        this_input=input(a + ": ").split()
        for x in range(len(this_input)):
            my_tuple=(a,my_alphabets[x])
            my_dict[my_tuple] = this_input[x]

    start=input("Start state: ") #gets the start state from the user
    final=list((input("Final state: ")))

    #takes in from the user a string whose acceptibility is to be tested
    test_string= input("Please enter a string digit: ")
    current_state=start
    for i in range(len(test_string)):
        new_tuple = (current_state,test_string[i]) #stores dictionary key
        new_state=my_dict[new_tuple]
        current_state=new_state
    if current_state==final[0]:
        return True #accepting state
    else:
        return False #rejecting state
