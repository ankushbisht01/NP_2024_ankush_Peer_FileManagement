def store_data(chunks:list , number_of_host:int):
    #use a hashtable to store the data
    data = {}
    for i in range(0, len(chunks)):
        # Store each chunk on two hosts
        data[i % number_of_host] = chunks[i]
        data[(i + 1) % number_of_host] = chunks[i]
    return data

def save_data(data:dict):
    #save the data into a file with a netp format 
    with open("data.netp", "w") as file:
        for key, value in data.items():
            file.write(f"{key} {value}\n")



def main():
    chunks = ['temp/input.wav-0.chunk', 'temp/input.wav-1.chunk' , 'temp/input.wav-2.chunk' , 'temp/input.wav-3.chunk']
    number_of_host = 2
    data = store_data(chunks, number_of_host)
    
    save_data(data)
    
if __name__ == "__main__":
    main()
