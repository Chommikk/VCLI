from linkedin import text_to_linkedin
from image_encoding import hide_message, get_message
import sys
import os

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "pull":
       print(get_message("hidtest.png"))

    elif len(sys.argv) == 3 and sys.argv[1] == "initialize":
        if os.path.exists(".vcli"):
            print("repository is already initialized")
        else:
            with open(".vcli", "w") as f:
                f.write(sys.argv[2])
            print("repository initialized")

    elif len(sys.argv) == 3 and sys.argv[1] == "push":
        if not os.path.exists(".vcli"):
            print("repository not initialized cannot push")
        else:
            with open("main.py") as f:
                content = f.read()
            hide_message(content, "test.png")

if __name__ == "__main__":
    main()
