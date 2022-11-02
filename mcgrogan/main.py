from time import sleep
import generate_data

# how to write a function
def process_data(data):
    print("Begin data processing...")
    sleep(2)
    print("data processed")
    
def main():
    print("hello world")
    process_data(2)
    print(generate_data.data_points())
    
if __name__ == "__main__":
    main()
