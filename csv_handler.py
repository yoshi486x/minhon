import csv


class CSV:
    def __init__(self, in_filename=None, out_filename=None):
        self.in_filename = in_filename
        self.out_filename = out_filename

    def check(self):
        print(self.in_filename)
        print(self.out_filename)
        return

    def scan(self):
        try:
            with open(self.in_filename) as f:
                reader = csv.reader(f)
                bucket = [num for num in reader]
        except Exception as err:
            return None, err
        return bucket, None

    def print(self, bucket):
        try:
            with open(self.out_filename, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(bucket)
        except Exception as err:
            return err
        return None

def run(in_filename, out_filename):
    c = CSV(in_filename, out_filename)
    return c.scan()


if __name__ == "__main__":
    c = CSV(
        in_filename="DeepL_news_dataset2.csv",
        out_filename="Everyone_news_output.csv"
    )
    # scan
    res, err = c.scan()
    if err is not None:
        print(err)
    # print('res:', res)

    # print
    err = c.print(res)
    if err is not None:
        print(err)
    else:
        print('success')