if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N): #The programw will run for this many times
        ask = input() #Enter the action to be performed
        ask_list = ask.split()
        if ask_list[0] == 'insert': #used to add elements to the list at a specific place
            l.insert(int(ask_list[1]), int(ask_list[2]))
        elif ask_list[0] == 'print': #Used to print the list
            print(l)
        elif ask_list[0] == 'remove': #Used to remove elemenst from the list using the value of the element
            l.remove(int(ask_list[1]))
        elif ask_list[0] == 'append':
            l.append(int(ask_list[1]))
        elif ask_list[0] == 'sort':
            l.sort()
        elif ask_list[0] == 'pop':
            l.pop()
        elif ask_list[0] == 'reverse':
            l.reverse()
        else:
            print("Please enter a valid command")
            