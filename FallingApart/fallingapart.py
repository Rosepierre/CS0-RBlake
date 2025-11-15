#Roger Blake 
#solves the falling apart kattis problem




def get_numbers():

    numberofints = int(input())
    integer = list(map(int, input().split()))
    integer.sort(reverse=True)

    return integer

def exvaluation(integer):

    alice_turns = 0
    bob_turns = 0

    for i in range(len(integer)):
        if i % 2 == 0:
            alice_turns += integer[i]
        else:
            bob_turns += integer[i]
    print(f"{alice_turns} {bob_turns}")
    

integer = get_numbers()
exvaluation(integer)