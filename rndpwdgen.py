import random
def main():
   out = open("pwd_list.txt", "a")
   purpose = input("What's the password for?\n")
   out.write(purpose + ": ")
   pwd = ""
   for i in range(random.randint(8, 24)):
      pwd += chr(random.randint(33, 127))
   print(pwd)
   out.write(pwd+'\n')
   out.close()
if __name__ == '__main__':
   main()
