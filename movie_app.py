display_menu = """********** My Movies Database **********

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Filter movies by rating

Enter choice (1-10): """

class MovieApp:
    def __init__(self,storage):
        self._storage = storage

    def _command_add_movie(self):
        pass

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        print (movies)


    def run(self):
        func_dict = {
            "1": self._command_list_movies,

        }
        """Main function to display the menu and handle user inputs."""
        print(display_menu)
        while True:
            try:
                user_input = input("Enter your choice: ").strip()

                if user_input == "0":
                    print("Bye!")
                    break

                # Retrieve the function associated with the user input
                func_id = func_dict.get(user_input)

                if func_id:
                    # Call the selected function
                    func_id()
                else:
                    # If user_input is not in func_dict or 0, print an error message
                    print("Invalid option. Please enter a valid choice.")

            except KeyError:
                print("Invalid option. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a number.")

            except Exception as e:
                # Catch any other unexpected errors and display them
                print(f"An unexpected error occurred: {e}")

            # Display the menu again for the next round of input
            input("\nPress Enter to display the menu...")
            print(display_menu)