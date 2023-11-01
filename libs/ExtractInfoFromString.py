import re


def extract_information(input_string):
    try:
      # Preprocess input_string
      input_string = input_string.strip()
      # Replace all \n\n with \n      
      input_string = input_string.replace('\r\n', '\n')
      input_string = input_string.replace('\n\n', '\n')

      # Define regex patterns for each field
      name_pattern = r'नाव\s*:\s*([^\n]+)'
      father_name_pattern = r'वडीलांचे नाव\s*:\s*([^\n]+)'
      house_number_pattern = r'घर क्रमाक\s*:\s*([^\n]+)'
      age_pattern = r'वय\s*:\s*(\d+)'
      gender_pattern = r'लिंग\s*:\s*([^\n]+)'
      id_pattern = r'ISF(\d+)'

      names = re.findall(name_pattern, input_string)
      father_names = re.findall(father_name_pattern, input_string)
      house_numbers = re.findall(house_number_pattern, input_string)
      ages = re.findall(age_pattern, input_string)
      genders = re.findall(gender_pattern, input_string)
      ids = re.findall(id_pattern, input_string)
      # Open the file in append mode
      with open('data.txt', 'a', encoding='utf-8') as file:
          # Append data to the file
          file.write('---------------------------------\n')
          file.write(input_string)
          file.write('---------------------------------\n')
      # Combine the extracted information into a list of dictionaries
      extracted_information = []
      for i in range(len(names)):
          entry = {
              'no': i + 1,
              'name': names[i] if i < len(names) else 'Error Name',
              'fname': father_names[i] if i < len(father_names) else 'Error Father name',
              'hno': house_numbers[i] if i < len(house_numbers) else 'Error house number',
              'age': ages[i] if i < len(ages) else 'Error Age',
              'gender': genders[i] if i < len(genders) else 'Error Gender',
              'ID': 'ISF' + ids[i] if i < len(ids) else 'Error ID'
          }
          extracted_information.append(entry)

      return extracted_information
    except Exception as e:
      print("Error in Extracting Information from string: ", str(e))
      return []