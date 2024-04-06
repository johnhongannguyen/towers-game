from stack import Stack

print("\n Towers of Hanoi game ")

# create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]

# Set up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)
    # left_stack.print_items()

num_optimal_moves = (2 ** num_disks - 1)
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

# User Input


def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {name} for {letter}")
