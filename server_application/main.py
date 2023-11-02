import sys
from CONSTANTS import *
from app import app


def main():
    app.run(host=HOST, port=5000, debug=True)


if __name__ == "__main__":
    main()
