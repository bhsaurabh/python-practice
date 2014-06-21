#!/usr/bin/python

def move_tower(height, from_pole, to_pole, with_pole):
    if height < 1:
        return  # base case
    # Step 1: Move tower of height-1 to intermediate pole, using final pole
    move_tower(height-1, from_pole, with_pole, to_pole)
    # Step 2: Move a disc from source pole to final pole
    move_disk(from_pole, to_pole)
    # Step 3: Move height-1 tower from intermediate pole to final pole
    move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole, to_pole):
    print("Moving disk from %s to %s." % (from_pole, to_pole))


if __name__ == '__main__':
    move_tower(5, "A", "C", "B")
    