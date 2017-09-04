import zipfile
# create the ZIP file
print("--------------------------------------------------")

zip_file = zipfile.ZipFile("sample.zip","w")
zip_file.write("sets.py");
zip_file.write("FileHandling.py")
zip_file.close()

print(zipfile.is_zipfile("sample.zip"))
print(zip_file.namelist())


print("--------------------------------------------------")