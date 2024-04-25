import sys
import os
import glob

def split_file_into_chunks(absolute_path: str):
    # Splits the file into chunks
    # so Telegram can handle it (2GB max)
    chunks = []

    file_size = os.path.getsize(absolute_path)

    frame_size = 4 

    # 50 MB chunk size 
    chunk_size = 10*1024*1024     

    if file_size > chunk_size:
        # Create temp directory if it doesn't exist
        temp_dir = os.path.join(os.path.dirname(sys.argv[0]), "temp")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # Split the file into chunks
        with open(absolute_path, "rb") as file:
            # print(f"Splitting {absolute_path} into chunks...")
            chunk_num = 0
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                # Write the chunk to a file in `temp`
                chunk_file_path = os.path.join(
                    temp_dir,

                    f"{chunk_num}-{os.path.basename(absolute_path)}.chunk"
                )
                # print(f"Writing chunk to {chunk_file_path}...")

                with open(chunk_file_path, "wb") as chunk_file:
                    chunk_file.write(chunk)

                chunks.append(chunk_file_path)
                chunk_num += 1

    else:
        # No need to split the file
        chunks.append(absolute_path)

    return chunks



def combine_chunks(chunks_list, output_file):
    with open(output_file, "wb") as outfile:
        for chunk_file in chunks_list:
            with open(chunk_file, "rb") as infile:
                outfile.write(infile.read())
            # Optionally, remove the chunk file after reading
            os.remove(chunk_file)


