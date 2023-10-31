import re


def extract_information(input_string):
    try:
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

      # Combine the extracted information into a list of dictionaries
      extracted_information = []
      for i in range(len(names)):
          entry = {
              'Serial No': i+1,
              'नाव': names[i],
              'वडीलांचे नाव': father_names[i],
              'घर क्रमांक': house_numbers[i],
              'वय': ages[i],
              'लिंग': genders[i],
              'ID': 'ISF' + ids[i]
          }
          extracted_information.append(entry)

      return extracted_information
    except Exception as e:
      print("Error in ExtractText", str(e))
      return []