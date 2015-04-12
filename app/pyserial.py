import serial
import time
from time import gmtime, strftime
import sqlite3

def getcurtime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


class Database:
    _NAME = 'parkbase.db'

    def __init__(self):
        self.conn = sqlite3.connect(Database._NAME)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        self.cursor.close()

    def __exit__(self):
        self.conn.close()

    def update(self, sensor_id, occupied):

        value = 1 if occupied else 0

        stat = "UPDATE parkinglot set value={1},time='{2}' where location={0};".format(sensor_id,
                                                                                    value,
                                                                                    getcurtime())
        self.cursor.execute(stat)
        self.conn.commit()


    def create(self):
        self.cursor.execute("""CREATE TABLE parkinglot (
location INTEGER NOT NULL PRIMARY KEY,
value INTEGER,
time TEXT)""")

    def add_sensor(self, sensor_id):

        value=0
        stat = """INSERT INTO parkinglot values ({0}, {1}, '{2}')""".format(sensor_id,
                                                                            value,
                                                                            getcurtime())
        self.cursor.execute(stat)
        self.conn.commit()


    def read(self, sensor_id):
        self.cursor.execute("SELECT * FROM parkinglot WHERE '\
                            'location='%s'" % sensor_id)

        data = self.cursor.fetchone()

        if data:
            loc, val, time = data[0], data[1], data[2]
            occupied = True if val == 1 else False
            return (loc, occupied, time)

    def read_sensor(self):
        port = serial.Serial('/dev/ttyUSB0', baudrate=115200,
                             timeout=3.0)
        return port.read(3)


def read_from_db():
    db = Database()
    return db.read(10001)


def main():
    db = Database()

    try:
        db.create()
        db.add_sensor(10001)
    except sqlite3.OperationalError:
        pass

    while True:
        time.sleep(1)
        val = db.read_sensor()
        try:
            # you get 'O' when Occupied, 'F' when free
            val = val.strip().decode('utf-8')
            val = True if val == 'O' else False
            print(val)
            db.update(10001, val)
        except UnicodeDecodeError:
            pass


if __name__ == '__main__':
    main()
