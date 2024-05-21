# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"6353.00","system":"readv2"},{"code":"635B.00","system":"readv2"},{"code":"Q11..11","system":"readv2"},{"code":"Q11z.00","system":"readv2"},{"code":"Q110.11","system":"readv2"},{"code":"6351.00","system":"readv2"},{"code":"635A.00","system":"readv2"},{"code":"6356.00","system":"readv2"},{"code":"635..13","system":"readv2"},{"code":"Q317100","system":"readv2"},{"code":"6357.00","system":"readv2"},{"code":"6352.00","system":"readv2"},{"code":"Q111.00","system":"readv2"},{"code":"Q456.00","system":"readv2"},{"code":"Q110.00","system":"readv2"},{"code":"23926.0","system":"readv2"},{"code":"46795.0","system":"readv2"},{"code":"7828.0","system":"readv2"},{"code":"107078.0","system":"readv2"},{"code":"17968.0","system":"readv2"},{"code":"19598.0","system":"readv2"},{"code":"106617.0","system":"readv2"},{"code":"20429.0","system":"readv2"},{"code":"29996.0","system":"readv2"},{"code":"45702.0","system":"readv2"},{"code":"17915.0","system":"readv2"},{"code":"35209.0","system":"readv2"},{"code":"47154.0","system":"readv2"},{"code":"48011.0","system":"readv2"},{"code":"27662.0","system":"readv2"},{"code":"32439.0","system":"readv2"},{"code":"1211.0","system":"readv2"},{"code":"23670.0","system":"readv2"},{"code":"26683.0","system":"readv2"},{"code":"11829.0","system":"readv2"},{"code":"29074.0","system":"readv2"},{"code":"164.0","system":"readv2"},{"code":"19574.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('prematurity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["prematurity---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["prematurity---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["prematurity---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
