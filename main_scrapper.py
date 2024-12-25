import os

def main():
    print("Welcome to the Scraper Tool!")
    print("Choose an option:")
    print("1. Scrape news from CNN")
    print("2. Search and scrape content from Wikipedia")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice == 1:
            print("\nYou chose to scrape news from CNN.")
            os.system('python3 cnn_scrapper.py')  # Call the CNN scraper script
        elif choice == 2:
            print("\nYou chose to search and scrape content from Wikipedia.")
            # Prompt user for a search term
            search_term = input("Enter the Wikipedia page you want to search: ")
            os.system(f'python3 wikipedia_scrapper.py "{search_term}"')  # Call the Wikipedia scraper with the search term
        else:
            print("Invalid choice! Please enter 1 or 2.")
            main()  # Restart the main function for valid input
        
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
        main()  # Restart the main function for valid input

if __name__ == "__main__":
    main()
