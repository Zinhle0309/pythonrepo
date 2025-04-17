def modify_file(input_file, output_file):
    """
    Reads the content of the input file, modifies it, and writes it to the output file.
    """
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.readlines()

        # Modify the content (example: convert all text to uppercase)
        modified_content = [line.upper() for line in content]

        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"File has been successfully modified and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except ProcessError:
        print(f"Error: The file {input_file} is not accessible.")
        


# Example usage
if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    modify_file(input_file, output_file)