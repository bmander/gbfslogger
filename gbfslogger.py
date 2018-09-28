import datetime
import time
from gbfs import Feed

FETCH_PERIOD = 60 #seconds

if __name__=='__main__':
    from sys import argv

    if len(argv) < 3:
        print( "usage: {} feed_url csv_out_fn".format(argv[0]) )
        exit()

    feed_url, csv_out_fn = argv[1], argv[2]

    feed = Feed(feed_url)

    with open(csv_out_fn,"w") as fpout:
        
        # first time, write with header
        bikes = feed.free_bike_status()
        bikes.to_csv(fpout, index=False)
        fpout.flush()

        print( "{}: got {} records".format(datetime.datetime.now(), len(bikes)) )

        while True:

            time.sleep(FETCH_PERIOD)

            try:
                bikes = feed.free_bike_status()
                bikes.to_csv(fpout, index=False, header=False)
                fpout.flush()
                print( "{}: got {} records".format(datetime.datetime.now(), len(bikes)) )
            except Exception as ex:
                print( "{}: encountered problem: {}".format(datetime.datetime.now(), ex))

