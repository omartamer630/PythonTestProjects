import time

index = 0
storage = 1
bookShelf = [None] * storage
condition = input("Want to add a book ? [Y/n] ").capitalize().strip()

while condition in ["Yes","Y"]:

  if storage > 0 :

    print(f"You Have {storage} Storage for Books")

    bookShelf[index] = input("Please enter your book name :")

    print("Adding a book to your BookShelf..")
    time.sleep(1.5)
    print("Book has been added!")
    storage-=1

    condition = input("Want to add another book ? [Y/n] ").capitalize().strip()
    index += 1
  else :

    print("No more storage left for books.")
    condition = input("add more Storage ? [Y/n] ").capitalize().strip()

    if condition in ["Yes","Y"] :

      additional_storage = int(input("How many storage spaces do you want to add? ").strip())
      bookShelf.extend([None] * additional_storage)
      storage += additional_storage
      print("Adding more storage...")

      time.sleep(1.5)
      print(f"Storage has been increased by {additional_storage}!")
      condition = "Y"

    else :

      condition = None

else :

  print("See You Soon ^^")
