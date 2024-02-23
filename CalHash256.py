import hashlib
import os
import argparse
import shutil
argv = argparse.ArgumentParser()
argv.add_argument('-p ', '--Path', default="")

def GetSHA256(filename):
    sha256_hash = hashlib.sha256()
    try:
        with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        return(sha256_hash.hexdigest())
    except IOError as e:
        write_log(f"Get sha {filename} fail as err: {e}")
        return False
  
def write_log(message):
    with open('logCalHash.txt', 'a',encoding="UTF-8") as log_file:
        log_file.write(message + '\n')       


if __name__ == '__main__': 
    szScanFolder = argv.parse_args().Path
    if not os.path.exists(szScanFolder+"\\HashResult"):
        os.mkdir(szScanFolder+"\\HashResult")
    files = os.listdir(szScanFolder)
    for file in files:            
        file_hash = GetSHA256(f"{szScanFolder}\\{file}")
        if file_hash == False:
            continue
        if os.path.exists(f"{argv.parse_args().Path}\\HashResult\\{file_hash}"):
            continue
        try:
            write_log(f"{szScanFolder}\\{file} with hash:{file_hash} copy to {argv.parse_args().Path}\\HashResult\\{file_hash}")
            shutil.move(f"{szScanFolder}\\{file}",f"{argv.parse_args().Path}\\HashResult\\{file_hash}")
        except IOError as e:
            write_log(f"{szScanFolder}\\{file} with hash:{file_hash} copy to {argv.parse_args().Path}\\HashResult\\{file_hash} Error: {e}")
            continue   
        


