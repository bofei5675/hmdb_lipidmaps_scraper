from schema import *
import pandas as pd
import time
from sqlalchemy import *
from sqlalchemy_utils import *
if __name__ == '__main__':
    df = pd.read_table('filtered_lipidmaps.txt',sep = ' ')
    df = df[['V1','V2']]
    print(df.columns.values)
    print(df.shape)
    print(df.head())
    db = RaMP_schema()
    sess = db.session
    sourcetb = db.Source
    for index,row in df.iterrows():
        #print(row)
        hmdbid = row['V1']
        lipidmapsid = row['V2']
        print('Result is {}:{}'.format(hmdbid,lipidmapsid))
        
        hmdbid = 'hmdb:' + hmdbid
        lipidmapsid = 'LIPIDMAPS:' + lipidmapsid
        (res1,), = sess.query(exists().where(sourcetb.sourceId == hmdbid))
        (res2,), = sess.query(exists().where(sourcetb.sourceId == lipidmapsid))
        
        if res1:
            if not res2:
                print('{} is found to {}'.format(hmdbid,lipidmapsid))
                this_ramp = sess.query(sourcetb).filter(sourcetb.sourceId == hmdbid).first()
                rampid = this_ramp.rampId
                commonName = this_ramp.commonName
                newSource = db.Source(sourceId = lipidmapsid,
                                      rampId = rampid,
                                      IDtype = 'LIPIDMAPS',
                                      geneOrCompound = 'compound',
                                      commonName = commonName)
                sess.add(newSource)
                sess.commit()                
                