from pandas import DataFrame, read_excel
from argparse import ArgumentParser
from os import remove


def change_file_format_to_csv(filename):
    filename = filename.split(".")
    filename[-1] = 'csv'


if __name__ == "__main__":
    # Parse arguments
    # parser = ArgumentParser()
    # parser.add_argument("-i", "--input", default="", required=False,
    #                     help="Input file to be converted")
    # args = parser.parse_args()

    # Load input
    # print(args.input)
    content = read_excel("output.xlsx")

    # Store input as CSV
    content.to_csv("output.csv")