import json
def store_data(chunks:list , number_of_host:int):
    #use a hashtable to store the data
    data = {}
    for i in range(0, len(chunks)):
        #assign the chunks to i%2 host
        host = f"Host{i%number_of_host}"
        if host not in data:
            data[host] = {
                "HostIP":"127.0.0.1", 
                "PORT": 5050 + i%number_of_host,
                "chunks": [chunks[i]]
            }
        else:
            data[host]["chunks"].append(chunks[i])
    
    
    #save in a json file
    with open("data.json", "w") as file:
        json.dump(data, file)

    return data






def main():
    chunks = ['temp/input.wav-0.chunk', 'temp/input.wav-1.chunk' , 'temp/input.wav-2.chunk' , 'temp/input.wav-3.chunk']
    number_of_host = 2
    data = store_data(chunks, number_of_host)
    print(data)
    
    
if __name__ == "__main__":
    main()
