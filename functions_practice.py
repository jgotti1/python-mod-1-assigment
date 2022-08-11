# 1.
def hello():
    print("Hello User")

hello()
#2
def pack(one,two,three):
    return[one,two,three]
    
print(pack("shirt","shorts","socks"))
print(pack(1,2,3))


#3
def eat_lunch(lunch):
  if len(lunch) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch)):
      if i == 0:
        print(f"First I eat {lunch[0]}")
      else:
        print(f"Next I eat {lunch[i]}")


eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["cake","cookies","sandwich","steak"])
   