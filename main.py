import sys
from App import App

def main():
    # Command line arguments
    if len(sys.argv) != 3 or (sys.argv[2] != "gui" and sys.argv[2] != "console"):
        print("Usage: " + sys.argv[0] + " <input sudoku filename> <gui/console>")
        return

    # Extracting command line arguments
    sudoku_file = sys.argv[1]
    gui_active = (sys.argv[2] == "gui")

    print("Sudoku File:", sudoku_file)
    print("GUI Active:", gui_active)

    app = App(gui_active, sudoku_file)
    app.run()

if __name__ == "__main__":
    main()
