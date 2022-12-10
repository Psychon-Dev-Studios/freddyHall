import os, sys
from modules.constants import manifest
PATH = sys.path[0]
version = manifest.appVersion

checksum_dirs= ["/assets", "/settings"]
full_checksum = []
final_checksum = []

print("Generating checksums for the following directories: %s\n\n"%(checksum_dirs))


for targetDIR in checksum_dirs:
    generated_checksum = []

    for root, subfolders, filenames in os.walk(PATH + targetDIR):
        for file in filenames:
            if not ".pyc" in file:
                generated_checksum.append(file)

    full_checksum.append(generated_checksum)

full_checksum.append(version)




print("Generated checksum:")
print(full_checksum)