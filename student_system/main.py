from manager import StudentManager

def main():
    manager = StudentManager()

    manager.load("students.json")

    while True:
        print("\n1) Add student")
        print("2) Show all")
        print("3) Save")
        print("0) Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            score = float(input("Score: "))
            manager.add_student(name, score)
        
        elif choice == "2":
            manager.show_all()
        
        elif choice == "3":
            manager.save("students.json")
        
        elif choice == "0":
            break

        else:
            print("Invalid option.")
        
if __name__ == "__main__":
    main()
