import os
def CleanDir(folder_path: str) -> bool:
  try:
     
    # Get the list of filenames in the folder
    filenames = os.listdir(folder_path)
    # Iterate over the filenames and delete each file
    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return True
  except Exception as e:
     print("--> Error while cleaning directory, "+str(e))
     return False