from django.core.management.base import BaseCommand
from ICD_codes.models import MainCode, SubCode
import csv

def main():
    with open('MainCode.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ICD Main Code', 'Description'])  # Writing header
        for main_code in MainCode.objects.all():
                writer.writerow([main_code.ICD_main_code, main_code.description])

        # Export SubCode data
        with open('SubCode.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ICD Main Code', 'ICD Sub Code', 'Description'])  # Writing header
            for sub_code in SubCode.objects.all():
                writer.writerow([sub_code.ICD_main_code.ICD_main_code, sub_code.ICD_sub_code, sub_code.description])


if __name__ == "__main__":
    main()