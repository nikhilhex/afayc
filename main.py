from art import text2art
from colorama import Fore
import time

print(text2art("a.f.a.y.c", font='big'))
print(text2art("by nikhilhex", font='bell'))

print(f"{Fore.RED}Directions{Fore.GREEN}:{Fore.CYAN} You will have half a second to type a random letter and hit {Fore.LIGHTRED_EX}enter{Fore.CYAN}. If you accidentally type nothing, then you {Fore.RED}lose{Fore.CYAN}. If you run out of time, you {Fore.RED}lose{Fore.CYAN}. When you are ready to play, type {Fore.LIGHTBLUE_EX}ready{Fore.CYAN} to start")
st = input()
if st == "ready":
  for x in range(9223372036854775807):
    if x != 0:
      st = time.time()
      tmp = input(f"{x}) ")
      end = time.time()
      if end - st > 1 or tmp == "":
        print(f"{Fore.RED} You FAILED")
        print(f"Score: {x}. Better luck next time!")
        exit(0)