from stack import Stack

print("\n Towers of Hanoi game ")

# create the Stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]

# Set up the game
