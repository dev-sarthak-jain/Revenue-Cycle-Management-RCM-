file_path = ''
#file_path = 'extra_files\\icd10cm_order_2024.txt'
#file_path = 'extra_files\\codes_test.txt'
from .models import MainCode, SubCode
previous = None

def main():
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into fields based on whitespace
            fields = line.split()
            
            # Check if there are enough fields before attempting to access them
            if len(fields) >= 5:
                # Exclude the first and the last fields, capture the three middle fields
                code, heading = fields[1], fields[2]
                length = len(fields[3:])
                description_list = fields[3 + int(length / 2):]
                # Join the list elements into a single string
                description = " ".join(description_list)
                heading = int(heading)

                if heading == 0:
                    # Save to MainCode model
                    print(description)
                    main_code = MainCode(ICD_main_code=code, description=description)
                    main_code.save()
                    previous = main_code  # Save the MainCode object for foreign key reference in SubCode
                elif heading == 1:
                    # Save to SubCode model
                    if previous is not None:
                        sub_code = SubCode(ICD_main_code=previous, ICD_sub_code=code, description=description)
                        sub_code.save()

if __name__ == "__main__":
    main()