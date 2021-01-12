import xlsxwriter
import csv

# It needs some changes to make it work.
class File:

    def __init__(self, filename, schedule):
        self.filename = filename
        self.schedule = schedule

    def txt_file(self):
        """Creates a txt file."""

        filename = self.filename
        schedule = self.schedule
        with open(filename, 'w') as f:
            f.write("\t\tHOURS\t\t\t\tACTIVITIES\n")
            for key, value in schedule.items():
                for hr, act in value.items():
                    f.write(f"{hr}\t\t{act}\n")

    def xlsx_file(self):
        """Creates a xlsx file."""

        filename = self.filename
        schedule = self.schedule
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet("Schedule")

        row = 0
        column = 0

        headers = ['HOURS', 'ACTIVITIES']
        worksheet._write(row, column, headers[0])
        worksheet._write(row, column + 1, headers[1])

        row += 1

        for key, value in schedule.items():
            for hr, act in value.items():
                worksheet.write(row, column, hr)
                worksheet.write(row, column + 1, act)
                row += 1

        workbook.close()

    def csv_file(self):
        """Creates a csv file."""

        filename = self.filename
        schedule = self.schedule

        # Flattens dict.
        new_dict = []
        for key, value in schedule.items():
            for hr, act in value.items():
                row = {'HOUR': hr, 'ACTIVITY': act}
                new_dict.append(row)

        with open(filename, 'w', newline='') as f:
            fields = ['HOUR', 'ACTIVITY']
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(new_dict)
