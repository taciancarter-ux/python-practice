import sys
import time

def slow_print (text,delay=0.03):
    """Prints text character by character for a dramtic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def Birthday_letter(name, sender):
    banner = f"""
    **********************************************************
    *                                                        *
    *                                                        *
    *               H A P P Y    B I R T H D A Y             *
    *                        {name}                          *
    **********************************************************       
    """

    letter = f"""
        Dearest {name},
        
        Happy Birthday! On this special day, I wanted to create this code to remind you how much light and 
        Happiness you bring to everyone around you.It is very rare to cross paths with someone who leaves
        such a memorable impression.Thank you for being yourself and I hope this year brings you closer to
        you aspirations and being as happy as you possibly can along with a favorable adventure.
        
        Celebrate yourself today.You only turn 20 once anddd eat some cake!!
        
        With warm wishes,
        {sender}
    """

    print (banner)
    time.sleep( 1 )
    slow_print(letter, delay=0.02)
if __name__ =="__main__":
    friend_name = "Nashella"
    your_name   = "Tacian"

Birthday_letter(friend_name, your_name)



