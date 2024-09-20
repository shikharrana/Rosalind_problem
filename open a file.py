
    try:
    # Open the file in read mode
        with open('rosalind_revc.txt', 'r') as file:
        # Read the file content
            content = file.readline()
            print(content)

    except Exception as e:
    # Print any exception that occurs
        print(e)

