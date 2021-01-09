import xlsxwriter
import csv


class File:

    def __init__(self, filename, schedule):
        self.filename = filename
        self.schedule = schedule

    def txt_file(self):
        """Creates a txt file."""

        filename = self.filename
        schedule = self.schedule
        with open(filename, 'w') as f:
            f.write("\tHOURS\t\t\t\tACTIVITIES\n")
            for i in range(1, 25):
                if i < 10:
                    f.write(f"{schedule[i].replace('  ', ' ').replace('- ', '-  ')}\n")
                else:
                    f.write(f"{schedule[i]}\n")

    def xlsx_file(self):
        """Creates a xlsx file."""

        filename = self.filename
        schedule = self.schedule
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet("Schedule")

        new_list = []
        for v in schedule.values():
            new_list.append([v[:18], v[19:]])

        row = 0
        column = 0

        for hour, activity in new_list:
            worksheet.write(row, column, hour)
            worksheet.write(row, column + 1, activity)
            row += 1

        workbook.close()

    def csv_file(self):
        """Creates a csv file."""

        filename = self.filename
        schedule = self.schedule
        with open(filename, 'w') as f:
            fields = ['hour', 'activity']
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            writer = csv.writer(f)

            for v in schedule.values():
                if len(v) == 18:
                    row = {f" {v[:19].lstrip()}": v[19:]}
                else:
                    row = {v[:19]: v[19:]}
                writer.writerow(row)
