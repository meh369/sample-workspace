from  time import sleep

print('Best practices')

def process_data(data):
    print("Reading data...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Completed processing.")
    return modified_data

def read_data_from_web():
    print("Reading from web")
    data = "Data scrapped from web"
    return data

def write_data_to_database(data):
    print("Written to database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__=="__main__":
    main()
    