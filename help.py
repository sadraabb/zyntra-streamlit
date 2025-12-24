import sys
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"  # برای برگشت به رنگ پیش‌فرض
def main():
    while True:
        print(f"""{CYAN}
Guide for the Web-Based Entertainment Games Project:
1: Help for How Run This App
2: Requirments
0 : Exit

""")
        choice = int(input("Select an option: \n"))
        if choice == 1:
            print("""
Guide to Run the App (Windows):

1. Navigate to the project folder in your terminal.
2. Run the app with the following command:
   python -m streamlit run main.py

After executing the command, a browser window should open automatically 
showing the Web-Based Entertainment Games App.

Note: This command works on Windows. On Linux or Mac, you may use:
   streamlit run main.py
""")
            sys.exit()
        elif choice == 2:
            print("""
Requirements / Libraries Used:

1. streamlit - For building the web-based interactive app
2. random - To generate random numbers (used for user ID)
3. (Add any other libraries you use in your project here)

Installation Command:
   pip install streamlit

Make sure all libraries are installed before running the app.
""")
            sys.exit()
        elif choice == 0:
            print("Exiting the guide. Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Please select 1, 2, or 0.\n")



if __name__ == "__main__":
    main()