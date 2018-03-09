import pymysql
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request as RE
import urllib.error as ER
from multiprocessing import Pool
import socket

class LipidMaps():
    def __init__(self):
        self.hmdbToLipidmaps = dict()
        self.hmdbids = []
        self.downloaded_id = dict()
    def getHmdbIDfromRaMP(self):
        conn = pymysql.connect(host = 'localhost',
                      user = 'root',
                      passwd = 'Ehe131224',
                      db = 'mathelabramp')
        hmdbids = pd.read_sql('select * from source;',conn)
        hmdbids = hmdbids.loc[hmdbids['IDtype'] == 'hmdb',]
        hmdbids = hmdbids.sourceId.str.replace('hmdb:','')
        hmdbids = hmdbids.unique()
        self.hmdbids = hmdbids.tolist()
        conn.close()
    def getDownloaded_id(self):
        f =  open('lipidmaps.txt','r')
        downloaded_id = [x.rstrip('\n') for x in f if x != '\n']
        downloaded_id = {x.split('\t')[0]:x.split('\t')[1] for x in downloaded_id}
        #print(downloaded_id)
        self.downloaded_id = downloaded_id
        f.close()
        '''
    def getURL(self):
        for id in self.hmdbids:
            if id not in 
            '''
    def htmlParser(self,numbers):
        url = 'http://www.hmdb.ca/metabolites/'
        while len(self.hmdbids) > 0:
            
            id = self.hmdbids.pop(0)
            print('{} hmdb id left at {}...'.format(len(self.hmdbids),id))
            if id not in self.downloaded_id:
                try:
                    page = RE.urlopen(url + id,timeout=10)
                    soup = BeautifulSoup(page.read(),'html.parser')
                    external_links = soup.findAll('a',
                                                  {'class':'wishart-link-out'})
                    found = False
                    for each in external_links:
                        attrs = each.attrs
                        content = each.text
                        if 'lipidmaps' in attrs['href']:
                            print('{} has lipidmaps id {}'.\
                                  format(id,content.replace(' ','')))
                            with open('lipidmaps.txt','a') as f:
                                f.write('{}\t{}\n'.format(id,content))
                            self.downloaded_id[id] = content
                            found = True

                    if not found:  
                        with open('lipidmaps.txt','a') as f:
                            f.write('{}\t{}\n'.format(id,'NA'))
                        self.downloaded_id[id] = 'NA'
                except ER.HTTPError:
                    print('HTTP Not Found')
                    pass
                except ER.URLError:
                    print('Poor url formation')
                    pass
                except socket.timeout:
                    print('socket timeout')
                    pass
     
if __name__ == '__main__':
    ldmaps = LipidMaps()
    ldmaps.getHmdbIDfromRaMP()
    ldmaps.getDownloaded_id()
    ldmaps.htmlParser(0)
    '''
    with Pool(5) as p:
        p.map(ldmaps.htmlParser,range(0,len(ldmaps.hmdbids)))
        '''
    