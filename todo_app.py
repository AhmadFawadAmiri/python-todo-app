def todo_app():
    filename = "todo.txt"

    while True:
        print("\n--- To-Do List ---")
        print("0. ❌ Exit")
        print("1. 📝 Add Task")
        print("2. 🔎 View Tasks")
        print("3. ✅ Mark a task as done")
        print("4. ✂️  Delete a specific task by number")
        print("5. 🗑  Clear all tasks (with a confirmation)")
        print("6. 📁 Separate files per day or project")
        print("7. 📆 Add due dates to tasks")
        print("8. 📑 Select Task")
        print("9. ⚠️  About")
        print("_______________________________________________________________")

        choice = input("Choose an option (1-9): ")

        if choice == "0":
            print("👋 Exiting. Goodbye!")
            break

        elif choice == "1":
            task = input("Enter your task: ")
            with open(filename, "a") as file:
                file.write(task + "\n")
                print("✅ Task added!")

        elif choice == "2":
            print("\n📋 Your Tasks:")
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                    if not lines:
                        print("No tasks found.")
                    for i, line in enumerate(lines, start=1):
                        print(f"{i}. {line.strip()}")
            except FileNotFoundError:
                print("No task file found yet.")

        elif choice == "3":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()

                if not lines:
                    print("📭 No tasks to mark.")
                else:
                    for i, line in enumerate(lines, start=1):
                        print(f"{i}. {line.strip()}")

                    task_num = int(input("Enter task number to mark as done: "))
                    if 1 <= task_num <= len(lines):
                        lines[task_num - 1] = lines[task_num - 1].strip() + " ✅\n"
                        with open(filename, "w") as file:
                            file.writelines(lines)
                        print("✔️ Task marked as done!")
                    else:
                        print("❌ Invalid task number.")    

            except FileNotFoundError:
                print("No task file found.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()

                if not lines:
                    print("📭 No tasks to delete.")
                else:
                    print("\n🗒 Your Tasks:")
                    for i, line in enumerate(lines, start=1):
                        print(f"{i}. {line.strip()}")
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(lines):
                        deleted_task = lines.pop(task_num - 1).strip()
                        with open(filename, "w") as file:
                            file.writelines(lines)
                        print(f"✂️ Deleted: {deleted_task}")
                    else:
                        print("❌ Invalid task number.")

            except FileNotFoundError:
                print("No task file found.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "5":
            confirm = input("⚠️ Are you sure you want to delete ALL tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                try:
                    open(filename, "w").close()  # Clears file contents
                    print("🗑 All tasks have been deleted.")
                except Exception as e:
                    print("❌ An error occurred while clearing tasks:", e)
            else:
                print("🚫 Clear cancelled. Your tasks are safe.")

        elif choice == "6":
            new_file = input("📁 Enter a name for your to-do file (e.g. work.txt): ").strip()
            if new_file:
                filename = new_file
                print(f"✅ Switched to file: {filename}")
            else:
                print("❌ Invalid filename. Please try again.")

        elif choice == "7":
            task = input("📝 Enter your task: ").strip()
            due_date = input("📆 Enter due date (e.g. 2025-05-20 or Monday): ").strip()
            if task and due_date:
                with open(filename, "a") as file:
                    file.write(f"{task} (Due: {due_date})\n")
                print("✅ Task with due date added!")
            else:
                print("❌ Task and due date cannot be empty.")

        elif choice == "8":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()

                if not lines:
                    print("📭 No tasks to select.")
                else:
                    print("\n📑 Your Tasks:")
                    for i, line in enumerate(lines, start=1):
                        print(f"{i}. {line.strip()}")

                    task_num = int(input("Enter task number to highlight: "))
                    if 1 <= task_num <= len(lines):
                        if "⭐️" not in lines[task_num - 1]:
                            lines[task_num - 1] = "⭐️ " + lines[task_num - 1]
                        with open(filename, "w") as file:
                            file.writelines(lines)
                        print("🌟 Task highlighted!")
                    else:
                        print("❌ Invalid task number.")
            except FileNotFoundError:
                print("No task file found.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "9":
            print("\n⚠️  ABOUT THIS APP")
            print("📝 Python To-Do List App")
            print("📁 Supports multiple files/projects")
            print("📆 Add due dates, mark and highlight tasks")
            print("✂️ Delete, ✅ complete, and 🗑 clear tasks")
            print("💻 Made by [Your Name]")
            print("📅 Last updated: 2025")
            print("\n👨‍💻 AUTHOR INFO")
            print("📛 Name: Ahmad Fawad Amiri")
            print("🌐 Country: Germany")
            print("💼 Role: Python Learner & Developer")
            print("📧 Email: a**************i@gmail.com")
            print("📚 Goal: Learn Python from scratch to mastery 🚀")
            print("_______________________________________________________________")
        
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, 4, 5, or 9.")
            

# Run the App
todo_app()