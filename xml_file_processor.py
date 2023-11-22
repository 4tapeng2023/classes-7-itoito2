import xml.etree.ElementTree as ET
from typing import Dict


class FileProcessor:
    def read_file(self, filename: str) -> Dict:
        try:
            file_content = []

            tree = ET.parse(filename)
            root = tree.getroot()

            for child in root:
                temp_dict = {}

                for element in child:
                    temp_dict[f"{element.tag}"] = element.text

                file_content.append(temp_dict)

            return file_content
        
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    
    def add_record(self, filename: str, record: Dict) -> None:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()

            new_pirate = ET.SubElement(root, "pirate")

            for key, value in record.items():
                ET.SubElement(new_pirate, key).text = value

            tree = ET.ElementTree(root)
            tree.write(filename)

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def delete_record(self, filename: str, record_id: int) -> None:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            
            pirate_to_delete = root.find(f"./pirate[id='{record_id}']")
            
            if pirate_to_delete is not None:
                root.remove(pirate_to_delete)
                
                tree.write(filename)
                print(f"Pirate with ID {record_id} deleted successfully.")
            else:
                print(f"No pirate found with ID {record_id}.")
                
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


    def udpate_record(self, filename: str, record_id: int, new_record: str) -> None:
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            
            pirate_to_update = root.find(f"./pirate[id='{record_id}']")
            
            if pirate_to_update is not None:
                for key, value in new_record.items():
                    existing_element = pirate_to_update.find(key)
                    if existing_element is not None:
                        existing_element.text = value
                    else:
                        ET.SubElement(pirate_to_update, key).text = value
                
                tree.write(filename)
                print(f"Pirate with ID {record_id} updated successfully.")

            else:
                print(f"No pirate found with ID {record_id}.")
                
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


    def display_records(self, filename: str) -> None:
        try:
            file_content = []

            tree = ET.parse(filename)
            root = tree.getroot()

            for child in root:
                temp_dict = {}

                for element in child:
                    temp_dict[f"{element.tag}"] = element.text

                file_content.append(temp_dict)

            for pirate in file_content:
                print(pirate)
        
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
