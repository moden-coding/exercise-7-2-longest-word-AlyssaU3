# Write your solution here
def longest(lst : list):
   long = lst[0]
   for word in lst:  
       if len(word)>len(long):
           long= word
   return long
    # pass
    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
    